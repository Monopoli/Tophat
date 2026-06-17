"""
cluster_portals.py — Halo 2 Xbox render-cluster portal parser and renderer.

Drop-in companion to ui_bsp.py and trigger_volumes.py.  Provides:
  - parse_cluster_portals(map_path) -> list[list[ClusterPortal]]   (one list per sbsp section)
  - get_cluster_portals(map_path)   -> cached version
  - ClusterPortalMixin              (mix into the same class as BspMixin)

Confirmed structure (cross-checked against Sbsp.txt, the Halo 2 "sbsp" tag
plugin layout):

  Cluster portals are their OWN standalone reflexive (count, ptr) at sbsp
  meta +0x5C, stride 0x24 (36) bytes/entry — entirely separate from the
  "Clusters" render-mesh reflexive at +0x9C:

    +0x00  back_cluster    int16   cluster behind the portal (-1 = none/outside)
    +0x02  front_cluster   int16   cluster in front of the portal
    +0x04  plane_index     int32   index into a plane list (not resolved here)
    +0x08  centroid        point3  polygon centroid, world units
    +0x14  radius          float32 bounding radius
    +0x18  flags           flags32 AI-cannot-hear / one-way / door / no-way / ...
    +0x1C  vertices        reflexive (count, ptr) -> point3 array, stride 0xC

  Each portal's vertex polygon is read straight from its own nested
  reflexive (XYZ only, 12 bytes/vertex — no extra trailing float). The
  reflexive pointer is translated to a relative offset within the sbsp meta
  the same way the top-level reflexive is: rel = ptr - voff (voff being the
  tag's own file-relative offset), applied uniformly whether the reflexive
  is top-level or nested, since pointers throughout one tag's meta share
  the same virtual-address base.

  History: before Sbsp.txt was available, this module located portals via
  a different, heuristic model: scan the "Clusters" reflexive at +0x9C,
  treat the first 80 bytes of each (variable-stride) cluster entry as a
  stable header, and read a "first_portal_vertex"/"portal_vertex_count"
  u16 pair at +36/+38 indexing into a separate shared vertex pool at
  +0xF4. Sbsp.txt shows that model was wrong: the real "Clusters" struct
  is fixed-stride (0xB0 bytes), and its real fields at +0x24/+0x26 are
  "Total Subpart Count" / "Section Lighting Flags" — unrelated to portals.
  Whatever the old heuristic was matching against to recover 31 plausible-
  looking polygons in 01b_spacestation was coincidental aliasing, not the
  real portal data, so it has been removed rather than kept as a fallback.
  Each render Cluster does separately carry its own list of portal indices
  (a "Portals" reflexive at Clusters-entry +0x8C, just int16 indices into
  this module's array) if a future feature wants per-cluster portal
  membership — not read here since rendering only needs the polygons.

Integration
------------
1.  Import alongside trigger_volumes:
        from cluster_portals import ClusterPortalMixin, get_cluster_portals

2.  Add ClusterPortalMixin to the App class:
        class App(tk.Tk, BspMixin, TriggerVolumeMixin, ClusterPortalMixin):
            ...
    (or mix it directly into BspMixin's bases, same as TriggerVolumeMixin)

3.  After _build_bsp_panel(parent), inject the checkbox onto the same row
    as the trigger volume toggle:
        self._cp_inject_controls(ctrl_frame)

4.  At the end of _bsp_load_file(), alongside _tv_on_map_loaded():
        self._cp_on_map_loaded(path)

5.  Inside the batch completion callback in _bsp_rebuild_geo(), alongside
    _tv_draw():
        self._cp_draw()

6.  In _bsp_on_section_change(), after self._bsp_geo is reassigned, call
    self._cp_draw() (or rely on _bsp_fit_view() -> _bsp_rebuild_geo() already
    calling it, if fit_view forces a rebuild).

Portals are per-sbsp-section (they describe boundaries between render
clusters within one BSP).  ClusterPortalMixin reads the live combobox
selection (_bsp_sect_combo.current()) at draw time, so switching sections
automatically shows that section's portals with no extra bookkeeping.
"""

import math
import struct
import tkinter as tk
from tkinter import ttk


