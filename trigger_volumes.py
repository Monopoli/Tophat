"""
trigger_volumes.py — Halo 2 Xbox trigger volume parser and renderer.

Drop-in companion to ui_bsp.py.  Provides:
  - parse_trigger_volumes(map_path) → list[TriggerVolume]
  - get_trigger_volumes(map_path)   → cached version
  - TriggerVolumeMixin              (mix into the same class as BspMixin)

Confirmed structure (cross-checked against scnrstructure.txt, the Halo 2
"scnr" tag plugin layout):

  The block is officially named **Kill Trigger Volumes**, a reflexive
  (count, ptr) at scnr meta +0x108, stride 0x44 (68) bytes/entry:

    +0x00  name_id              stringid  raw, unresolved (see note below)
    +0x04  object_name_index    int16
    +0x06  node_index           int16
    +0x08  node_name_id         stringid  raw, unresolved
    +0x0C  forward              vector3   unit vector, local OBB X axis
    +0x18  up                   vector3   unit vector, local OBB Z axis
    +0x24  position             point3    centre of volume, world units
    +0x30  extents              point3    half-extents along forward/right/up
    +0x3C  unknown              float32
    +0x40  kill_trigger_volume_index  int16  sub-index, NOT the array position
    +0x42  unknown              int16

  The reflexive pointer is translated to a relative offset within the scnr
  meta the same way cluster_portals.py does it for sbsp reflexives:
  rel = ptr - voff (voff being the tag's own file-relative offset).

  StringID note: name_id / node_name_id are raw 32-bit StringID values, not
  inline text. Resolving them to readable names requires the cache's
  separate global string-ID table, which nothing in this codebase parses
  yet — they're exposed here as-is for future use (e.g. once that table is
  decoded, or for manual cross-referencing by raw value).

  History: before scnrstructure.txt was available, this module found the
  array by brute-force byte-scanning the whole scnr meta for the longest
  run of 68-byte windows whose floats looked like a forward/up vector pair
  plus a map-scale position/extent pair. That scan's windows landed
  exactly 12 bytes into each true record — it skipped over the
  name_id/object_name_index/node_index/node_name_id header because those
  bytes don't look like floats, and locked onto the vector data instead.
  Because the 12-byte shift and the 68-byte stride are both constant, the
  per-index forward/up/position/extents the old code read were still
  correctly aligned to the right record — the rendered OBBs were never
  wrong — but the name field was invisible and the trailing "20 unused
  bytes" were actually a mix of the current record's tail and the next
  record's header. The blind scan is kept below as a fallback in case the
  reflexive at +0x108 ever doesn't validate (e.g. a different build).

Integration
-----------
1.  Import at the top of your main module:
        from trigger_volumes import TriggerVolumeMixin, get_trigger_volumes

2.  Add TriggerVolumeMixin to your App class alongside BspMixin:
        class App(tk.Tk, BspMixin, TriggerVolumeMixin):
            ...

3.  After _build_bsp_panel(parent) in __init__ / build, inject the checkbox:
        self._tv_inject_controls(ctrl_frame)   # ctrl_frame = the control bar Frame

4.  At the end of _bsp_load_file(), after getting BSP sections:
        self._tv_on_map_loaded(path)

5.  Inside _bsp_rebuild_geo()'s batch completion callback, after drawing BSP edges:
        self._tv_draw()

That's it.  Pan/zoom work for free because OBB edges share the 'geo' tag.
"""

import math
import struct
import tkinter as tk
from tkinter import ttk


# ── Data class ─────────────────────────────────────────────────────────────

