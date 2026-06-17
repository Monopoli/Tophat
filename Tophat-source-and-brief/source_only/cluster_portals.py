"""
cluster_portals.py — Halo 2 Xbox render-cluster portal parser and renderer.

Drop-in companion to ui_bsp.py and trigger_volumes.py.  Provides:
  - parse_cluster_portals(map_path) -> list[list[ClusterPortal]]   (one list per sbsp section)
  - get_cluster_portals(map_path)   -> cached version
  - ClusterPortalMixin              (mix into the same class as BspMixin)

Discovered structure (01b_spacestation, per-sbsp-section sbsp meta block):
  Each sbsp meta has a CLUSTERS reflexive at meta+0x09c (count, ptr).  Cluster
  entries are NOT fixed stride end-to-end (they carry inline sub-reflexive
  data for subclusters elsewhere in the block), but the first 80 bytes of
  every cluster entry are a stable fixed-size header, which is sufficient to
  read the portal vertex range:

    cluster_header (first 80 bytes of each cluster entry, stride 80):
      +36  first_portal_vertex  u16   index into the portal vertex pool
      +38  portal_vertex_count  u16   number of vertices for this cluster's portal

  Portal vertex pool, a second reflexive at meta+0x0f4 (count, ptr), stride 16:
      +0   x  f32
      +4   y  f32
      +8   z  f32
      +12  w  f32   (unknown / lightmap-related, unused for rendering)

  Not every cluster has a valid portal: many report count=0, or — because the
  +36/+38 fields can alias into another cluster's inline sub-reflexive data —
  implausibly large counts.  We therefore validate each candidate against:
    - 3 <= count <= 8           (real portals here are triangles/quads)
    - vertex range inside the portal vertex pool
    - all positions finite and map-scale (|coord| < 400)
    - coplanarity within a small tolerance (cross-section contamination
      reliably produces non-planar point sets)
    - non-degenerate spatial extent

  This recovers 31 valid portal polygons across the 6 sbsp sections of
  01b_spacestation (sizes: 19 triangles, 12 quads).  It is a conservative
  filter — it undercounts true portals rather than rendering garbage.

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
    __slots__ = ('cluster_index', 'verts')

    def __init__(self, cluster_index, verts):
        self.cluster_index = cluster_index   # owning cluster, for reference/debug
        self.verts         = verts           # list of (x, y, z), 3-8 entries, planar


# ── Binary helpers ─────────────────────────────────────────────────────────

def _rf(d, o):
    return struct.unpack_from('<f', d, o)[0]

def _ri32(d, o):
    return struct.unpack_from('<I', d, o)[0]

def _ri16(d, o):
    return struct.unpack_from('<H', d, o)[0]

def _read_4cc(d, o):
    return d[o:o+4][::-1].decode('ascii', errors='replace')


# ── Geometry validation ─────────────────────────────────────────────────────

_CLUSTER_HEADER_STRIDE = 80   # bytes; stable prefix of each cluster entry
_PORTAL_VERT_STRIDE    = 16   # bytes per portal vertex pool entry
_MIN_PORTAL_VERTS      = 3
_MAX_PORTAL_VERTS      = 8    # real portals here are tris/quads; bigger = contamination
_COPLANAR_TOL          = 2.0  # world units


def _is_planar(verts, tol=_COPLANAR_TOL):
    """Check whether a point set lies within tol of the plane through verts[0:3]."""
    if len(verts) < 3:
        return False
    p0, p1, p2 = verts[0], verts[1], verts[2]
    ax, ay, az = p1[0]-p0[0], p1[1]-p0[1], p1[2]-p0[2]
    bx, by, bz = p2[0]-p0[0], p2[1]-p0[1], p2[2]-p0[2]
    nx = ay*bz - az*by
    ny = az*bx - ax*bz
    nz = ax*by - ay*bx
    mag = math.sqrt(nx*nx + ny*ny + nz*nz)
    if mag < 1e-3:
        return False
    nx, ny, nz = nx/mag, ny/mag, nz/mag
    d = nx*p0[0] + ny*p0[1] + nz*p0[2]
    for v in verts[3:]:
        if abs(nx*v[0] + ny*v[1] + nz*v[2] - d) > tol:
            return False
    return True


def _has_extent(verts, min_span=0.5):
    """Reject degenerate (near-zero-area) point sets."""
    xs = [v[0] for v in verts]
    ys = [v[1] for v in verts]
    zs = [v[2] for v in verts]
    span = (max(xs)-min(xs)) + (max(ys)-min(ys)) + (max(zs)-min(zs))
    return span > min_span


# ── Per-section parser ───────────────────────────────────────────────────────

def _parse_sbsp_portals(bsp_meta: bytes, sbsp_voff: int) -> list[ClusterPortal]:
    """Extract valid cluster portal polygons from one sbsp meta block."""
    try:
        cluster_count = _ri32(bsp_meta, 0x09c)
        cluster_ptr   = _ri32(bsp_meta, 0x0a0)
        cluster_rel   = cluster_ptr - sbsp_voff

        pverts_count  = _ri32(bsp_meta, 0x0f4)
        pverts_ptr    = _ri32(bsp_meta, 0x0f8)
        pverts_rel    = pverts_ptr - sbsp_voff

        if not (0 < cluster_rel < len(bsp_meta) and 0 < pverts_rel < len(bsp_meta)):
            return []
        if cluster_count <= 0 or pverts_count <= 0:
            return []

        portals = []
        for ci in range(cluster_count):
            c_off = cluster_rel + ci * _CLUSTER_HEADER_STRIDE
            if c_off + 40 > len(bsp_meta):
                break

            first = _ri16(bsp_meta, c_off + 36)
            count = _ri16(bsp_meta, c_off + 38)

            if not (_MIN_PORTAL_VERTS <= count <= _MAX_PORTAL_VERTS):
                continue
            if first >= pverts_count or first + count > pverts_count:
                continue

            verts = []
            valid = True
            for vi in range(count):
                vo = pverts_rel + (first + vi) * _PORTAL_VERT_STRIDE
                if vo + 12 > len(bsp_meta):
                    valid = False
                    break
                x = _rf(bsp_meta, vo)
                y = _rf(bsp_meta, vo + 4)
                z = _rf(bsp_meta, vo + 8)
                if not (math.isfinite(x) and math.isfinite(y) and math.isfinite(z)
                        and abs(x) < 400 and abs(y) < 400 and abs(z) < 200):
                    valid = False
                    break
                verts.append((x, y, z))

            if valid and _is_planar(verts) and _has_extent(verts):
                portals.append(ClusterPortal(ci, verts))

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