# ── Data class ─────────────────────────────────────────────────────────────

class ClusterPortal:
    """One convex portal polygon between two render clusters."""
    __slots__ = (
        'back_cluster', 'front_cluster', 'plane_index',
        'centroid', 'radius', 'flags', 'verts',
    )

    def __init__(self, back_cluster, front_cluster, plane_index,
                 centroid, radius, flags, verts):
        self.back_cluster  = back_cluster    # int16, -1 = none/outside
        self.front_cluster = front_cluster   # int16
        self.plane_index   = plane_index     # int32, unresolved plane reference
        self.centroid      = centroid        # (x, y, z) world units
        self.radius        = radius          # float32 bounding radius
        self.flags         = flags           # raw flags32 bitmask
        self.verts         = verts           # list of (x, y, z), 3+ entries, planar

    # Flag bit meanings per Sbsp.txt's "Cluster Portals" flags32 definition.
    @property
    def ai_cannot_hear(self):
        return bool(self.flags & 0x01)

    @property
    def is_one_way(self):
        return bool(self.flags & 0x02)

    @property
    def is_door(self):
        return bool(self.flags & 0x04)

    @property
    def is_no_way(self):
        return bool(self.flags & 0x08)

    @property
    def is_one_way_reversed(self):
        return bool(self.flags & 0x10)

    @property
    def no_one_can_hear(self):
        return bool(self.flags & 0x20)


# ── Binary helpers ─────────────────────────────────────────────────────────

def _rf(d, o):
    return struct.unpack_from('<f', d, o)[0]

def _ri32(d, o):
    return struct.unpack_from('<I', d, o)[0]

def _ri32s(d, o):
    return struct.unpack_from('<i', d, o)[0]

def _ri16s(d, o):
    return struct.unpack_from('<h', d, o)[0]

def _read_4cc(d, o):
    return d[o:o+4][::-1].decode('ascii', errors='replace')

def _read_reflexive(d, o):
    """Read a (count, ptr) reflexive header. Returns (count, ptr) or None."""
    if o < 0 or o + 8 > len(d):
        return None
    return (_ri32(d, o), _ri32(d, o + 4))


# ── Canonical record layout (confirmed against Sbsp.txt) ───────────────────

_PORTAL_REFLEXIVE_OFF = 0x5C   # (count, ptr) of the standalone Cluster Portals block
_PORTAL_STRIDE         = 0x24  # 36 bytes per entry

_OFF_BACK_CLUSTER  = 0x00   # int16
_OFF_FRONT_CLUSTER = 0x02   # int16
_OFF_PLANE_INDEX   = 0x04   # int32
_OFF_CENTROID      = 0x08   # point3
_OFF_RADIUS        = 0x14   # float32
_OFF_FLAGS         = 0x18   # flags32
_OFF_VERTS_REFLEX  = 0x1C   # (count, ptr) -> point3 array

_VERT_STRIDE = 0x0C   # 12 bytes, XYZ only

_MAX_PORTALS_SANE      = 8192   # defensive cap against corrupted reflexives
_MAX_PORTAL_VERTS_SANE = 64


# ── Per-section parser ───────────────────────────────────────────────────────