class TriggerVolume:
    """One oriented bounding box read from the scenario tag."""
    __slots__ = (
        'forward', 'up', 'right', 'position', 'extents', 'index',
        'name_id', 'node_name_id', 'object_name_index', 'node_index',
        'kill_trigger_volume_index',
    )

    def __init__(self, index, forward, up, position, extents,
                 name_id=0, node_name_id=0,
                 object_name_index=-1, node_index=-1,
                 kill_trigger_volume_index=-1):
        self.index    = index
        self.forward  = forward   # (fx, fy, fz)  unit vector
        self.up       = up        # (ux, uy, uz)  unit vector
        # right = up × forward
        fx, fy, fz = forward
        ux, uy, uz = up
        self.right = (
            uy * fz - uz * fy,
            uz * fx - ux * fz,
            ux * fy - uy * fx,
        )
        self.position = position  # (px, py, pz)  world centre
        self.extents  = extents   # (ex, ey, ez)  half-extents along f/right/up

        # Metadata from the canonical Kill Trigger Volumes record. name_id /
        # node_name_id are raw StringID values (see module docstring) — not
        # human-readable text yet.
        self.name_id                   = name_id
        self.node_name_id              = node_name_id
        self.object_name_index         = object_name_index
        self.node_index                = node_index
        self.kill_trigger_volume_index = kill_trigger_volume_index

    def corners(self):
        """Return the 8 world-space corner positions of the OBB."""
        px, py, pz = self.position
        fx, fy, fz = self.forward
        rx, ry, rz = self.right
        ux, uy, uz = self.up
        ex, ey, ez = self.extents
        corners = []
        for sf in (-1, 1):
            for sr in (-1, 1):
                for su in (-1, 1):
                    corners.append((
                        px + sf*ex*fx + sr*ey*rx + su*ez*ux,
                        py + sf*ex*fy + sr*ey*ry + su*ez*uy,
                        pz + sf*ex*fz + sr*ey*rz + su*ez*uz,
                    ))
        return corners  # 8 corners, indices 0–7

    # 12 edges of the OBB (index pairs into corners())
    EDGES = [
        # bottom face  (su = -1): corners 0,1,2,3
        (0, 1), (0, 2), (1, 3), (2, 3),
        # top face     (su = +1): corners 4,5,6,7
        (4, 5), (4, 6), (5, 7), (6, 7),
        # vertical pillars
        (0, 4), (1, 5), (2, 6), (3, 7),
    ]


# ── Binary helpers ─────────────────────────────────────────────────────────

def _rf(d, o):
    return struct.unpack_from('<f', d, o)[0]

def _ri32(d, o):
    return struct.unpack_from('<I', d, o)[0]

def _ri16s(d, o):
    return struct.unpack_from('<h', d, o)[0]

def _read_4cc(d, o):
    return d[o:o+4][::-1].decode('ascii', errors='replace')


# ── Canonical record layout (confirmed against scnrstructure.txt) ──────────

_TV_REFLEXIVE_OFF = 0x108   # offset of the Kill Trigger Volumes reflexive in scnr meta
_TV_STRIDE         = 68     # 0x44 bytes per entry

_OFF_NAME       = 0x00   # stringid, raw/unresolved
_OFF_OBJ_NAME_IX = 0x04  # int16
_OFF_NODE_IX    = 0x06   # int16
_OFF_NODE_NAME  = 0x08   # stringid, raw/unresolved
_OFF_FORWARD    = 0x0C   # vector3
_OFF_UP         = 0x18   # vector3
_OFF_POSITION   = 0x24   # point3
_OFF_EXTENTS    = 0x30   # point3
_OFF_KTV_INDEX  = 0x40   # int16, distinct from this entry's array position


def _entry_geometry_is_sane(fw, up, pos, ext):
    """Sanity check shared by the reflexive path and the fallback scan."""
    fx, fy, fz = fw
    ux, uy, uz = up
    px, py, pz = pos
    ex, ey, ez = ext
    if not all(math.isfinite(v) for v in (fx, fy, fz, ux, uy, uz, px, py, pz, ex, ey, ez)):
        return False
    fw_mag = fx*fx + fy*fy + fz*fz
    up_mag = ux*ux + uy*uy + uz*uz
    return (
        0.85 < fw_mag < 1.15 and
        0.85 < up_mag < 1.15 and
        abs(px) < 500 and abs(py) < 500 and abs(pz) < 300 and
        0.01 < ex < 1000 and 0.01 < ey < 1000 and 0.01 < ez < 1000
    )


