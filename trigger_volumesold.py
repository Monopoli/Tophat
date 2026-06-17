"""
trigger_volumes.py — Halo 2 Xbox trigger volume parser and renderer.

Drop-in companion to ui_bsp.py.  Provides:
  - parse_trigger_volumes(map_path) → list[TriggerVolume]
  - get_trigger_volumes(map_path)   → cached version
  - TriggerVolumeMixin              (mix into the same class as BspMixin)

Discovered structure (01b_spacestation, tag section at file offset 0xb525000):
  scnr tag entry in the tag array (16 bytes each):
    +0  class tag  'scnr' (4-char reversed)
    +8  voff       offset of scnr meta from tag_file_off  (i.e. seek to tag_file_off+voff)
    +12 size       byte length of scnr meta

  Note: voff is NOT an index into the in-memory tag_section window; it is a file
  offset added to tag_file_off, exactly as the BSP viewer does for sbsp tags.

  Trigger volume array within scnr meta:
    Located by scanning for the longest contiguous run of valid entries.
    Stride: 68 bytes per entry (no name field in this game build).

  Per-entry layout (68 bytes):
    +0   forward_x  f32  ─┐ unit forward vector (local OBB X axis)
    +4   forward_y  f32   │
    +8   forward_z  f32  ─┘  (≈0 for floor-level volumes)
    +12  up_x       f32  ─┐ unit up vector (local OBB Z axis)
    +16  up_y       f32   │
    +20  up_z       f32  ─┘  (≈1 for most volumes — world up)
    +24  position_x f32  ─┐ centre of volume in world units
    +28  position_y f32   │
    +32  position_z f32  ─┘
    +36  extent_x   f32  ─┐ half-extents along forward / right / up
    +40  extent_y   f32   │
    +44  extent_z   f32  ─┘
    +48  [20 bytes of indices/flags — not used for rendering]

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
    __slots__ = ('forward', 'up', 'right', 'position', 'extents', 'index')

    def __init__(self, index, forward, up, position, extents):
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

def _read_4cc(d, o):
    return d[o:o+4][::-1].decode('ascii', errors='replace')


# ── TV array detection ─────────────────────────────────────────────────────

_TV_STRIDE = 68   # bytes per trigger volume entry

def _is_valid_tv_entry(entry: bytes) -> bool:
    """Return True if 68 bytes look like a plausible trigger volume entry."""
    if len(entry) < _TV_STRIDE:
        return False
    try:
        fx = _rf(entry,  0);  fy = _rf(entry,  4);  fz = _rf(entry,  8)
        ux = _rf(entry, 12);  uy = _rf(entry, 16);  uz = _rf(entry, 20)
        px = _rf(entry, 24);  py = _rf(entry, 28);  pz = _rf(entry, 32)
        ex = _rf(entry, 36);  ey = _rf(entry, 40);  ez = _rf(entry, 44)
    except struct.error:
        return False
    if not all(math.isfinite(v) for v in (fx,fy,fz,ux,uy,uz,px,py,pz,ex,ey,ez)):
        return False
    fw_mag = fx*fx + fy*fy + fz*fz
    up_mag = ux*ux + uy*uy + uz*uz
    return (
        0.85 < fw_mag < 1.15 and
        0.85 < up_mag < 1.15 and
        abs(px) < 500 and abs(py) < 500 and abs(pz) < 300 and
        0.01 < ex < 1000 and 0.01 < ey < 1000 and 0.01 < ez < 1000
    )


def _find_tv_array(scnr: bytes) -> tuple[int, int] | None:
    """
    Scan scnr meta for the longest contiguous run of valid TV entries.
    Returns (start_offset, count) or None.
    """
    best_start = None
    best_count = 0
    i = 0
    while i < len(scnr) - _TV_STRIDE:
        if _is_valid_tv_entry(scnr[i:i + _TV_STRIDE]):
            # Extend the run forward
            run_start = i
            run_count = 1
            j = i + _TV_STRIDE
            while j + _TV_STRIDE <= len(scnr):
                if _is_valid_tv_entry(scnr[j:j + _TV_STRIDE]):
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
    return (best_start, best_count) if best_start is not None else None


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

        result = _find_tv_array(scnr_meta)
        if result is None:
            return []

        start_off, count = result
        volumes = []
        for idx in range(count):
            eo    = start_off + idx * _TV_STRIDE
            entry = scnr_meta[eo:eo + _TV_STRIDE]
            fw  = (_rf(entry,  0), _rf(entry,  4), _rf(entry,  8))
            up  = (_rf(entry, 12), _rf(entry, 16), _rf(entry, 20))
            pos = (_rf(entry, 24), _rf(entry, 28), _rf(entry, 32))
            ext = (_rf(entry, 36), _rf(entry, 40), _rf(entry, 44))
            volumes.append(TriggerVolume(idx, fw, up, pos, ext))

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