def _parse_sbsp_portals(bsp_meta: bytes, sbsp_voff: int) -> list[ClusterPortal]:
    """Extract cluster portal polygons from one sbsp meta block by reading
    the standalone Cluster Portals reflexive and each entry's own nested
    vertex reflexive directly (confirmed structure, no heuristics needed)."""
    try:
        header = _read_reflexive(bsp_meta, _PORTAL_REFLEXIVE_OFF)
        if header is None:
            return []
        count, ptr = header
        if count <= 0 or count > _MAX_PORTALS_SANE:
            return []

        rel = ptr - sbsp_voff
        if not (0 <= rel < len(bsp_meta)):
            return []
        if rel + count * _PORTAL_STRIDE > len(bsp_meta):
            return []

        portals = []
        for pi in range(count):
            off = rel + pi * _PORTAL_STRIDE

            back_cluster  = _ri16s(bsp_meta, off + _OFF_BACK_CLUSTER)
            front_cluster = _ri16s(bsp_meta, off + _OFF_FRONT_CLUSTER)
            plane_index   = _ri32s(bsp_meta, off + _OFF_PLANE_INDEX)
            centroid = (
                _rf(bsp_meta, off + _OFF_CENTROID + 0),
                _rf(bsp_meta, off + _OFF_CENTROID + 4),
                _rf(bsp_meta, off + _OFF_CENTROID + 8),
            )
            radius = _rf(bsp_meta, off + _OFF_RADIUS)
            flags  = _ri32(bsp_meta, off + _OFF_FLAGS)

            vheader = _read_reflexive(bsp_meta, off + _OFF_VERTS_REFLEX)
            if vheader is None:
                continue
            vcount, vptr = vheader
            if vcount < 3 or vcount > _MAX_PORTAL_VERTS_SANE:
                continue

            vrel = vptr - sbsp_voff
            if not (0 <= vrel < len(bsp_meta)):
                continue
            if vrel + vcount * _VERT_STRIDE > len(bsp_meta):
                continue

            verts = []
            valid = True
            for vi in range(vcount):
                vo = vrel + vi * _VERT_STRIDE
                x = _rf(bsp_meta, vo + 0)
                y = _rf(bsp_meta, vo + 4)
                z = _rf(bsp_meta, vo + 8)
                if not (math.isfinite(x) and math.isfinite(y) and math.isfinite(z)
                        and abs(x) < 1000 and abs(y) < 1000 and abs(z) < 500):
                    valid = False
                    break
                verts.append((x, y, z))

            if valid:
                portals.append(ClusterPortal(
                    back_cluster=back_cluster, front_cluster=front_cluster,
                    plane_index=plane_index, centroid=centroid,
                    radius=radius, flags=flags, verts=verts,
                ))

        return portals

    except Exception:
        return []


# ── Public parser ──────────────────────────────────────────────────────────

def parse_cluster_portals(map_path: str) -> list[list[ClusterPortal]]:
    """
    Parse cluster portals from every sbsp section of a Halo 2 Xbox .map file.
    Returns a list of per-section portal lists, in the same order as
    get_bsp_sections() / parse_all_bsp_sections() in ui_bsp.py, so index i
    here corresponds to section i in the BSP viewer's combobox.
    """
    try:
        with open(map_path, 'rb') as f:
            hdr = f.read(0x800)

        if _ri32(hdr, 0x004) != 8:
            return []

        tag_file_off = _ri32(hdr, 0x010)
        tag_length   = _ri32(hdr, 0x014)

        with open(map_path, 'rb') as f:
            f.seek(tag_file_off)
            tag_section = f.read(tag_length)

        tag_entries_offset = _ri32(tag_section, 0x08)
        tag_count          = _ri32(tag_section, 0x18)

        sbsp_entries = []
        for i in range(tag_count):
            off = tag_entries_offset + i * 16
            if _read_4cc(tag_section, off) == 'sbsp':
                voff = _ri32(tag_section, off + 8)
                size = _ri32(tag_section, off + 12)
                sbsp_entries.append((voff, size))

        results = []
        for voff, size in sbsp_entries:
            if size <= 0:
                results.append([])
                continue
            with open(map_path, 'rb') as f:
                f.seek(tag_file_off + voff)
                bsp_meta = f.read(size)
            results.append(_parse_sbsp_portals(bsp_meta, voff))

        return results

    except Exception as e:
        print(f'Cluster portal parse error: {e}')
        return []


# ── Cache ──────────────────────────────────────────────────────────────────

_cp_cache: dict[str, list[list[ClusterPortal]]] = {}

def get_cluster_portals(map_path: str) -> list[list[ClusterPortal]]:
    """Cached wrapper around parse_cluster_portals()."""
    if map_path not in _cp_cache:
        _cp_cache[map_path] = parse_cluster_portals(map_path)
    return _cp_cache.get(map_path, [])


# ── Mixin ──────────────────────────────────────────────────────────────────