def _read_tv_entry(scnr_meta: bytes, off: int) -> dict | None:
    """Read one full Kill Trigger Volumes record at its true start offset."""
    if off < 0 or off + _TV_STRIDE > len(scnr_meta):
        return None
    try:
        name_id      = _ri32(scnr_meta, off + _OFF_NAME)
        obj_name_ix  = _ri16s(scnr_meta, off + _OFF_OBJ_NAME_IX)
        node_ix      = _ri16s(scnr_meta, off + _OFF_NODE_IX)
        node_name_id = _ri32(scnr_meta, off + _OFF_NODE_NAME)
        fw  = (_rf(scnr_meta, off + _OFF_FORWARD + 0), _rf(scnr_meta, off + _OFF_FORWARD + 4), _rf(scnr_meta, off + _OFF_FORWARD + 8))
        up  = (_rf(scnr_meta, off + _OFF_UP + 0),      _rf(scnr_meta, off + _OFF_UP + 4),      _rf(scnr_meta, off + _OFF_UP + 8))
        pos = (_rf(scnr_meta, off + _OFF_POSITION + 0), _rf(scnr_meta, off + _OFF_POSITION + 4), _rf(scnr_meta, off + _OFF_POSITION + 8))
        ext = (_rf(scnr_meta, off + _OFF_EXTENTS + 0),  _rf(scnr_meta, off + _OFF_EXTENTS + 4),  _rf(scnr_meta, off + _OFF_EXTENTS + 8))
        ktv_index = _ri16s(scnr_meta, off + _OFF_KTV_INDEX)
    except struct.error:
        return None
    return {
        'name_id': name_id, 'node_name_id': node_name_id,
        'object_name_index': obj_name_ix, 'node_index': node_ix,
        'forward': fw, 'up': up, 'position': pos, 'extents': ext,
        'kill_trigger_volume_index': ktv_index,
    }


def _read_tv_reflexive(scnr_meta: bytes, scnr_voff: int) -> tuple[int, int] | None:
    """
    Read the (count, ptr) reflexive header at the fixed scnr offset and
    translate ptr into an offset relative to scnr_meta, using the same
    (ptr - voff) convention already validated for sbsp reflexives in
    cluster_portals.py. Returns (start_offset, count) or None.
    """
    if len(scnr_meta) < _TV_REFLEXIVE_OFF + 8:
        return None
    count = _ri32(scnr_meta, _TV_REFLEXIVE_OFF)
    if count == 0:
        return (0, 0)
    if count < 0 or count > 4096:
        return None
    ptr = _ri32(scnr_meta, _TV_REFLEXIVE_OFF + 4)
    rel = ptr - scnr_voff
    if not (0 <= rel < len(scnr_meta)):
        return None
    if rel + count * _TV_STRIDE > len(scnr_meta):
        return None
    return (rel, count)


# ── Fallback: legacy blind scan (pre-scnrstructure.txt) ─────────────────────

def _is_valid_tv_window(window: bytes) -> bool:
    """True if a 68-byte window's bytes-at-old-offsets look like a TV entry."""
    if len(window) < _TV_STRIDE:
        return False
    try:
        fw  = (_rf(window, 0),  _rf(window, 4),  _rf(window, 8))
        up  = (_rf(window, 12), _rf(window, 16), _rf(window, 20))
        pos = (_rf(window, 24), _rf(window, 28), _rf(window, 32))
        ext = (_rf(window, 36), _rf(window, 40), _rf(window, 44))
    except struct.error:
        return False
    return _entry_geometry_is_sane(fw, up, pos, ext)


