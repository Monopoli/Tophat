"""
Halo 2 Xbox Object Monitor — BSP Geometry tab.

Parses collision BSP sections from a Halo 2 Xbox .map file and renders a
wireframe projection.  Also parses and renders trigger volumes from the
scenario tag as dashed OBB wireframes (see trigger_volumes.py).

Rendering strategy (Option D — tkinter canvas vector):
  Geometry is loaded once per view/angle/Z-filter change as native tkinter
  canvas line items tagged 'geo'.  Pan and zoom are implemented as canvas
  c.move('geo', dx, dy) and c.scale('geo', ox, oy, fx, fy) — Tk applies a
  matrix transform to all items in its C layer with no Python redraw loop.
  Lines stay perfectly sharp at all zoom levels.

  Cost breakdown:
    Load / view / angle / Z-filter change  → O(edges) create_line calls (one-time)
    Pan                                    → one c.move()  call  (instant)
    Zoom                                   → one c.scale() call  (instant)
    Poll tick (object dots)                → c.delete('dynamic') + O(active objects)

  This is fast for a handful of items, but c.move()/c.scale() are still
  O(items tagged 'geo') in Tk's C layer — with tens of thousands of BSP
  edge items, navigation can start to feel laggy even though no Python
  redraw is involved (see _bsp_apply_pan / _bsp_apply_zoom docstrings).

  Two mitigations are available, independently togglable in the control bar:
    - Detail cull (LOD): skip creating edges whose on-screen projected
      length is below a pixel threshold at rebuild time. Cheap, keeps the
      vector architecture, partial win — see the 'Detail cull' controls
      and the lod_* code in _bsp_rebuild_geo().
    - Raster edge mode: render the whole wireframe to an off-screen Pillow
      image once per rebuild and display it as a SINGLE canvas image item,
      so c.move()/c.scale() touch one item instead of N. Pan is exact
      (pure translation). Zoom shows a cheaply resampled live preview via
      _bsp_raster_live_resize(), then a debounced full-resolution rebake
      restores crispness once the gesture settles
      (_bsp_raster_schedule_rebake / _bsp_raster_rebake_settled). Requires
      Pillow — see HAS_PIL below, same optional-dependency pattern as
      ui_map.py's BSP-background feature.
"""

import os
import struct
import math
import tkinter as tk
from tkinter import ttk, filedialog

from trigger_volumes import TriggerVolumeMixin, get_trigger_volumes
from cluster_portals import ClusterPortalMixin, get_cluster_portals

try:
    from PIL import Image, ImageDraw, ImageTk
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


# ── BSP geometry for a single sbsp section ────────────────────────────────

class BspGeometry:
    """Parsed collision BSP geometry for one sbsp tag."""
    __slots__ = (
        'verts', 'triangles', 'edges_unique',
        'xmin', 'xmax', 'ymin', 'ymax', 'zmin', 'zmax',
        'map_name', 'scenario_path', 'section_label',
        # Projected coords — rebuilt when view/angle changes, never on pan/zoom
        'proj_verts',    # list of (px, py) in neutral canvas space (scale=1, pan=0,0)
        'proj_key',      # (view, angle, z_filter, zmin, zmax, show_e, show_v) that built it
    )

    def __init__(self):
        self.verts            = []
        self.triangles        = []
        self.edges_unique     = []
        self.xmin = self.xmax = 0.0
        self.ymin = self.ymax = 0.0
        self.zmin = self.zmax = 0.0
        self.map_name         = ''
        self.scenario_path    = ''
        self.section_label    = ''
        self.proj_verts       = []
        self.proj_key         = None


# ── Low-level binary helpers ───────────────────────────────────────────────

def _rf(d, o):
    v = struct.unpack_from('<f', d, o)[0]
    return v if not (v != v) and abs(v) < 1e15 else None

def _ri16(d, o):  return struct.unpack_from('<H', d, o)[0]
def _ri16s(d, o): return struct.unpack_from('<h', d, o)[0]
def _ri32(d, o):  return struct.unpack_from('<I', d, o)[0]

def _read_4cc(d, o):
    return d[o:o+4][::-1].decode('ascii', errors='replace')


def _find_sbsp_geometry_blocks(bsp_meta: bytes, sbsp_voff: int):
    meta_size = len(bsp_meta)
    seen = set()
    best = None
    best_vc = 0

    for bt in range(0x20, min(0x2000, meta_size - 64), 4):
        valid = []
        for b in range(8):
            pos = bt + b * 8
            if pos + 8 > meta_size:
                break
            cnt = _ri32(bsp_meta, pos)
            ptr = _ri32(bsp_meta, pos + 4)
            off = ptr - sbsp_voff
            if 0 < off < meta_size and 10 <= cnt <= 200000:
                valid.append((cnt, off))
            else:
                if valid:
                    break
        if len(valid) < 3:
            continue

        sc, so = valid[-3]
        ec, eo = valid[-2]
        vc, vo = valid[-1]

        key = (sc, ec, vc)
        if key in seen:
            continue
        seen.add(key)

        if vo + 48 > meta_size:
            continue

        xs, ys = [], []
        for vi in range(min(vc, 50)):
            x = _rf(bsp_meta, vo + vi * 16)
            y = _rf(bsp_meta, vo + vi * 16 + 4)
            if (x is not None and y is not None
                    and abs(x) < 50000 and abs(y) < 50000):
                xs.append(x)
                ys.append(y)
        if len(xs) < 3:
            continue

        spread = (max(xs) - min(xs)) + (max(ys) - min(ys))
        if 5.0 <= spread <= 2000.0 and vc > best_vc:
            best_vc = vc
            best = (sc, so, ec, eo, vc, vo)

    return best


def _parse_single_sbsp(bsp_meta: bytes, sbsp_voff: int) -> BspGeometry | None:
    try:
        blocks = _find_sbsp_geometry_blocks(bsp_meta, sbsp_voff)
        if blocks is None:
            return None

        SURF_COUNT, SURF_OFF, EDGE_COUNT, EDGE_OFF, VERT_COUNT, VERT_OFF = blocks
        geo = BspGeometry()

        for i in range(VERT_COUNT):
            o = VERT_OFF + i * 16
            x = _rf(bsp_meta, o)
            y = _rf(bsp_meta, o + 4)
            z = _rf(bsp_meta, o + 8)
            geo.verts.append((x or 0.0, y or 0.0, z or 0.0))

        nonzero = [(x, y, z) for x, y, z in geo.verts if abs(x) + abs(y) > 0.1]
        if nonzero:
            geo.xmin = min(v[0] for v in nonzero)
            geo.xmax = max(v[0] for v in nonzero)
            geo.ymin = min(v[1] for v in nonzero)
            geo.ymax = max(v[1] for v in nonzero)
            geo.zmin = min(v[2] for v in nonzero)
            geo.zmax = max(v[2] for v in nonzero)

        edge_set = set()
        for si in range(SURF_COUNT):
            o          = SURF_OFF + si * 8
            first_edge = _ri16s(bsp_meta, o + 2)
            poly = []
            eidx = first_edge
            for _ in range(24):
                eo  = EDGE_OFF + eidx * 12
                sv  = _ri16(bsp_meta, eo)
                ev  = _ri16(bsp_meta, eo + 2)
                fwd = _ri16(bsp_meta, eo + 4)
                rev = _ri16(bsp_meta, eo + 6)
                ls  = _ri16(bsp_meta, eo + 8)
                if ls == si:
                    poly.append(sv);  eidx = fwd
                else:
                    poly.append(ev);  eidx = rev
                a, b = (sv, ev) if sv < ev else (ev, sv)
                edge_set.add((a, b))
                if eidx == first_edge:
                    break
            for j in range(1, len(poly) - 1):
                geo.triangles.append((poly[0], poly[j], poly[j + 1]))

        geo.edges_unique = list(edge_set)
        return geo

    except Exception:
        return None