class ClusterPortalMixin:
    """
    Renders cluster portal polygons on the BSP canvas.

    Requires BspMixin in the same class (for canvas/projection helpers and
    the section combobox).  See module docstring for the integration call
    sites (_cp_inject_controls, _cp_on_map_loaded, _cp_draw).
    """

    _CP_COLOUR      = '#33ccff'   # portal edge colour
    _CP_FILL        = '#1a4d66'   # faint fill so polygons read as panes, not wire loops
    _CP_FILL_STIPPLE = 'gray25'

    # ── Setup ──────────────────────────────────────────────────────────────

    def _cp_inject_controls(self, ctrl_frame):
        """
        Add a 'Cluster Portals' toggle checkbox to an existing control bar
        Frame.  Call this once, alongside _tv_inject_controls().
        """
        self._cp_show = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            ctrl_frame, text='Portals',
            variable=self._cp_show,
            command=self._cp_toggle,
        ).pack(side=tk.LEFT, padx=(8, 0))
        self._cp_lbl = ttk.Label(ctrl_frame, text='',
                                  foreground='#33ccff',
                                  font=('Consolas', 8))
        self._cp_lbl.pack(side=tk.LEFT, padx=(4, 0))

    def _cp_on_map_loaded(self, map_path: str):
        """
        Load (and cache) cluster portals for map_path.  Call this after
        get_bsp_sections() succeeds inside _bsp_load_file(), alongside
        _tv_on_map_loaded().
        """
        self._cp_sections = get_cluster_portals(map_path)
        self._cp_update_label()

    def _cp_update_label(self):
        if not hasattr(self, '_cp_lbl'):
            return
        portals = self._cp_current_section_portals()
        n = len(portals)
        self._cp_lbl.config(text=f'{n} portals' if n else 'no portals')

    def _cp_current_section_portals(self):
        sections = getattr(self, '_cp_sections', [])
        if not sections:
            return []
        try:
            idx = self._bsp_sect_combo.current()
        except Exception:
            idx = 0
        if idx < 0 or idx >= len(sections):
            idx = 0
        return sections[idx]

    # ── Toggle ─────────────────────────────────────────────────────────────

    def _cp_toggle(self):
        if self._cp_show.get():
            self._cp_draw()
        else:
            self._bsp_canvas.delete('cp')

    # ── Draw ───────────────────────────────────────────────────────────────

    def _cp_draw(self):
        """
        Draw the current section's cluster portals as filled, outlined
        polygons.  Items are tagged both 'geo' and 'cp':
          - 'geo' makes them participate in pan/zoom alongside BSP geometry
          - 'cp'  lets _cp_toggle() delete only portal items
        Call this at the end of the batch_edges completion callback in
        _bsp_rebuild_geo(), alongside _tv_draw().
        """
        c = self._bsp_canvas
        c.delete('cp')
        self._cp_update_label()

        if not getattr(self, '_cp_show', tk.BooleanVar(value=False)).get():
            return

        portals = self._cp_current_section_portals()
        if not portals:
            return

        view  = self._bsp_view.get()
        angle = self._bsp_angle
        ca    = math.cos(math.radians(angle))
        sa    = math.sin(math.radians(angle))

        z_filter = self._bsp_z_filter.get()
        try:
            zmin_f = self._bsp_zmin_var.get()
            zmax_f = self._bsp_zmax_var.get()
        except Exception:
            z_filter = False
            zmin_f = zmax_f = 0.0

        for portal in portals:
            if z_filter:
                zs = [v[2] for v in portal.verts]
                if max(zs) < zmin_f or min(zs) > zmax_f:
                    continue

            pts = []
            for (wx, wy, wz) in portal.verts:
                h, v = self._proj_hv(wx, wy, wz, view, ca, sa)
                pts.append(self._hv_to_canvas(h, v))

            flat = [coord for xy in pts for coord in xy]

            # Faint fill so the portal reads as a translucent pane
            c.create_polygon(
                *flat,
                fill=self._CP_FILL, outline='',
                stipple=self._CP_FILL_STIPPLE,
                tags=('geo', 'cp'),
            )
            # Solid outline on top
            c.create_polygon(
                *flat,
                fill='', outline=self._CP_COLOUR, width=1,
                tags=('geo', 'cp'),
            )