def _find_tv_array_fallback(scnr_meta: bytes) -> tuple[int, int] | None:
    """
    Scan scnr meta for the longest contiguous run of windows whose
    forward/up/position/extents floats look sane at the *old* (pre-header)
    relative offsets, then shift back by 0x0C to land on each record's true
    start (the name_id field), so the caller can read full entries —
    including the name — via _read_tv_entry(). Returns (start_offset, count)
    or None.
    """
    best_start = None
    best_count = 0
    i = 0
    n = len(scnr_meta)
    while i < n - _TV_STRIDE:
        if _is_valid_tv_window(scnr_meta[i:i + _TV_STRIDE]):
            run_start = i
            run_count = 1
            j = i + _TV_STRIDE
            while j + _TV_STRIDE <= n:
                if _is_valid_tv_window(scnr_meta[j:j + _TV_STRIDE]):
                    run_count += 1
                    j += _TV_STRIDE
                else:
                    break
            if run_count > best_count:
                best_count = run_count
                best_start = run_start
            i = j
        else:
            i += 4  # walk by alignment unit
    if best_start is None:
        return None
    true_start = best_start - 0x0C
    if true_start < 0:
        return None
    return (true_start, best_count)


# ── Public parser ──────────────────────────────────────────────────────────

def parse_trigger_volumes(map_path: str) -> list[TriggerVolume]:
    """
    Parse all trigger volumes from a Halo 2 Xbox .map file.
    Returns a (possibly empty) list of TriggerVolume objects.
    """
    try:
        with open(map_path, 'rb') as f:
            hdr = f.read(0x800)

        # Validate Halo 2 Xbox map header (version 8)
        if _ri32(hdr, 0x004) != 8:
            return []

        tag_file_off = _ri32(hdr, 0x010)
        tag_length   = _ri32(hdr, 0x014)

        with open(map_path, 'rb') as f:
            f.seek(tag_file_off)
            tag_section = f.read(tag_length)

        tag_entries_offset = _ri32(tag_section, 0x08)
        tag_count          = _ri32(tag_section, 0x18)

        # Find the scenario (scnr) tag entry
        scnr_voff = None
        scnr_size = None
        for i in range(tag_count):
            off = tag_entries_offset + i * 16
            if _read_4cc(tag_section, off) == 'scnr':
                scnr_voff = _ri32(tag_section, off + 8)
                scnr_size = _ri32(tag_section, off + 12)
                break

        if scnr_voff is None:
            return []

        # Read scnr meta directly from the map file.
        # voff is an offset from tag_file_off (same pattern as sbsp in ui_bsp.py).
        with open(map_path, 'rb') as f:
            f.seek(tag_file_off + scnr_voff)
            scnr_meta = f.read(scnr_size)

        # Primary path: read the Kill Trigger Volumes reflexive directly.
        start_off = None
        count = None
        ref = _read_tv_reflexive(scnr_meta, scnr_voff)
        if ref is not None:
            rel, c = ref
            if c == 0:
                return []
            first = _read_tv_entry(scnr_meta, rel)
            if first is not None and _entry_geometry_is_sane(
                first['forward'], first['up'], first['position'], first['extents']
            ):
                start_off, count = rel, c

        # Fallback: legacy blind scan, shifted onto the true record start.
        if start_off is None:
            fallback = _find_tv_array_fallback(scnr_meta)
            if fallback is None:
                return []
            start_off, count = fallback

        volumes = []
        for idx in range(count):
            off = start_off + idx * _TV_STRIDE
            entry = _read_tv_entry(scnr_meta, off)
            if entry is None:
                break
            volumes.append(TriggerVolume(
                index=idx,
                forward=entry['forward'], up=entry['up'],
                position=entry['position'], extents=entry['extents'],
                name_id=entry['name_id'], node_name_id=entry['node_name_id'],
                object_name_index=entry['object_name_index'],
                node_index=entry['node_index'],
                kill_trigger_volume_index=entry['kill_trigger_volume_index'],
            ))

        return volumes

    except Exception as e:
        print(f'Trigger volume parse error: {e}')
        return []


# ── Cache ──────────────────────────────────────────────────────────────────

_tv_cache: dict[str, list[TriggerVolume]] = {}

def get_trigger_volumes(map_path: str) -> list[TriggerVolume]:
    """Cached wrapper around parse_trigger_volumes()."""
    if map_path not in _tv_cache:
        _tv_cache[map_path] = parse_trigger_volumes(map_path)
    return _tv_cache.get(map_path, [])