def parse_all_bsp_sections(map_path: str) -> list[BspGeometry]:
    try:
        with open(map_path, 'rb') as f:
            hdr = f.read(0x800)

        if _ri32(hdr, 0x004) != 8:
            return []

        map_name      = hdr[0x1A8:0x1C8].split(b'\x00')[0].decode('ascii', errors='replace')
        scenario_path = hdr[0x1C8:0x208].split(b'\x00')[0].decode('ascii', errors='replace')

        tag_file_off   = _ri32(hdr, 0x010)
        tag_length     = _ri32(hdr, 0x014)

        with open(map_path, 'rb') as f:
            f.seek(tag_file_off)
            tag_section = f.read(tag_length)

        tag_entries_offset = _ri32(tag_section, 0x08)
        tag_count          = _ri32(tag_section, 0x18)

        sbsp_entries = []
        for i in range(tag_count):
            off = tag_entries_offset + i * 16
            if _read_4cc(tag_section, off) == 'sbsp':
                sbsp_entries.append((_ri32(tag_section, off + 8),
                                     _ri32(tag_section, off + 12)))

        results = []
        for idx, (sbsp_voff, sbsp_size) in enumerate(sbsp_entries):
            with open(map_path, 'rb') as f:
                f.seek(tag_file_off + sbsp_voff)
                bsp_meta = f.read(sbsp_size)

            geo = _parse_single_sbsp(bsp_meta, sbsp_voff)
            if geo is None:
                continue

            geo.map_name      = map_name
            geo.scenario_path = scenario_path
            geo.section_label = (
                f'Section {idx + 1}  '
                f'({len(geo.verts):,} verts, '
                f'{len(geo.edges_unique):,} edges)'
            )
            results.append(geo)

        return results

    except Exception as e:
        print(f'BSP parse error: {e}')
        return []


# ── Cache ──────────────────────────────────────────────────────────────────

_bsp_cache: dict[str, list[BspGeometry]] = {}

def get_bsp_sections(map_path: str) -> list[BspGeometry]:
    if map_path not in _bsp_cache:
        sections = parse_all_bsp_sections(map_path)
        if sections:
            _bsp_cache[map_path] = sections
    return _bsp_cache.get(map_path, [])

def get_bsp_geometry(map_path: str):
    secs = get_bsp_sections(map_path)
    return secs[0] if secs else None


# ── BspMixin ───────────────────────────────────────────────────────────────

# Batch size for incremental canvas item creation (edges per after() tick)
_BATCH = 2000

# Min interval between coalesced pan/zoom canvas transform calls, in ms.
# Both c.move() and c.scale() are O(items tagged 'geo') on the Tk/C side —
# not because the coordinate math is slow, but because each call marks
# the canvas's dirty rectangle and queues a redraw that re-rasterizes every
# item whose bounding box intersects it (Tk's damage/repair model). A BSP
# section can have 50,000+ edge items; rapid <B1-Motion>/<MouseWheel> bursts
# (common with trackpads and high-res wheels, and just fast mouse drags)
# can fire many events before a single redraw finishes, so without
# coalescing each one queues its own full-scene repaint and the visible
# result is a jump-then-stall pattern as the backlog drains.
# 8ms (~120Hz) is comfortably above typical display refresh rates, so it
# never becomes the limiting factor on perceived smoothness, while still
# coalescing bursts down to one transform call per window.
_TRANSFORM_FLUSH_MS = 8

# ── Raster edge-mode constants ──────────────────────────────────────────────
# Padding (px) baked around the viewport so panning doesn't immediately
# reveal blank canvas; exceeding ~60% of this in either axis schedules a
# rebake (see _bsp_apply_pan).
_RASTER_MARGIN = 250
# Cap on the live-resized preview's pixel dimensions during an active zoom
# gesture, just to bound memory/time on an extreme zoom-out before the
# debounced rebake replaces it with a properly-sized fresh render.
_RASTER_LIVE_MAX_PX = 6000
# How long to wait after the last pan/zoom flush before doing a full,
# crisp re-render of the raster image. Long enough that a continuous
# gesture doesn't keep re-triggering it, short enough that the live
# (resampled, slightly soft) preview snaps back to crisp almost
# immediately after the user stops.
_RASTER_REBAKE_DEBOUNCE_MS = 200

# World-unit span (across the shorter canvas dimension) used for the
# DEFAULT view on load / section change / view-projection change — see
# _bsp_view_origin(). Many campaign maps have a large outer bounding /
# kill-volume shell as part of their collision BSP, so fitting to the
# full extent (_bsp_fit_view, still used by the 'Fit' button) starts
# zoomed out far enough that the actual playable geometry near the
# origin is barely visible. Tune this if your maps run bigger/smaller —
# it's just a starting point; +/- zoom and the 'Fit' button still work
# normally from there.
_DEFAULT_VIEW_SPAN = 200.0

