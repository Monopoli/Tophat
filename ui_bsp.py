"""
Halo 2 Xbox Object Monitor — BSP Geometry tab.

Parses collision BSP sections from a Halo 2 Xbox .map file and renders a
wireframe projection.

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

  The only real cost is the initial geometry load.  For spacestation section 1
  (~27k edges) this takes ~1-2s on first load, after which all navigation is
  effectively free.

  To keep the initial load from blocking the UI we batch the create_line calls
  and yield to the event loop every 2000 edges via after(0, ...) chaining.
"""

import os
import struct
import math
import tkinter as tk
from tkinter import ttk, filedialog


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

class BspMixin:
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

        # StringVars / BooleanVars — must be created before any widget
        self._bsp_view        = tk.StringVar(value='Top')
        self._bsp_show_edges  = tk.BooleanVar(value=True)
        self._bsp_show_verts  = tk.BooleanVar(value=False)
        self._bsp_show_objs   = tk.BooleanVar(value=True)
        self._bsp_z_filter    = tk.BooleanVar(value=False)
        self._bsp_zmin_var    = tk.DoubleVar(value=-50.0)
        self._bsp_zmax_var    = tk.DoubleVar(value=10.0)
        self._bsp_angle       = 0.0

        # ── Control bar ───────────────────────────────────────────────────
        ctrl = ttk.Frame(parent)
        ctrl.pack(fill=tk.X, padx=8, pady=(8, 4))

        ttk.Button(ctrl, text='Load .map file…',
                   command=self._bsp_load_file).pack(side=tk.LEFT)

        self._bsp_file_lbl = ttk.Label(ctrl, text='No .map loaded.',
                                        foreground='#9898b8',
                                        font=('Consolas', 9))
        self._bsp_file_lbl.pack(side=tk.LEFT, padx=(8, 0))

        self._bsp_sect_frame = ttk.Frame(ctrl)
        self._bsp_sect_frame.pack(side=tk.LEFT, padx=(12, 0))
        ttk.Label(self._bsp_sect_frame, text='Section:').pack(side=tk.LEFT)
        self._bsp_sect_var = tk.StringVar()
        self._bsp_sect_combo = ttk.Combobox(
            self._bsp_sect_frame, textvariable=self._bsp_sect_var,
            state='readonly', width=42)
        self._bsp_sect_combo.pack(side=tk.LEFT, padx=(4, 0))
        self._bsp_sect_combo.bind('<<ComboboxSelected>>', self._bsp_on_section_change)
        self._bsp_sect_frame.pack_forget()

        sep = ttk.Separator(ctrl, orient=tk.VERTICAL)
        sep.pack(side=tk.LEFT, fill=tk.Y, padx=8, pady=2)

        ttk.Checkbutton(ctrl, text='Edges',
                        variable=self._bsp_show_edges,
                        command=self._bsp_rebuild_geo).pack(side=tk.LEFT)
        ttk.Checkbutton(ctrl, text='Vertices',
                        variable=self._bsp_show_verts,
                        command=self._bsp_rebuild_geo).pack(side=tk.LEFT)
        ttk.Checkbutton(ctrl, text='Objects',
                        variable=self._bsp_show_objs,
                        command=self._bsp_draw_objects).pack(side=tk.LEFT)

        ttk.Separator(ctrl, orient=tk.VERTICAL).pack(
            side=tk.LEFT, fill=tk.Y, padx=8, pady=2)
        ttk.Label(ctrl, text='Z filter:').pack(side=tk.LEFT)
        ttk.Checkbutton(ctrl, text='Enable',
                        variable=self._bsp_z_filter,
                        command=self._bsp_rebuild_geo).pack(side=tk.LEFT)
        ttk.Label(ctrl, text='min:').pack(side=tk.LEFT, padx=(6, 2))
        ttk.Entry(ctrl, textvariable=self._bsp_zmin_var, width=7).pack(side=tk.LEFT)
        ttk.Label(ctrl, text='max:').pack(side=tk.LEFT, padx=(4, 2))
        ttk.Entry(ctrl, textvariable=self._bsp_zmax_var, width=7).pack(side=tk.LEFT)
        ttk.Button(ctrl, text='Apply', command=self._bsp_rebuild_geo,
                   width=6).pack(side=tk.LEFT, padx=4)

        self._bsp_stat_lbl = ttk.Label(ctrl, text='', foreground='#9898b8',
                                        font=('Consolas', 8))
        self._bsp_stat_lbl.pack(side=tk.RIGHT)

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
        self._bsp_fit_view()

    def _bsp_on_section_change(self, _event=None):
        idx = self._bsp_sect_combo.current()
        if 0 <= idx < len(self._bsp_sections):
            self._bsp_geo = self._bsp_sections[idx]
            self._bsp_fit_view()

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
        self._bsp_fit_view()

    def _proj_hv(self, wx, wy, wz, view, ca, sa):
        """Project one world vertex to rotated (h, v) plane coords."""
        if view == 'Front':
            h, v = wx, wz
        elif view == 'Side':
            h, v = wy, wz
        elif view == 'Iso':
            h = wx - wy
            v = (wx + wy) * 0.5 - wz
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
            span_h = (g.xmax - g.ymin) - (g.xmin - g.ymax)
            span_v = ((g.xmax+g.ymax)*0.5 - g.zmin) - ((g.xmin+g.ymin)*0.5 - g.zmax)
            ch_world = cv_world = 0.0
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

    def _bsp_on_resize(self, event=None):
        self._bsp_draw_objects()
        self._bsp_draw_overlay()

    # ── Geometry rebuild (one-time per view/angle/filter change) ──────────
    #
    # Projects all verts, builds a flat list of canvas coords for each visible
    # edge, then issues create_line calls in batches to avoid blocking the UI.
    # All items are tagged 'geo'.  Subsequent pan/zoom just call c.move/c.scale.

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
        if show_edges:
            verts_w = g.verts
            for (i0, i1) in g.edges_unique:
                if z_filter:
                    if not (zmin_f <= verts_w[i0][2] <= zmax_f and
                            zmin_f <= verts_w[i1][2] <= zmax_f):
                        continue
                edges_to_draw.append((proj[i0][0], proj[i0][1],
                                      proj[i1][0], proj[i1][1]))

        vert_col = '#3a5080'
        verts_to_draw = []
        if show_verts:
            for i, (_, _, wz) in enumerate(g.verts):
                if z_filter and not (zmin_f <= wz <= zmax_f):
                    continue
                verts_to_draw.append(proj[i])

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
                              fill=edge_col, width=1, tags='geo')
            if end < len(edges_to_draw):
                self._bsp_file_lbl.config(
                    text=self._bsp_file_lbl.cget('text').split('  [')[0] +
                         f'  [loading {end}/{len(edges_to_draw)} edges…]')
                self.after(0, lambda: batch_edges(end))
            else:
                # Edges done — draw verts then finish up
                for (px, py) in verts_to_draw:
                    c.create_rectangle(px-1, py-1, px+1, py+1,
                                       fill=vert_col, outline='', tags='geo')
                self._bsp_loading = False
                lbl = self._bsp_file_lbl.cget('text').split('  [')[0]
                self._bsp_file_lbl.config(text=lbl)
                self._bsp_draw_objects()
                self._bsp_draw_overlay()

        self.after(0, lambda: batch_edges(0))

    # ── Pan / zoom — pure canvas transform, no item rebuild ───────────────

    def _bsp_apply_pan(self, dx, dy):
        """Translate all geo items and update pan state."""
        self._bsp_pan_x += dx
        self._bsp_pan_y += dy
        self._bsp_canvas.move('geo', dx, dy)
        self._bsp_draw_objects()
        self._bsp_draw_overlay()

    def _bsp_apply_zoom(self, factor, cx, cy):
        """Scale all geo items around (cx, cy) and update transform state."""
        self._bsp_pan_x = cx + (self._bsp_pan_x - cx) * factor
        self._bsp_pan_y = cy + (self._bsp_pan_y - cy) * factor
        self._bsp_scale *= factor
        self._bsp_canvas.scale('geo', cx, cy, factor, factor)
        self._bsp_update_zoom_lbl()
        self._bsp_draw_objects()
        self._bsp_draw_overlay()

    # ── Object dots and overlay (redrawn each tick / pan / zoom) ──────────

    def _bsp_draw_objects(self):
        c = self._bsp_canvas
        c.delete('dynamic')
        g = self._bsp_geo
        if not g or not self._bsp_show_objs.get():
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
                          fill=col, outline='#ffffff', width=1, tags='dynamic')

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
        if self._bsp_drag is None:
            return
        sx, sy = self._bsp_drag
        self._bsp_drag = (event.x, event.y)
        self._bsp_apply_pan(event.x - sx, event.y - sy)

    def _bsp_drag_end(self, event):
        self._bsp_drag = None

    def _bsp_zoom_wheel(self, event):
        factor = 1.15 if (event.num == 4 or event.delta > 0) else 1 / 1.15
        self._bsp_apply_zoom(factor, event.x, event.y)

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
        except Exception:
            pass