# ── Mixin ──────────────────────────────────────────────────────────────────

class TriggerVolumeMixin:
    """
    Renders trigger volume OBBs on the BSP canvas.

    Requires BspMixin in the same class.  See module docstring for the
    three integration call sites (_tv_inject_controls, _tv_on_map_loaded,
    _tv_draw).
    """

    _TV_COLOUR        = '#ff6600'   # OBB edge colour
    _TV_CENTRE_COLOUR = '#ffaa44'   # centre cross colour

    # ── Setup ──────────────────────────────────────────────────────────────

    def _tv_inject_controls(self, ctrl_frame):
        """
        Add a 'Trigger Vols' toggle checkbox to an existing control bar Frame.
        Call this once, right after _build_bsp_panel().
        """
        self._tv_show = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            ctrl_frame, text='Triggers',
            variable=self._tv_show,
            command=self._tv_toggle,
        ).pack(side=tk.LEFT, padx=(8, 0))
        self._tv_lbl = ttk.Label(ctrl_frame, text='',
                                  foreground='#ff6600',
                                  font=('Consolas', 8))
        self._tv_lbl.pack(side=tk.LEFT, padx=(4, 0))

    def _tv_on_map_loaded(self, map_path: str):
        """
        Load (and cache) trigger volumes for map_path.  Call this after
        get_bsp_sections() succeeds inside _bsp_load_file().
        """
        self._tv_volumes = get_trigger_volumes(map_path)
        if hasattr(self, '_tv_lbl'):
            n = len(self._tv_volumes)
            self._tv_lbl.config(text=f'{n} volumes' if n else 'no volumes')

    # ── Toggle ─────────────────────────────────────────────────────────────

    def _tv_toggle(self):
        if self._tv_show.get():
            self._tv_draw()
        else:
            self._bsp_canvas.delete('tv')

    # ── Draw ───────────────────────────────────────────────────────────────

    def _tv_draw(self):
        """
        Draw all trigger volume OBBs as dashed wireframe boxes.
        Items are tagged both 'geo' and 'tv':
          - 'geo' makes them participate in c.move() / c.scale() pan/zoom
          - 'tv'  lets _tv_toggle() delete only TV items without clearing BSP geo
        Call this at the end of the batch_edges completion callback in
        _bsp_rebuild_geo().
        """
        c = self._bsp_canvas
        c.delete('tv')

        if not getattr(self, '_tv_show', tk.BooleanVar(value=False)).get():
            return

        vols = getattr(self, '_tv_volumes', [])
        if not vols:
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

        for vol in vols:
            # Z-filter: skip volumes whose extent doesn't overlap the Z band
            if z_filter:
                vz = vol.position[2]
                ve = vol.extents[2]
                if vz + ve < zmin_f or vz - ve > zmax_f:
                    continue

            corners = vol.corners()

            # Project each of the 8 OBB corners to canvas space
            proj = []
            for (wx, wy, wz) in corners:
                h, v = self._proj_hv(wx, wy, wz, view, ca, sa)
                proj.append(self._hv_to_canvas(h, v))

            # Draw the 12 edges
            for (i0, i1) in TriggerVolume.EDGES:
                x0, y0 = proj[i0]
                x1, y1 = proj[i1]
                c.create_line(x0, y0, x1, y1,
                              fill=self._TV_COLOUR, width=1,
                              dash=(4, 3),
                              tags=('geo', 'tv'))

            # Small cross at the volume centre
            h, v = self._proj_hv(
                vol.position[0], vol.position[1], vol.position[2],
                view, ca, sa)
            cx, cy = self._hv_to_canvas(h, v)
            r = 4
            c.create_line(cx - r, cy,     cx + r, cy,
                          fill=self._TV_CENTRE_COLOUR, width=1, tags=('geo', 'tv'))
            c.create_line(cx,     cy - r, cx,     cy + r,
                          fill=self._TV_CENTRE_COLOUR, width=1, tags=('geo', 'tv'))