class BspMixin(TriggerVolumeMixin, ClusterPortalMixin):
    """BSP geometry visualiser tab — vector canvas rendering."""

    def _build_bsp_panel(self, parent):
        self._bsp_sections:   list[BspGeometry] = []
        self._bsp_geo:        BspGeometry | None = None
        self._bsp_map_path:   str = ''

        # Canvas transform state — tracks the cumulative pan/scale applied
        # to the 'geo' tag since the last full geometry rebuild.
        self._bsp_scale    = 1.0   # current world→canvas scale (px per world unit)
        self._bsp_pan_x    = 0.0   # canvas x of world origin
        self._bsp_pan_y    = 0.0   # canvas y of world origin
        self._bsp_drag     = None
        self._bsp_loading  = False  # True while batched geo load is in progress
        self._bsp_pending_zoom = None  # [factor, cx, cy] accumulated this window, or None
        self._bsp_zoom_flush_armed = False  # True while a flush is scheduled and pending
        self._bsp_pending_pan = None  # [dx, dy] accumulated this window, or None
        self._bsp_pan_flush_armed = False  # True while a flush is scheduled and pending

        # StringVars / BooleanVars — must be created before any widget
        self._bsp_view        = tk.StringVar(value='Top')
        self._bsp_show_edges  = tk.BooleanVar(value=True)
        self._bsp_show_verts  = tk.BooleanVar(value=False)
        self._bsp_show_objs   = tk.BooleanVar(value=True)
        self._bsp_z_filter    = tk.BooleanVar(value=False)
        self._bsp_zmin_var    = tk.DoubleVar(value=-50.0)
        self._bsp_zmax_var    = tk.DoubleVar(value=10.0)
        self._bsp_angle       = 0.0
        self._bsp_show_wireframe = tk.BooleanVar(value=True)
        self._bsp_follow_player  = tk.BooleanVar(value=False)

        # Detail culling (LOD): edges whose ON-SCREEN projected length is
        # below this many pixels are skipped entirely at build time. They
        # still cost a transform on every later c.move()/c.scale() call if
        # we create them, for zero visible benefit, so the cheapest fix is
        # to simply never create the canvas item in the first place.
        # Re-evaluated on every rebuild (view/angle/Z-filter/Edges/Vertices
        # change, Fit, snap-angle), so it tracks the scale that was active
        # at that point — see _bsp_rebuild_geo() for the actual filter.
        self._bsp_lod_enable  = tk.BooleanVar(value=True)
        self._bsp_lod_min_px  = tk.DoubleVar(value=1.0)

        # Edge render mode: 'Vector' = today's per-edge create_line items
        # (optionally LOD-culled above); 'Raster' = whole wireframe baked
        # to one Pillow image, displayed as a single canvas image item.
        # Falls back to 'Vector' if Pillow isn't installed.
        self._bsp_edge_render = tk.StringVar(value='Vector')
        self._bsp_raster_item       = None   # canvas image item id, or None
        self._bsp_raster_photo      = None   # current PhotoImage (keep a ref so it isn't GC'd)
        self._bsp_raster_base_img   = None   # PIL Image as rendered at the last bake
        self._bsp_raster_base_scale = 1.0    # self._bsp_scale at bake time
        self._bsp_raster_base_pan   = (0.0, 0.0)
        self._bsp_raster_drift      = [0.0, 0.0]  # accumulated pan since last bake
        self._bsp_raster_rebake_after_id = None   # scheduled debounce id, or None

        # ── Control bar, row 1: file loading + layer visibility toggles ────
        ctrl1 = ttk.Frame(parent)
        ctrl1.pack(fill=tk.X, padx=8, pady=(8, 2))

        ttk.Button(ctrl1, text='Load .map file…',
                   command=self._bsp_load_file).pack(side=tk.LEFT)

        self._bsp_file_lbl = ttk.Label(ctrl1, text='No .map loaded.',
                                        foreground='#9898b8',
                                        font=('Consolas', 9))
        self._bsp_file_lbl.pack(side=tk.LEFT, padx=(8, 0))

        self._bsp_sect_frame = ttk.Frame(ctrl1)
        self._bsp_sect_frame.pack(side=tk.LEFT, padx=(12, 0))
        ttk.Label(self._bsp_sect_frame, text='Section:').pack(side=tk.LEFT)
        self._bsp_sect_var = tk.StringVar()
        self._bsp_sect_combo = ttk.Combobox(
            self._bsp_sect_frame, textvariable=self._bsp_sect_var,
            state='readonly', width=42)
        self._bsp_sect_combo.pack(side=tk.LEFT, padx=(4, 0))
        self._bsp_sect_combo.bind('<<ComboboxSelected>>', self._bsp_on_section_change)
        self._bsp_sect_frame.pack_forget()

        ttk.Separator(ctrl1, orient=tk.VERTICAL).pack(
            side=tk.LEFT, fill=tk.Y, padx=8, pady=2)

        # All show/hide layer toggles live together here: the three that
        # decide what gets built into the rebuild (Edges, Vertices,
        # Objects), the one that just flips visibility on what's already
        # built (Geometry), and the trigger-volume / cluster-portal
        # toggles injected by their own mixins.
        ttk.Label(ctrl1, text='Layers:').pack(side=tk.LEFT)
        ttk.Checkbutton(ctrl1, text='Edges',
                        variable=self._bsp_show_edges,
                        command=self._bsp_rebuild_geo).pack(side=tk.LEFT, padx=(4, 0))
        ttk.Checkbutton(ctrl1, text='Vertices',
                        variable=self._bsp_show_verts,
                        command=self._bsp_rebuild_geo).pack(side=tk.LEFT)
        ttk.Checkbutton(ctrl1, text='Objects',
                        variable=self._bsp_show_objs,
                        command=self._bsp_on_show_objs_toggle).pack(side=tk.LEFT)
        ttk.Checkbutton(ctrl1, text='Geometry',
                        variable=self._bsp_show_wireframe,
                        command=self._bsp_apply_wireframe_visibility,
                        ).pack(side=tk.LEFT)

        # ── Trigger volume toggle (TriggerVolumeMixin) ────────────────────
        self._tv_inject_controls(ctrl1)

        # ── Cluster portal toggle (ClusterPortalMixin) ─────────────────────
        self._cp_inject_controls(ctrl1)

        self._bsp_stat_lbl = ttk.Label(ctrl1, text='', foreground='#9898b8',
                                        font=('Consolas', 8))
        self._bsp_stat_lbl.pack(side=tk.RIGHT)

        # ── Control bar, row 2: filtering / render-quality groups ──────────
        ctrl2 = ttk.Frame(parent)
        ctrl2.pack(fill=tk.X, padx=8, pady=(0, 4))

        ttk.Label(ctrl2, text='Z filter:').pack(side=tk.LEFT)
        ttk.Checkbutton(ctrl2, text='Enable',
                        variable=self._bsp_z_filter,
                        command=self._bsp_rebuild_geo).pack(side=tk.LEFT)
        ttk.Label(ctrl2, text='min:').pack(side=tk.LEFT, padx=(6, 2))
        ttk.Entry(ctrl2, textvariable=self._bsp_zmin_var, width=7).pack(side=tk.LEFT)
        ttk.Label(ctrl2, text='max:').pack(side=tk.LEFT, padx=(4, 2))
        ttk.Entry(ctrl2, textvariable=self._bsp_zmax_var, width=7).pack(side=tk.LEFT)
        ttk.Button(ctrl2, text='Apply', command=self._bsp_rebuild_geo,
                   width=6).pack(side=tk.LEFT, padx=4)

        ttk.Separator(ctrl2, orient=tk.VERTICAL).pack(
            side=tk.LEFT, fill=tk.Y, padx=8, pady=2)
        ttk.Label(ctrl2, text='Detail cull:').pack(side=tk.LEFT)
        ttk.Checkbutton(ctrl2, text='Enable',
                        variable=self._bsp_lod_enable,
                        command=self._bsp_rebuild_geo).pack(side=tk.LEFT)
        ttk.Label(ctrl2, text='min px:').pack(side=tk.LEFT, padx=(6, 2))
        ttk.Entry(ctrl2, textvariable=self._bsp_lod_min_px, width=5).pack(side=tk.LEFT)
        ttk.Button(ctrl2, text='Apply', command=self._bsp_rebuild_geo,
                   width=6).pack(side=tk.LEFT, padx=4)
        self._bsp_lod_lbl = ttk.Label(ctrl2, text='', foreground='#9898b8',
                                       font=('Consolas', 8))
        self._bsp_lod_lbl.pack(side=tk.LEFT, padx=(6, 0))

        ttk.Separator(ctrl2, orient=tk.VERTICAL).pack(
            side=tk.LEFT, fill=tk.Y, padx=8, pady=2)
        ttk.Label(ctrl2, text='Edge render:').pack(side=tk.LEFT)
        _raster_state = tk.NORMAL if HAS_PIL else tk.DISABLED
        ttk.Radiobutton(ctrl2, text='Vector', value='Vector',
                        variable=self._bsp_edge_render,
                        command=self._bsp_rebuild_geo).pack(side=tk.LEFT)
        ttk.Radiobutton(ctrl2, text='Raster', value='Raster',
                        variable=self._bsp_edge_render,
                        state=_raster_state,
                        command=self._bsp_rebuild_geo).pack(side=tk.LEFT)
        if not HAS_PIL:
            ttk.Label(ctrl2, text='(needs Pillow)', foreground='#7a4a4a',
                      font=('Consolas', 8)).pack(side=tk.LEFT, padx=(2, 0))

        # ── Navigation bar ────────────────────────────────────────────────
        nav = ttk.Frame(parent)
        nav.pack(fill=tk.X, padx=8, pady=(0, 2))

        # View projection buttons
        ttk.Label(nav, text='View:', foreground='#9898b8',
                  font=('Consolas', 9)).pack(side=tk.LEFT)
        self._bsp_view_btns = {}
        for _v in ('Top', 'Front', 'Side', 'Iso'):
            _active = (_v == 'Top')
            btn = tk.Button(
                nav, text=_v, width=5, font=('Consolas', 9),
                relief=tk.SUNKEN if _active else tk.RAISED,
                bg='#1e3a6e' if _active else '#1c1c28',
                fg='#ffffff' if _active else '#9898b8',
                activebackground='#22223a', activeforeground='#ffffff',
                bd=1, cursor='hand2',
                command=lambda v=_v: self._bsp_set_view(v),
            )
            btn.pack(side=tk.LEFT, padx=1)
            self._bsp_view_btns[_v] = btn

        ttk.Separator(nav, orient=tk.VERTICAL).pack(
            side=tk.LEFT, fill=tk.Y, padx=6, pady=2)

        # Zoom
        ttk.Button(nav, text='-', width=3,
                   command=self._bsp_zoom_out).pack(side=tk.LEFT)
        self._bsp_zoom_lbl = ttk.Label(nav, text='100%', width=6,
                                        font=('Consolas', 9),
                                        foreground='#9898b8', anchor='center')
        self._bsp_zoom_lbl.pack(side=tk.LEFT)
        ttk.Button(nav, text='+', width=3,
                   command=self._bsp_zoom_in).pack(side=tk.LEFT)

        ttk.Separator(nav, orient=tk.VERTICAL).pack(
            side=tk.LEFT, fill=tk.Y, padx=6, pady=2)

        # Pan arrows
        ttk.Button(nav, text='<', width=3,
                   command=lambda: self._bsp_pan_step(-1, 0)).pack(side=tk.LEFT)
        ttk.Button(nav, text='^', width=3,
                   command=lambda: self._bsp_pan_step(0, 1)).pack(side=tk.LEFT)
        ttk.Button(nav, text='v', width=3,
                   command=lambda: self._bsp_pan_step(0, -1)).pack(side=tk.LEFT)
        ttk.Button(nav, text='>', width=3,
                   command=lambda: self._bsp_pan_step(1, 0)).pack(side=tk.LEFT)

        ttk.Separator(nav, orient=tk.VERTICAL).pack(
            side=tk.LEFT, fill=tk.Y, padx=6, pady=2)

        ttk.Button(nav, text='Fit', width=4,
                   command=self._bsp_fit_view).pack(side=tk.LEFT)
        ttk.Button(nav, text='Origin', width=7,
                   command=self._bsp_view_origin).pack(side=tk.LEFT, padx=(2, 0))
        ttk.Button(nav, text='Player', width=7,
                   command=self._bsp_center_on_player).pack(side=tk.LEFT, padx=(2, 0))
        ttk.Checkbutton(nav, text='Follow',
                        variable=self._bsp_follow_player,
                        command=self._bsp_on_follow_toggle).pack(side=tk.LEFT, padx=(4, 0))

        ttk.Separator(nav, orient=tk.VERTICAL).pack(
            side=tk.LEFT, fill=tk.Y, padx=6, pady=2)

        # Snap-to-angle
        ttk.Label(nav, text='Snap:', foreground='#9898b8',
                  font=('Consolas', 9)).pack(side=tk.LEFT)
        for _lbl, _ang in [('0', 0), ('45', 45), ('90', 90), ('135', 135),
                            ('180', 180), ('225', 225), ('270', 270), ('315', 315)]:
            ttk.Button(nav, text=_lbl, width=4,
                       command=lambda a=_ang: self._bsp_snap_angle(a)
                       ).pack(side=tk.LEFT, padx=1)

        ttk.Separator(nav, orient=tk.VERTICAL).pack(
            side=tk.LEFT, fill=tk.Y, padx=6, pady=2)

        self._bsp_angle_lbl = ttk.Label(nav, text='0 deg', font=('Consolas', 9),
                                         foreground='#9898b8', width=6)
        self._bsp_angle_lbl.pack(side=tk.LEFT)

        # ── Canvas ────────────────────────────────────────────────────────
        self._bsp_canvas = tk.Canvas(parent, bg='#0d0d12',
                                      highlightthickness=0, cursor='crosshair')
        self._bsp_canvas.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 8))
        self._bsp_canvas.bind('<Configure>', self._bsp_on_resize)
        self._bsp_canvas.bind('<Motion>',    self._bsp_mouse_move)
        self._bsp_canvas.bind('<ButtonPress-1>',   self._bsp_drag_start)
        self._bsp_canvas.bind('<B1-Motion>',       self._bsp_drag_move)
        self._bsp_canvas.bind('<ButtonRelease-1>', self._bsp_drag_end)
        self._bsp_canvas.bind('<MouseWheel>',      self._bsp_zoom_wheel)
        self._bsp_canvas.bind('<Button-4>',        self._bsp_zoom_wheel)
        self._bsp_canvas.bind('<Button-5>',        self._bsp_zoom_wheel)

        self._bsp_coord_lbl = ttk.Label(parent, text='', foreground='#9898b8',
                                         font=('Consolas', 8))
        self._bsp_coord_lbl.pack(fill=tk.X, padx=8)

    # ── File loading ───────────────────────────────────────────────────────

    def _bsp_load_file(self):
        path = filedialog.askopenfilename(
            title='Select Halo 2 Xbox .map file',
            filetypes=[('Map files', '*.map'), ('All files', '*.*')])
        if not path:
            return
        self._bsp_map_path = path
        short = os.path.basename(path)
        self._bsp_file_lbl.config(text=f'Loading {short}…')
        self.update_idletasks()

        self._bsp_sections = get_bsp_sections(path)

        if not self._bsp_sections:
            self._bsp_file_lbl.config(
                text=f'Failed to parse {short} (not Halo 2 Xbox v8?)')
            self._bsp_sect_frame.pack_forget()
            return

        labels = [g.section_label for g in self._bsp_sections]
        self._bsp_sect_combo.configure(values=labels)
        self._bsp_sect_combo['width'] = min(55, max(30, max(len(l) for l in labels)))
        self._bsp_sect_combo.current(0)
        self._bsp_sect_frame.pack(side=tk.LEFT, padx=(12, 0))

        self._bsp_geo = self._bsp_sections[0]
        g = self._bsp_geo
        self._bsp_file_lbl.config(text=f'{short}  ({g.map_name})')
        self._bsp_stat_lbl.config(text=f'{len(self._bsp_sections)} sections')
        self._tv_on_map_loaded(path)
        self._cp_on_map_loaded(path)
        self._bsp_view_origin()

    def _bsp_on_section_change(self, _event=None):
        idx = self._bsp_sect_combo.current()
        if 0 <= idx < len(self._bsp_sections):
            self._bsp_geo = self._bsp_sections[idx]
            self._bsp_view_origin()

    # ── View / projection helpers ──────────────────────────────────────────

    def _bsp_set_view(self, view: str):
        self._bsp_view.set(view)
        for v, btn in self._bsp_view_btns.items():
            if v == view:
                btn.config(relief=tk.SUNKEN, bg='#1e3a6e', fg='#ffffff')
            else:
                btn.config(relief=tk.RAISED, bg='#1c1c28', fg='#9898b8')
        self._bsp_angle = 0.0
        self._bsp_angle_lbl.config(text='0 deg')
        self._bsp_view_origin()

    def _proj_hv(self, wx, wy, wz, view, ca, sa):
        """Project one world vertex to rotated (h, v) plane coords."""
        if view == 'Front':
            h, v = wx, wz
        elif view == 'Side':
            h, v = wy, wz
        elif view == 'Iso':
            h = wx - wy
            v = (wx + wy) * 0.5 + wz
        else:  # Top
            h, v = wx, wy
        return h * ca + v * sa, -h * sa + v * ca

    def _hv_to_canvas(self, h, v):
        """Convert (h, v) projected coords to canvas pixels."""
        return h * self._bsp_scale + self._bsp_pan_x, \
              -v * self._bsp_scale + self._bsp_pan_y

    def _bsp_fit_view(self):
        g = self._bsp_geo
        if not g:
            return
        cw = self._bsp_canvas.winfo_width()  or 800
        ch = self._bsp_canvas.winfo_height() or 600
        pad = 32
        view = self._bsp_view.get()

        if view == 'Front':
            span_h, span_v = g.xmax - g.xmin, g.zmax - g.zmin
            ch_world = (g.xmin + g.xmax) / 2
            cv_world = (g.zmin + g.zmax) / 2
        elif view == 'Side':
            span_h, span_v = g.ymax - g.ymin, g.zmax - g.zmin
            ch_world = (g.ymin + g.ymax) / 2
            cv_world = (g.zmin + g.zmax) / 2
        elif view == 'Iso':
            # h = wx - wy is maximised/minimised by opposite corners of the
            # X/Y box; v = (wx+wy)*0.5 + wz similarly. Compute the actual
            # centre instead of assuming it's at world origin — that
            # assumption silently mis-fit (and partially clipped) any
            # geometry not symmetric around (0,0,0).
            max_h, min_h = g.xmax - g.ymin, g.xmin - g.ymax
            max_v = (g.xmax + g.ymax) * 0.5 + g.zmax
            min_v = (g.xmin + g.ymin) * 0.5 + g.zmin
            span_h, span_v = max_h - min_h, max_v - min_v
            ch_world = (max_h + min_h) / 2
            cv_world = (max_v + min_v) / 2
        else:  # Top
            span_h, span_v = g.xmax - g.xmin, g.ymax - g.ymin
            ch_world = (g.xmin + g.xmax) / 2
            cv_world = (g.ymin + g.ymax) / 2

        if span_h < 1 or span_v < 1:
            return

        self._bsp_scale = min((cw - pad*2) / span_h, (ch - pad*2) / span_v)
        self._bsp_pan_x = cw/2 - ch_world * self._bsp_scale
        self._bsp_pan_y = ch/2 + cv_world * self._bsp_scale
        self._bsp_update_zoom_lbl()
        self._bsp_rebuild_geo()

    def _bsp_view_origin(self):
        """Default camera: centred on world (0,0,0) at a fixed, modest
        zoom (_DEFAULT_VIEW_SPAN world units across the shorter canvas
        dimension), rather than fit-to-extent. World origin always
        projects to (h,v) = (0,0) regardless of view/angle (every
        _proj_hv branch is linear with no offset), so centring on it is
        just panning to the canvas centre — no projection math needed."""
        g = self._bsp_geo
        if not g:
            return
        cw = self._bsp_canvas.winfo_width()  or 800
        ch = self._bsp_canvas.winfo_height() or 600
        pad = 32
        self._bsp_scale = (min(cw, ch) - pad * 2) / _DEFAULT_VIEW_SPAN
        self._bsp_pan_x = cw / 2
        self._bsp_pan_y = ch / 2
        self._bsp_update_zoom_lbl()
        self._bsp_rebuild_geo()

    def _bsp_find_player_origin(self):
        """Look up the locally-tracked player's world position. Player
        slots only carry a SlaveUnitIndex, not a position — same
        cross-reference into the live object table by salt that the
        Player tab's unit panel uses, since that's the only place world
        position actually lives. Returns (wx, wy, wz) or None."""
        objects = getattr(self, '_objects', [])
        players = getattr(self, '_player_data', [])
        for p in players:
            if p.get('left_game'):
                continue
            unit_obj = None
            slave = p.get('slave_unit_index', 0xFFFFFFFF)
            if slave != 0xFFFFFFFF:
                slave_salt = (slave >> 16) & 0xFFFF
                unit_obj = next((o for o in objects if o.get('salt') == slave_salt), None)
            if unit_obj is None:
                pcg_unit = p.get('ctrl', {}).get('unit_index', 0xFFFFFFFF)
                if pcg_unit != 0xFFFFFFFF:
                    pcg_salt = (pcg_unit >> 16) & 0xFFFF
                    unit_obj = next((o for o in objects if o.get('salt') == pcg_salt), None)
            if unit_obj is not None:
                orig = unit_obj.get('origin')
                if orig and orig[0] is not None:
                    return orig
        return None

    def _bsp_center_on_player(self):
        """One-shot version: pan (current zoom unchanged) so the player
        is centred right now, going through a full rebuild. Used by the
        'Player' button and once immediately whenever 'Follow player' is
        switched on. The continuous per-tick version is _bsp_follow_tick,
        which does the same math but as a cheap incremental c.move()
        instead of a rebuild — see that docstring for why."""
        g = self._bsp_geo
        if not g:
            return

        target = self._bsp_find_player_origin()
        if target is None:
            if hasattr(self, '_bsp_stat_lbl'):
                self._bsp_stat_lbl.config(
                    text='No live player position (not connected / not spawned?)')
            return

        wx, wy, wz = target
        view  = self._bsp_view.get()
        a     = math.radians(self._bsp_angle)
        ca, sa = math.cos(a), math.sin(a)
        h, v = self._proj_hv(wx, wy, wz, view, ca, sa)
        cw = self._bsp_canvas.winfo_width()  or 800
        ch = self._bsp_canvas.winfo_height() or 600
        self._bsp_pan_x = cw / 2 - h * self._bsp_scale
        self._bsp_pan_y = ch / 2 + v * self._bsp_scale
        self._bsp_update_zoom_lbl()
        self._bsp_rebuild_geo()

    def _bsp_on_follow_toggle(self):
        """Command for the 'Follow player' checkbox. Tk updates the
        BooleanVar before invoking this, so .get() already reflects the
        new state. Snap to the player immediately on enable, for instant
        feedback rather than waiting for the next poll tick."""
        if self._bsp_follow_player.get():
            self._bsp_center_on_player()

    def _bsp_follow_tick(self):
        """Continuous version of _bsp_center_on_player, called once per
        poll tick from _bsp_tick() (already gated on the BSP tab being
        active). Deliberately does NOT call _bsp_rebuild_geo() — doing a
        full delete-and-recreate of every edge item on every tick would
        undo all the pan/zoom performance work elsewhere in this file.
        Instead it computes the player's CURRENT projected canvas position
        from the live scale/pan/view/angle and nudges the view by exactly
        the offset needed to bring them back to centre, via the same
        c.move()-based _bsp_apply_pan() pan uses — O(items) in Tk's C
        layer, not a Python redraw, so this is just as cheap as a manual
        drag regardless of edge count or render mode.

        Manual pan/zoom still work normally while following: zooming
        changes how much area you see around the player; panning away
        will simply get corrected back to centre on the next tick (that's
        the point of 'follow' — uncheck it to look around freely)."""
        if not self._bsp_follow_player.get():
            return
        g = self._bsp_geo
        if not g:
            return
        target = self._bsp_find_player_origin()
        if target is None:
            return  # not spawned / not connected yet — silently wait, no label spam

        wx, wy, wz = target
        view  = self._bsp_view.get()
        a     = math.radians(self._bsp_angle)
        ca, sa = math.cos(a), math.sin(a)
        h, v = self._proj_hv(wx, wy, wz, view, ca, sa)
        px, py = self._hv_to_canvas(h, v)
        cw = self._bsp_canvas.winfo_width()  or 800
        ch = self._bsp_canvas.winfo_height() or 600
        dx, dy = cw / 2 - px, ch / 2 - py
        if dx * dx + dy * dy < 0.25:
            return  # sub-pixel — not worth a move() call
        self._bsp_apply_pan(dx, dy)

    def _bsp_on_resize(self, event=None):
        self._bsp_draw_objects()
        self._bsp_draw_overlay()

    # ── Geometry rebuild (one-time per view/angle/filter change) ──────────
    #
    # Projects all verts, builds a flat list of canvas coords for each visible
    # edge, then issues create_line calls in batches to avoid blocking the UI.
    # All items are tagged 'geo'.  Subsequent pan/zoom just call c.move/c.scale.

    def _bsp_apply_wireframe_visibility(self):
        """Show/hide the BSP wireframe (edges + verts) without touching
        trigger volume or cluster portal items, and without forcing a
        rebuild — used by the 'Geometry' layer checkbox."""
        c = self._bsp_canvas
        state = 'normal' if self._bsp_show_wireframe.get() else 'hidden'
        c.itemconfigure('wireframe', state=state)

    def _bsp_rebuild_geo(self):
        """Reproject and redraw all geometry canvas items."""
        if self._bsp_loading:
            # Cancel any in-progress batch load
            self._bsp_loading = False

        c = self._bsp_canvas
        c.delete('geo')
        c.delete('dynamic')
        c.delete('overlay')
        self._bsp_draw_overlay()

        # Raster state belongs to whichever 'geo' items just got deleted
        # above — always clear it here so a stale item id / stale base
        # image can never linger into the next mode or the next rebuild.
        self._bsp_raster_item = None
        self._bsp_raster_base_img = None
        self._bsp_raster_drift = [0.0, 0.0]
        if self._bsp_raster_rebake_after_id is not None:
            self.after_cancel(self._bsp_raster_rebake_after_id)
            self._bsp_raster_rebake_after_id = None

        g = self._bsp_geo
        if not g or not g.verts:
            cw = c.winfo_width() or 800
            ch = c.winfo_height() or 600
            c.create_text(cw//2, ch//2,
                          text='Load a .map file to view BSP geometry',
                          fill='#2a2a5a', font=('Consolas', 13), tags='overlay')
            return

        z_filter = self._bsp_z_filter.get()
        try:
            zmin_f = self._bsp_zmin_var.get()
            zmax_f = self._bsp_zmax_var.get()
        except Exception:
            z_filter = False
            zmin_f = zmax_f = 0.0

        view       = self._bsp_view.get()
        angle      = self._bsp_angle
        show_edges = self._bsp_show_edges.get()
        show_verts = self._bsp_show_verts.get()
        ca = math.cos(math.radians(angle))
        sa = math.sin(math.radians(angle))

        # Project all verts to canvas coords at current scale/pan
        proj = []
        for (wx, wy, wz) in g.verts:
            h, v = self._proj_hv(wx, wy, wz, view, ca, sa)
            px, py = self._hv_to_canvas(h, v)
            proj.append((px, py))
        g.proj_verts = proj

        # Build edge list — flat coord tuples for create_line
        edge_col = '#1a3060'
        edges_to_draw = []
        n_culled = 0
        lod_enabled = self._bsp_lod_enable.get()
        try:
            lod_min_px = max(0.0, self._bsp_lod_min_px.get())
        except Exception:
            lod_min_px = 0.0
        lod_min_px2 = lod_min_px * lod_min_px
        if show_edges:
            verts_w = g.verts
            for (i0, i1) in g.edges_unique:
                if z_filter:
                    if not (zmin_f <= verts_w[i0][2] <= zmax_f and
                            zmin_f <= verts_w[i1][2] <= zmax_f):
                        continue
                x0, y0 = proj[i0]
                x1, y1 = proj[i1]
                if lod_enabled and lod_min_px2 > 0:
                    # Cheap on-screen length test using coords already
                    # projected at the CURRENT scale/pan — no extra trig,
                    # no sqrt. An edge under threshold contributes nothing
                    # visually but would still cost a transform on every
                    # later pan/zoom if we created it, so skip it here.
                    dx, dy = x1 - x0, y1 - y0
                    if dx * dx + dy * dy < lod_min_px2:
                        n_culled += 1
                        continue
                edges_to_draw.append((x0, y0, x1, y1))

        if hasattr(self, '_bsp_lod_lbl'):
            if lod_enabled and lod_min_px > 0 and (edges_to_draw or n_culled):
                self._bsp_lod_lbl.config(
                    text=f'{len(edges_to_draw):,} drawn / {n_culled:,} culled')
            else:
                self._bsp_lod_lbl.config(text='')

        vert_col = '#3a5080'
        verts_to_draw = []
        if show_verts:
            for i, (_, _, wz) in enumerate(g.verts):
                if z_filter and not (zmin_f <= wz <= zmax_f):
                    continue
                verts_to_draw.append(proj[i])

        # ── Finish-up steps shared by both edge render paths ───────────────
        def finish_rebuild():
            self._bsp_apply_wireframe_visibility()
            self._tv_draw()
            self._cp_draw()
            self._bsp_draw_objects()
            self._bsp_draw_overlay()

        if self._bsp_edge_render.get() == 'Raster' and HAS_PIL:
            self._bsp_loading = False
            self._bsp_raster_build(edges_to_draw, verts_to_draw, edge_col, vert_col)
            finish_rebuild()
            return

        # ── Vector path: today's per-edge create_line items, batched ───────
        # Batch-load canvas items via after() so the UI stays responsive
        self._bsp_loading = True
        self._bsp_file_lbl.config(
            text=self._bsp_file_lbl.cget('text').split('  [')[0] +
                 f'  [loading 0/{len(edges_to_draw)} edges…]')

        def batch_edges(start):
            if not self._bsp_loading:
                return
            end = min(start + _BATCH, len(edges_to_draw))
            for i in range(start, end):
                x0, y0, x1, y1 = edges_to_draw[i]
                c.create_line(x0, y0, x1, y1,
                              fill=edge_col, width=1, tags=('geo', 'wireframe'))
            if end < len(edges_to_draw):
                self._bsp_file_lbl.config(
                    text=self._bsp_file_lbl.cget('text').split('  [')[0] +
                         f'  [loading {end}/{len(edges_to_draw)} edges…]')
                self.after(0, lambda: batch_edges(end))
            else:
                # Edges done — draw verts then finish up
                for (px, py) in verts_to_draw:
                    c.create_rectangle(px-1, py-1, px+1, py+1,
                                       fill=vert_col, outline='', tags=('geo', 'wireframe'))
                self._bsp_loading = False
                lbl = self._bsp_file_lbl.cget('text').split('  [')[0]
                self._bsp_file_lbl.config(text=lbl)
                finish_rebuild()

        self.after(0, lambda: batch_edges(0))

    # ── Raster edge rendering (alternate to per-edge vector items) ─────────
    #
    # Bakes the whole wireframe (post-LOD-cull edge list, already projected
    # at the CURRENT scale/pan) into one Pillow image and shows it as a
    # single canvas image item tagged 'geo' (so it pans/zooms alongside
    # triggers/portals/object-dots with zero changes to _bsp_apply_pan) and
    # 'wireframe' (so the Geometry layer checkbox still hides/shows it) and
    # 'raster' (for its own selective bookkeeping).
    #
    # Padding the image by _RASTER_MARGIN px beyond the viewport on each
    # side lets ordinary panning move the (exact, lossless) image around
    # for a while before a gap could appear; _bsp_apply_pan tracks drift
    # since the last bake and schedules a rebake before that happens.
    #
    # Tk's canvas.scale() repositions an image item's anchor correctly
    # (same point-transform math as any other item) but does NOT resize
    # its pixel content. So the image participates in c.scale('geo', ...)
    # for position only; _bsp_apply_zoom separately calls
    # _bsp_raster_live_resize() to resample the image to the new size —
    # cheap because cost depends on output canvas pixel dimensions, not on
    # edge count — and _bsp_raster_schedule_rebake() to queue a full crisp
    # re-render once the gesture settles.

    def _bsp_raster_build(self, edges_to_draw, verts_to_draw, edge_col, vert_col):
        c = self._bsp_canvas
        c.delete('raster')
        cw = c.winfo_width()  or 800
        ch = c.winfo_height() or 600
        m  = _RASTER_MARGIN

        bg = self._bsp_canvas.cget('bg')  # '#0d0d12' — keep the image seamless with the canvas
        img = Image.new('RGB', (cw + 2*m, ch + 2*m), bg)
        draw = ImageDraw.Draw(img)
        for (x0, y0, x1, y1) in edges_to_draw:
            draw.line([(x0 + m, y0 + m), (x1 + m, y1 + m)], fill=edge_col, width=1)
        for (px, py) in verts_to_draw:
            draw.rectangle([px + m - 1, py + m - 1, px + m + 1, py + m + 1], fill=vert_col)

        photo = ImageTk.PhotoImage(img)
        item = c.create_image(-m, -m, anchor='nw', image=photo,
                              tags=('geo', 'wireframe', 'raster'))

        self._bsp_raster_item       = item
        self._bsp_raster_photo      = photo  # keep a ref — Tk drops the image if GC'd
        self._bsp_raster_base_img   = img
        self._bsp_raster_base_scale = self._bsp_scale
        self._bsp_raster_base_pan   = (self._bsp_pan_x, self._bsp_pan_y)
        self._bsp_raster_drift      = [0.0, 0.0]

    def _bsp_raster_live_resize(self):
        """Cheap resampled preview during an active zoom gesture — called
        from _bsp_apply_zoom. Resizes the BASE image (from the last bake)
        to match the current scale; Tk has already moved the item's anchor
        correctly via c.scale(), so only the pixel content needs updating."""
        if self._bsp_edge_render.get() != 'Raster' or not HAS_PIL:
            return
        if self._bsp_raster_item is None or self._bsp_raster_base_img is None:
            return
        if self._bsp_raster_base_scale <= 0:
            return
        r = self._bsp_scale / self._bsp_raster_base_scale
        if r <= 0:
            return
        base = self._bsp_raster_base_img
        w = min(_RASTER_LIVE_MAX_PX, max(1, round(base.width * r)))
        h = min(_RASTER_LIVE_MAX_PX, max(1, round(base.height * r)))
        resized = base.resize((w, h), Image.NEAREST)
        self._bsp_raster_photo = ImageTk.PhotoImage(resized)
        self._bsp_canvas.itemconfigure(self._bsp_raster_item, image=self._bsp_raster_photo)
        self._bsp_raster_schedule_rebake()

    def _bsp_raster_schedule_rebake(self):
        """(Re)start the settle timer. Repeated calls during a continuous
        gesture keep pushing this back, so the actual rebake only fires
        once input goes quiet for _RASTER_REBAKE_DEBOUNCE_MS."""
        if self._bsp_edge_render.get() != 'Raster' or not HAS_PIL:
            return
        if self._bsp_raster_rebake_after_id is not None:
            self.after_cancel(self._bsp_raster_rebake_after_id)
        self._bsp_raster_rebake_after_id = self.after(
            _RASTER_REBAKE_DEBOUNCE_MS, self._bsp_raster_rebake_settled)

    def _bsp_raster_rebake_settled(self):
        """Gesture has settled — do a full, crisp re-render at the current
        scale/pan. Reuses the normal rebuild path, which is cheap relative
        to the gesture it's settling after (no per-frame cost, one-shot)."""
        self._bsp_raster_rebake_after_id = None
        if self._bsp_edge_render.get() != 'Raster' or not HAS_PIL:
            return
        self._bsp_rebuild_geo()

    def _bsp_apply_pan(self, dx, dy):
        """Translate all geo items (BSP wireframe, trigger volumes, portals,
        and object dots — all tagged 'geo') and update pan state.  This is
        the only per-event work; it is O(1) regardless of scene size because
        it's a single Tk canvas transform, not a Python-side redraw.  Object
        dots are NOT reprojected here — they ride along via the shared tag,
        and the independent _bsp_tick() poll keeps their world positions
        fresh on its own schedule.  The overlay text is static during a pan
        (it shows scale/bounds, neither of which change), so it's skipped.

        In raster mode the wireframe image rides along via the same 'geo'
        tag — c.move() is an exact translation for an image item, no
        resampling needed, so this stays just as free as the vector case.
        We do track cumulative drift since the last bake, though: once it
        gets close to the padding margin baked into the image, a rebake is
        scheduled so panning never actually reveals blank canvas."""
        self._bsp_pan_x += dx
        self._bsp_pan_y += dy
        self._bsp_canvas.move('geo', dx, dy)

        if self._bsp_edge_render.get() == 'Raster' and self._bsp_raster_item is not None:
            self._bsp_raster_drift[0] += dx
            self._bsp_raster_drift[1] += dy
            margin = _RASTER_MARGIN
            if (abs(self._bsp_raster_drift[0]) > margin * 0.6 or
                    abs(self._bsp_raster_drift[1]) > margin * 0.6):
                self._bsp_raster_schedule_rebake()

    def _bsp_apply_zoom(self, factor, cx, cy):
        """Scale all geo items around (cx, cy) and update transform state.
        Same O(1) reasoning as _bsp_apply_pan — see that docstring.  The
        overlay IS refreshed here because the displayed zoom percentage
        changes; that's two cheap create_text calls, not the bottleneck.

        In raster mode, c.scale() correctly repositions the wireframe
        image's anchor (Tk applies the same point-transform to any item
        type) but does NOT resize its pixel content — that part is on us,
        via _bsp_raster_live_resize(), which also arms the debounced
        rebake so the live (resampled, slightly soft) preview snaps back
        to a crisp re-render shortly after the gesture stops."""
        self._bsp_pan_x = cx + (self._bsp_pan_x - cx) * factor
        self._bsp_pan_y = cy + (self._bsp_pan_y - cy) * factor
        self._bsp_scale *= factor
        self._bsp_canvas.scale('geo', cx, cy, factor, factor)
        self._bsp_update_zoom_lbl()
        self._bsp_draw_overlay()
        self._bsp_raster_live_resize()

    # ── Object dots and overlay (redrawn each tick / pan / zoom) ──────────

    def _bsp_clear_objects(self):
        """Remove any visible object dots from the canvas without doing any
        of the recompute work in _bsp_draw_objects. Used when the
        'Objects' checkbox is unchecked, so the existing dots disappear
        immediately rather than lingering until some other redraw clears
        them incidentally."""
        self._bsp_canvas.delete('dynamic')

    def _bsp_on_show_objs_toggle(self):
        """Checkbox command for 'Objects'. Tk updates the BooleanVar before
        invoking this, so _bsp_show_objs.get() already reflects the new
        state. On uncheck: clear the dots immediately (one cheap delete)
        without touching the projection/iteration logic. On check: do a
        normal full redraw."""
        if self._bsp_show_objs.get():
            self._bsp_draw_objects()
        else:
            self._bsp_clear_objects()

    def _bsp_draw_objects(self):
        """
        Redraw object dots from self._objects.

        The 'Objects' checkbox (_bsp_show_objs) is checked FIRST, before
        any other work — including the c.delete('dynamic') that used to
        run unconditionally on every call. With the checkbox off, this is
        now a single attribute read and nothing else: no delete, no
        iteration over self._objects, no projection math. This matters
        most for the poll-tick call path (_bsp_tick), which invokes this
        once per tick regardless of the checkbox state — previously every
        tick still paid for a Tk dirty-rectangle delete even with objects
        hidden; now a disabled toggle costs one boolean check per tick and
        nothing more.

        Clearing already-visible dots when the checkbox is unchecked is
        handled by _bsp_on_show_objs_toggle / _bsp_clear_objects, not by
        this function, so that the common (no-op) tick path doesn't need
        to do a delete it doesn't need.
        """
        if not self._bsp_show_objs.get():
            return

        c = self._bsp_canvas
        c.delete('dynamic')
        g = self._bsp_geo
        if not g:
            return

        from constants import TYPE_COLORS
        cw = c.winfo_width()  or 800
        ch = c.winfo_height() or 600
        z_filter = self._bsp_z_filter.get()
        try:
            zmin_f = self._bsp_zmin_var.get()
            zmax_f = self._bsp_zmax_var.get()
        except Exception:
            z_filter = False
            zmin_f = zmax_f = 0.0

        view  = self._bsp_view.get()
        angle = self._bsp_angle
        ca = math.cos(math.radians(angle))
        sa = math.sin(math.radians(angle))
        margin = 8

        for o in getattr(self, '_objects', []):
            if not o.get('active'):
                continue
            orig = o.get('origin') or (None, None, None)
            if orig[0] is None:
                continue
            if z_filter and not (zmin_f <= orig[2] <= zmax_f):
                continue
            h, v = self._proj_hv(orig[0], orig[1], orig[2], view, ca, sa)
            px, py = self._hv_to_canvas(h, v)
            if not (-margin <= px <= cw + margin and -margin <= py <= ch + margin):
                continue
            typ = o.get('type', 'object')
            col = TYPE_COLORS.get(typ, '#9898b8')
            r = 4 if typ in ('biped', 'vehicle') else 3
            c.create_oval(px-r, py-r, px+r, py+r,
                          fill=col, outline='#ffffff', width=1, tags=('dynamic', 'geo'))

    def _bsp_draw_overlay(self):
        """Redraw the status text overlay (always on top)."""
        c  = self._bsp_canvas
        cw = c.winfo_width()  or 800
        ch = c.winfo_height() or 600
        c.delete('overlay')
        g = self._bsp_geo
        if not g:
            return
        c.create_text(4, ch - 4,
                      text=f'Scale: {self._bsp_scale:.3f} px/wu  '
                           f'[{self._bsp_view.get()}]  [{g.section_label}]',
                      fill='#2a2a5a', font=('Consolas', 8),
                      anchor='sw', tags='overlay')
        c.create_text(cw - 4, ch - 4,
                      text=f'X:{g.xmin:.0f}…{g.xmax:.0f}  '
                           f'Y:{g.ymin:.0f}…{g.ymax:.0f}  '
                           f'Z:{g.zmin:.0f}…{g.zmax:.0f}',
                      fill='#2a2a5a', font=('Consolas', 8),
                      anchor='se', tags='overlay')

    # ── Input handlers ─────────────────────────────────────────────────────

    def _bsp_zoom_in(self):
        c = self._bsp_canvas
        cx, cy = (c.winfo_width() or 800) / 2, (c.winfo_height() or 600) / 2
        self._bsp_apply_zoom(1.25, cx, cy)

    def _bsp_zoom_out(self):
        c = self._bsp_canvas
        cx, cy = (c.winfo_width() or 800) / 2, (c.winfo_height() or 600) / 2
        self._bsp_apply_zoom(1 / 1.25, cx, cy)

    def _bsp_pan_step(self, dx, dy):
        c    = self._bsp_canvas
        step = (c.winfo_width() or 800) * 0.15
        self._bsp_apply_pan(dx * step, -dy * step)

    def _bsp_snap_angle(self, degrees):
        self._bsp_angle = float(degrees)
        self._bsp_angle_lbl.config(text=f'{degrees} deg')
        self._bsp_rebuild_geo()

    def _bsp_drag_start(self, event):
        self._bsp_drag = (event.x, event.y)

    def _bsp_drag_move(self, event):
        """
        Accumulate the drag delta immediately, but defer the actual
        c.move() call to a fixed-rate flush — identical reasoning to
        _bsp_zoom_wheel: <B1-Motion> can fire many times per second during
        a fast mouse drag, and each c.move('geo', ...) call marks Tk's
        whole-canvas dirty rectangle and queues a redraw that re-rasterizes
        every one of the tens of thousands of BSP edge items. Without
        coalescing, a fast drag queues a full-scene repaint per motion
        event, and the visible result is exactly the 'screen updates, then
        waits, then updates' stutter — the input queue outruns the redraw,
        so several deltas pile up before the next repaint actually shows.
        """
        if self._bsp_drag is None:
            return
        sx, sy = self._bsp_drag
        self._bsp_drag = (event.x, event.y)
        dx, dy = event.x - sx, event.y - sy

        if self._bsp_pending_pan is None:
            self._bsp_pending_pan = [dx, dy]
        else:
            self._bsp_pending_pan[0] += dx
            self._bsp_pending_pan[1] += dy

        if not self._bsp_pan_flush_armed:
            self._bsp_pan_flush_armed = True
            self.after(_TRANSFORM_FLUSH_MS, self._bsp_flush_pan)

    def _bsp_flush_pan(self):
        """Apply the accumulated drag delta from this window's motion
        events as a single c.move() call.  Same armed-flag discipline as
        _bsp_flush_zoom — cleared on fire, not on consume — so a
        continuous drag gets one flush per _TRANSFORM_FLUSH_MS window with
        no rearm gap in between."""
        self._bsp_pan_flush_armed = False
        pending = self._bsp_pending_pan
        self._bsp_pending_pan = None
        if pending is None:
            return
        dx, dy = pending
        self._bsp_apply_pan(dx, dy)

    def _bsp_drag_end(self, event):
        self._bsp_drag = None

    def _bsp_zoom_wheel(self, event):
        """
        Accumulate the wheel delta immediately (so the zoom *feels*
        responsive — _bsp_pending_zoom always reflects the latest cursor
        position and combined factor), but defer the actual c.scale() call
        to a fixed-rate flush via after().

        Why this matters: c.scale('geo', ...) is O(items tagged 'geo') in
        Tk's C layer — tens of thousands of BSP edges, plus trigger volume
        and portal items, plus object dots, all get their coordinate lists
        rewritten on every call. A single physical scroll gesture can emit
        a burst of MouseWheel events (trackpads and high-res wheels often
        fire 10+ in well under a second). Without coalescing, each one
        queues its own full-scene rescale, and Tk processes them serially
        before any repaint.

        Scheduling is decoupled from flushing via _bsp_zoom_flush_armed:
        the flush timer is only (re)armed when it isn't already running,
        so a continuous scroll keeps a single recurring ~120fps cadence
        instead of a fresh one-shot timer being scheduled after every
        flush. An earlier version armed a new one-shot after() only when
        pending was None, which meant every flush briefly cleared the
        pending slot and the very next wheel tick had to wait out a full
        fresh window before its result became visible — a visible 'step,
        then stall' even during smooth, continuous scrolling. Keeping a
        flush flag that only clears once the timer itself fires (not when
        the data is consumed) removes that gap entirely.
        """
        factor = 1.15 if (event.num == 4 or event.delta > 0) else 1 / 1.15

        if self._bsp_pending_zoom is None:
            self._bsp_pending_zoom = [factor, event.x, event.y]
        else:
            # Combine with whatever's already queued; keep the most recent
            # cursor position as the zoom centre.
            self._bsp_pending_zoom[0] *= factor
            self._bsp_pending_zoom[1] = event.x
            self._bsp_pending_zoom[2] = event.y

        if not self._bsp_zoom_flush_armed:
            self._bsp_zoom_flush_armed = True
            self.after(_TRANSFORM_FLUSH_MS, self._bsp_flush_zoom)

    def _bsp_flush_zoom(self):
        """Apply the accumulated zoom factor from this window's wheel
        events as a single c.scale() call.  The flush-armed flag is
        cleared here (not when pending is consumed), and is only re-armed
        by the next wheel event — so a continuous scroll gets one flush
        per _TRANSFORM_FLUSH_MS window with no extra rearm latency in between."""
        self._bsp_zoom_flush_armed = False
        pending = self._bsp_pending_zoom
        self._bsp_pending_zoom = None
        if pending is None:
            return
        factor, cx, cy = pending
        self._bsp_apply_zoom(factor, cx, cy)

    def _bsp_mouse_move(self, event):
        wx, wy = self._c2w(event.x, event.y)
        self._bsp_coord_lbl.config(
            text=f'  canvas ({event.x},{event.y})   world ({wx:.2f}, {wy:.2f})')

    def _bsp_update_zoom_lbl(self):
        if not hasattr(self, '_bsp_zoom_lbl'):
            return
        g = self._bsp_geo
        if g and (g.xmax - g.xmin) > 0:
            cw  = self._bsp_canvas.winfo_width() or 800
            pct = int(round(self._bsp_scale * (g.xmax - g.xmin) /
                            max(1, cw - 64) * 100))
        else:
            pct = int(round(self._bsp_scale * 100))
        self._bsp_zoom_lbl.config(text=f'{pct}%')

    def _w2c(self, wx, wy, wz=0.0):
        view = self._bsp_view.get()
        a = math.radians(self._bsp_angle)
        ca, sa = math.cos(a), math.sin(a)
        h, v = self._proj_hv(wx, wy, wz, view, ca, sa)
        return self._hv_to_canvas(h, v)

    def _c2w(self, px, py):
        rx = (px - self._bsp_pan_x) / self._bsp_scale
        ry = -(py - self._bsp_pan_y) / self._bsp_scale
        a  = math.radians(-self._bsp_angle)
        ca, sa = math.cos(a), math.sin(a)
        return rx * ca + ry * sa, -rx * sa + ry * ca

    # ── Poll tick ──────────────────────────────────────────────────────────

    def _bsp_tick(self):
        try:
            tab = self._main_nb.index(self._main_nb.select())
            if tab == 5:
                self._bsp_draw_objects()
                self._bsp_follow_tick()
        except Exception:
            pass
