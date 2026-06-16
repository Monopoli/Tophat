"""
Halo 2 Xbox Object Monitor — Map tab mixin.

Map calibration:
  The user sets two reference points to map world coords -> pixel coords:
    - Centre point:  a known world (x, y) that sits at the centre of the image
    - Corner point:  a known world (x, y) that sits at one corner of the image
  From these two points the monitor derives scale (world-units per pixel) and
  the pixel origin, then projects every tracked object in real time.

Map images:
  Drop a PNG named after the scenario leaf into the maps/ sub-folder alongside
  the scripts, e.g.  maps/01b_spacestation.png
  Until a real image exists a grey placeholder is drawn automatically.

Object icons (drawn on canvas, no image files needed):
  biped        ● filled circle        purple
  vehicle      ◆ filled diamond       blue
  weapon       ✕ cross                coral
  equipment    ▲ triangle             pink
  garbage      · small dot            grey
  projectile   → arrow head           amber
  scenery      □ open square          green
  machine      ⬡ hexagon              teal
  control      ⊕ circle+cross         teal dark
  light_fixture ★ star                yellow
  sound_scenery ♪ note                teal light
  crate        ▭ rectangle            lavender
  creature     ✦ 4-point star         red
"""

import math
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from constants import OBJECT_TYPES, TYPE_COLORS
from ui_objects import make_display_type

try:
    from PIL import Image, ImageTk
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


# ── Icon drawing helpers ───────────────────────────────────────────────────

ICON_SIZE = 8   # half-width of most icons in pixels

ICON_COLORS = {
    "biped":        "#9F99FF",
    "vehicle":      "#60b8ff",
    "weapon":       "#ff7055",
    "equipment":    "#e070a0",
    "garbage":      "#888090",
    "projectile":   "#ffb840",
    "scenery":      "#70cc50",
    "machine":      "#30c0a0",
    "control":      "#208070",
    "light_fixture":"#ffe060",
    "sound_scenery":"#60e0c0",
    "crate":        "#c0b0ff",
    "creature":     "#ff7070",
}


def _draw_icon(canvas, x, y, obj_type, label="", trail=None, selected=False):
    """Draw a type-specific icon at (x, y) on canvas. Returns list of item ids."""
    color   = ICON_COLORS.get(obj_type, "#aaaaaa")
    sel_col = "#ffffff"
    s       = ICON_SIZE
    ids     = []

    # Optional trail
    if trail and len(trail) >= 2:
        pts = []
        for tx, ty in trail:
            pts += [tx, ty]
        ids.append(canvas.create_line(
            *pts, fill=color, width=1,
            dash=(3, 3), tags="trail"))

    outline = sel_col if selected else color

    if obj_type == "biped":
        ids.append(canvas.create_oval(
            x-s, y-s, x+s, y+s,
            fill=color, outline=outline, width=2 if selected else 1))

    elif obj_type == "vehicle":
        pts = [x, y-s, x+s, y, x, y+s, x-s, y]
        ids.append(canvas.create_polygon(
            pts, fill=color, outline=outline, width=2 if selected else 1))

    elif obj_type == "weapon":
        w = s - 1
        ids.append(canvas.create_line(x-w, y-w, x+w, y+w, fill=color, width=2))
        ids.append(canvas.create_line(x+w, y-w, x-w, y+w, fill=color, width=2))

    elif obj_type == "equipment":
        pts = [x, y-s, x+s, y+s, x-s, y+s]
        ids.append(canvas.create_polygon(
            pts, fill=color, outline=outline, width=1))

    elif obj_type == "garbage":
        ids.append(canvas.create_oval(
            x-3, y-3, x+3, y+3, fill=color, outline=""))

    elif obj_type == "projectile":
        ids.append(canvas.create_polygon(
            [x-s, y-3, x+2, y, x-s, y+3],
            fill=color, outline=""))

    elif obj_type == "scenery":
        ids.append(canvas.create_rectangle(
            x-s, y-s, x+s, y+s,
            fill="", outline=color, width=2))

    elif obj_type == "machine":
        # hexagon
        pts = []
        for i in range(6):
            a = math.radians(60 * i - 30)
            pts += [x + s * math.cos(a), y + s * math.sin(a)]
        ids.append(canvas.create_polygon(
            pts, fill="", outline=color, width=2))

    elif obj_type == "control":
        ids.append(canvas.create_oval(
            x-s, y-s, x+s, y+s, fill="", outline=color, width=2))
        ids.append(canvas.create_line(x-s, y, x+s, y, fill=color, width=1))
        ids.append(canvas.create_line(x, y-s, x, y+s, fill=color, width=1))

    elif obj_type == "light_fixture":
        # 5-point star
        pts = []
        for i in range(5):
            ao = math.radians(72 * i - 90)
            ai = math.radians(72 * i - 90 + 36)
            pts += [x + s * math.cos(ao), y + s * math.sin(ao)]
            pts += [x + (s*0.4) * math.cos(ai), y + (s*0.4) * math.sin(ai)]
        ids.append(canvas.create_polygon(
            pts, fill=color, outline=""))

    elif obj_type == "sound_scenery":
        ids.append(canvas.create_oval(
            x-3, y-3, x+3, y+3, fill=color, outline=""))
        ids.append(canvas.create_line(
            x+3, y-3, x+s, y-s, fill=color, width=1))

    elif obj_type == "crate":
        ids.append(canvas.create_rectangle(
            x-s, y-int(s*0.6), x+s, y+int(s*0.6),
            fill=color, outline=outline, width=1))

    elif obj_type == "creature":
        # 4-point star
        pts = [x, y-s, x+3, y-3, x+s, y, x+3, y+3,
               x, y+s, x-3, y+3, x-s, y, x-3, y-3]
        ids.append(canvas.create_polygon(
            pts, fill=color, outline=""))

    else:
        ids.append(canvas.create_oval(
            x-4, y-4, x+4, y+4, fill=color, outline=""))

    # Label (index)
    if label:
        ids.append(canvas.create_text(
            x + s + 3, y, text=label,
            fill=color, font=("Consolas", 7), anchor="w"))

    return ids


# ── MapMixin ──────────────────────────────────────────────────────────────

class MapMixin:
    """Top-down map tab with calibration, object tracking and path trails."""

    def _build_map_panel(self, parent):
        # ── State ─────────────────────────────────────────────────────────
        self._map_image_path: str | None  = None
        self._map_photo                   = None   # ImageTk reference
        self._map_bg_id                   = None   # canvas item id for bg
        # Calibration: centre world coord and corner world coord + corner pixel
        self._map_cal_cx  = tk.DoubleVar(value=0.0)
        self._map_cal_cy  = tk.DoubleVar(value=0.0)
        self._map_cal_wx  = tk.DoubleVar(value=100.0)
        self._map_cal_wy  = tk.DoubleVar(value=100.0)
        self._map_cal_px  = tk.DoubleVar(value=0.0)   # corner pixel x (0 = left)
        self._map_cal_py  = tk.DoubleVar(value=0.0)   # corner pixel y (0 = top)
        # Tracked objects: {index: {'trail': deque, 'show_trail': bool}}
        self._map_tracked: dict[int, dict] = {}
        self._map_trail_len = 60           # max trail length in samples
        self._map_show_labels = tk.BooleanVar(value=True)
        self._map_active_only = tk.BooleanVar(value=False)
        # Canvas item ids for current frame (cleared each redraw)
        self._map_drawn_ids: list = []

        # ── Layout: left = controls, right = canvas ────────────────────────
        pw = ttk.PanedWindow(parent, orient=tk.HORIZONTAL)
        pw.pack(fill=tk.BOTH, expand=True)

        # ── Left panel ────────────────────────────────────────────────────
        left = ttk.Frame(pw)
        pw.add(left, weight=1)

        # Map image loader
        img_frame = ttk.LabelFrame(left, text="Map image")
        img_frame.pack(fill=tk.X, padx=6, pady=(6, 3))
        ttk.Button(img_frame, text="Load image…",
                   command=self._map_load_image).pack(
                       fill=tk.X, padx=4, pady=(3, 1))
        ttk.Button(img_frame, text="Render BSP as background",
                   command=self._map_use_bsp_background).pack(
                       fill=tk.X, padx=4, pady=(1, 3))
        self._map_img_lbl = ttk.Label(img_frame, text="No image loaded.",
                                       foreground="#9898b8",
                                       font=("Consolas", 8), wraplength=160)
        self._map_img_lbl.pack(fill=tk.X, padx=4, pady=(0, 4))

        # Calibration
        cal_frame = ttk.LabelFrame(left, text="Calibration")
        cal_frame.pack(fill=tk.X, padx=6, pady=3)

        def cal_row(frame, label, var, row):
            ttk.Label(frame, text=label, font=("Consolas", 8),
                      foreground="#9898b8").grid(
                          row=row, column=0, sticky="w", padx=4, pady=1)
            e = ttk.Entry(frame, textvariable=var, width=10,
                          font=("Consolas", 9))
            e.grid(row=row, column=1, padx=4, pady=1)

        ttk.Label(cal_frame, text="Centre world (x, y):",
                  font=("Consolas", 8), foreground="#9898b8").grid(
                      row=0, column=0, columnspan=2, sticky="w", padx=4, pady=(4, 0))
        cal_row(cal_frame, "  world x", self._map_cal_cx, 1)
        cal_row(cal_frame, "  world y", self._map_cal_cy, 2)

        ttk.Label(cal_frame, text="Corner world (x, y):",
                  font=("Consolas", 8), foreground="#9898b8").grid(
                      row=3, column=0, columnspan=2, sticky="w", padx=4, pady=(4, 0))
        cal_row(cal_frame, "  world x", self._map_cal_wx, 4)
        cal_row(cal_frame, "  world y", self._map_cal_wy, 5)

        ttk.Label(cal_frame, text="Corner pixel (px, py):",
                  font=("Consolas", 8), foreground="#9898b8").grid(
                      row=6, column=0, columnspan=2, sticky="w", padx=4, pady=(4, 0))
        cal_row(cal_frame, "  pixel x", self._map_cal_px, 7)
        cal_row(cal_frame, "  pixel y", self._map_cal_py, 8)

        ttk.Button(cal_frame, text="Apply calibration",
                   command=self._map_redraw).grid(
                       row=9, column=0, columnspan=2,
                       sticky="ew", padx=4, pady=4)

        # Display options
        opt_frame = ttk.LabelFrame(left, text="Display")
        opt_frame.pack(fill=tk.X, padx=6, pady=3)
        ttk.Checkbutton(opt_frame, text="Show labels",
                        variable=self._map_show_labels,
                        command=self._map_redraw).pack(
                            anchor="w", padx=4, pady=2)
        ttk.Checkbutton(opt_frame, text="Active only",
                        variable=self._map_active_only,
                        command=self._refresh_map_list).pack(
                            anchor="w", padx=4, pady=2)

        # Object picker
        pick_frame = ttk.LabelFrame(left, text="Track objects")
        pick_frame.pack(fill=tk.BOTH, expand=True, padx=6, pady=3)

        pick_cols = ("idx", "type", "salt", "active", "cluster", "origin")
        self._map_pick_tree = ttk.Treeview(
            pick_frame, columns=pick_cols,
            show="headings", selectmode="browse")
        pick_col_cfg = [
            ("idx",     "Idx",    40,  tk.W),
            ("type",    "Type",   110, tk.W),
            ("salt",    "Salt",   58,  tk.W),
            ("active",  "Act",    28,  tk.CENTER),
            ("cluster", "Clust",  42,  tk.E),
            ("origin",  "Origin", 120, tk.W),
        ]
        for col, hd, w, anc in pick_col_cfg:
            self._map_pick_tree.heading(col, text=hd)
            self._map_pick_tree.column(col, width=w, anchor=anc, minwidth=20)

        for tname, color in ICON_COLORS.items():
            self._map_pick_tree.tag_configure(tname, foreground=color)
        self._map_pick_tree.tag_configure("inactive", foreground="#3a3a5a")
        self._map_pick_tree.tag_configure("tracked",
                                          foreground="#ffffff",
                                          background="#1e3a6e")

        pick_vsb = ttk.Scrollbar(pick_frame, orient=tk.VERTICAL,
                                  command=self._map_pick_tree.yview)
        self._map_pick_tree.configure(yscrollcommand=pick_vsb.set)
        self._map_pick_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        pick_vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self._map_pick_tree.bind("<Double-1>", self._map_toggle_track)
        self._map_pick_tree.bind("<Return>",   self._map_toggle_track)

        # Trail checkbox + clear button
        btn_row = ttk.Frame(left)
        btn_row.pack(fill=tk.X, padx=6, pady=3)
        self._map_trail_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(btn_row, text="Draw trail",
                        variable=self._map_trail_var).pack(side=tk.LEFT)
        ttk.Button(btn_row, text="Clear trails",
                   command=self._map_clear_trails).pack(side=tk.RIGHT)
        ttk.Button(btn_row, text="Untrack all",
                   command=self._map_untrack_all).pack(side=tk.RIGHT, padx=4)

        # ── Right panel: map canvas ────────────────────────────────────────
        right = ttk.Frame(pw)
        pw.add(right, weight=4)

        self._map_canvas = tk.Canvas(right, bg="#0d0d12",
                                     highlightthickness=0, cursor="crosshair")
        self._map_canvas.pack(fill=tk.BOTH, expand=True)
        self._map_canvas.bind("<Configure>",  lambda e: self._map_redraw())
        self._map_canvas.bind("<Motion>",     self._map_mouse_move)
        self._map_canvas.bind("<Button-1>",   self._map_mouse_click)

        # Coord readout at bottom of canvas
        self._map_coord_lbl = ttk.Label(right, text="",
                                         foreground="#9898b8",
                                         font=("Consolas", 8))
        self._map_coord_lbl.pack(fill=tk.X)

        # Draw placeholder on first show
        self._map_canvas.after(100, self._map_redraw)

    # ── Calibration helpers ────────────────────────────────────────────────

    def _map_world_to_pixel(self, wx, wy):
        """Convert world (x, y) to canvas (px, py). Returns None if not calibrated."""
        try:
            cx  = self._map_cal_cx.get()
            cy  = self._map_cal_cy.get()
            crn_wx = self._map_cal_wx.get()
            crn_wy = self._map_cal_wy.get()
            crn_px = self._map_cal_px.get()
            crn_py = self._map_cal_py.get()
        except Exception:
            return None, None

        cw = self._map_canvas.winfo_width()  or 400
        ch = self._map_canvas.winfo_height() or 400
        centre_px = cw / 2
        centre_py = ch / 2

        dx_world = crn_wx - cx
        dy_world = crn_wy - cy
        dx_pixel = crn_px - centre_px
        dy_pixel = crn_py - centre_py

        if abs(dx_world) < 1e-6 or abs(dy_world) < 1e-6:
            return None, None

        scale_x = dx_pixel / dx_world   # pixels per world unit (x)
        scale_y = dy_pixel / dy_world   # pixels per world unit (y, note Y flipped)

        # Use the average scale if x/y scales are close; otherwise use separately
        px = centre_px + (wx - cx) * scale_x
        py = centre_py - (wy - cy) * scale_y   # screen Y is inverted
        return px, py

    def _map_pixel_to_world(self, px, py):
        """Convert canvas pixel to world coord."""
        try:
            cx     = self._map_cal_cx.get()
            cy     = self._map_cal_cy.get()
            crn_wx = self._map_cal_wx.get()
            crn_wy = self._map_cal_wy.get()
            crn_px = self._map_cal_px.get()
            crn_py = self._map_cal_py.get()
        except Exception:
            return None, None

        cw = self._map_canvas.winfo_width()  or 400
        ch = self._map_canvas.winfo_height() or 400
        centre_px = cw / 2
        centre_py = ch / 2

        dx_world = crn_wx - cx
        dy_world = crn_wy - cy
        dx_pixel = crn_px - centre_px
        dy_pixel = crn_py - centre_py

        if abs(dx_pixel) < 1 or abs(dy_pixel) < 1:
            return None, None

        scale_x = dx_world / dx_pixel
        scale_y = dy_world / dy_pixel

        wx = cx + (px - centre_px) * scale_x
        wy = cy - (py - centre_py) * scale_y
        return wx, wy

    # ── Image loading ──────────────────────────────────────────────────────

    def _map_use_bsp_background(self):
        """Render BSP collision geometry to a PNG and use it as the map background.
        Also auto-calibrates the map coordinate system from BSP world bounds."""
        try:
            from PIL import Image, ImageDraw
        except ImportError:
            from tkinter import messagebox
            messagebox.showwarning(
                "Pillow required",
                "Install Pillow to render BSP background:\n  pip install Pillow")
            return

        # Get BSP geometry — prefer the section currently shown in the BSP tab,
        # fall back to the first section of whatever is cached.
        geo = getattr(self, '_bsp_geo', None)
        if geo is None:
            try:
                from ui_bsp import _bsp_cache
                if _bsp_cache:
                    sections = next(iter(_bsp_cache.values()))
                    geo = sections[0] if sections else None
            except Exception:
                pass
        if geo is None or not geo.verts:
            from tkinter import messagebox
            messagebox.showinfo(
                "No BSP loaded",
                "Load a .map file on the BSP tab first, then come back here.")
            return

        # Render size
        IMG_W, IMG_H = 1024, 1024
        PAD = 24

        wx_range = geo.xmax - geo.xmin
        wy_range = geo.ymax - geo.ymin
        if wx_range < 1 or wy_range < 1:
            return

        # Scale: fit world into (IMG_W - 2*PAD) × (IMG_H - 2*PAD) preserving aspect
        sx = (IMG_W - 2*PAD) / wx_range
        sy = (IMG_H - 2*PAD) / wy_range
        scale = min(sx, sy)

        def w2i(wx, wy):
            px = PAD + (wx - geo.xmin) * scale
            py = IMG_H - PAD - (wy - geo.ymin) * scale   # Y flip
            return px, py

        img  = Image.new("RGBA", (IMG_W, IMG_H), (13, 13, 18, 255))
        draw = ImageDraw.Draw(img)

        # Draw edges
        for (i0, i1) in geo.edges_unique:
            x0, y0, _ = geo.verts[i0]
            x1, y1, _ = geo.verts[i1]
            p0 = w2i(x0, y0)
            p1 = w2i(x1, y1)
            draw.line([p0, p1], fill=(30, 60, 120, 255), width=1)

        # Save to temp file and use as map background
        import tempfile, os
        tmp = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
        tmp.close()
        img.save(tmp.name)

        self._map_image_path = tmp.name
        self._map_img_lbl.config(text=f"BSP geometry ({geo.map_name})")

        # Auto-calibrate: world centre at image centre, corner at top-right pixel
        cx_world = (geo.xmin + geo.xmax) / 2
        cy_world = (geo.ymin + geo.ymax) / 2
        self._map_cal_cx.set(round(cx_world, 2))
        self._map_cal_cy.set(round(cy_world, 2))

        # Corner = top-right of image (pixel PAD, IMG_H-PAD from top = geo.ymin)
        crn_wx = geo.xmin
        crn_wy = geo.ymax
        crn_px, crn_py = w2i(crn_wx, crn_wy)
        self._map_cal_wx.set(round(crn_wx, 2))
        self._map_cal_wy.set(round(crn_wy, 2))
        self._map_cal_px.set(round(crn_px, 2))
        self._map_cal_py.set(round(crn_py, 2))

        self._map_redraw()

    def _map_load_image(self):
        path = filedialog.askopenfilename(
            title="Select map image",
            filetypes=[("PNG images", "*.png"),
                       ("All images", "*.png *.jpg *.bmp"),
                       ("All files", "*.*")])
        if not path:
            return
        if not HAS_PIL:
            messagebox.showwarning(
                "Pillow not installed",
                "Install Pillow to use image files:\n  pip install Pillow\n\n"
                "A placeholder will be shown instead.")
            return
        self._map_image_path = path
        short = path.replace("\\", "/").split("/")[-1]
        self._map_img_lbl.config(text=short)
        self._map_redraw()

    def _map_load_photo(self, w, h):
        """Load and scale the map image to fit the canvas. Returns ImageTk or None."""
        if not HAS_PIL or not self._map_image_path:
            return None
        try:
            img = Image.open(self._map_image_path).convert("RGBA")
            img = img.resize((w, h), Image.LANCZOS)
            self._map_photo = ImageTk.PhotoImage(img)
            return self._map_photo
        except Exception as e:
            self._map_img_lbl.config(text=f"Load error: {e}")
            return None

    # ── Tracking ───────────────────────────────────────────────────────────

    def _map_toggle_track(self, _event=None):
        sel = self._map_pick_tree.selection()
        if not sel:
            return
        try:
            idx = int(sel[0])
        except ValueError:
            return

        if idx in self._map_tracked:
            del self._map_tracked[idx]
        else:
            self._map_tracked[idx] = {"trail": []}

        # Refresh row tag to show tracked state
        if self._map_pick_tree.exists(str(idx)):
            obj = next((o for o in self._objects if o.get("index") == idx), None)
            if obj:
                base_tag = obj.get("type", "biped")
                tags = ("tracked",) if idx in self._map_tracked else (base_tag,)
                self._map_pick_tree.item(str(idx), tags=tags)

    def _map_clear_trails(self):
        for v in self._map_tracked.values():
            v["trail"].clear()

    def _map_untrack_all(self):
        self._map_tracked.clear()
        self._refresh_map_list()

    # ── Object picker list ─────────────────────────────────────────────────

    def _refresh_map_list(self):
        """Update the map picker tree in-place (no scroll jump)."""
        tree        = self._map_pick_tree
        active_only = self._map_active_only.get()
        wanted      = {}

        for o in self._objects:
            idx        = o.get("index", "?")
            typ        = o.get("type", "?")
            salt       = o.get("salt", 0)
            is_active  = o.get("active", False)
            is_tracked = idx in self._map_tracked

            if active_only and not is_active and not is_tracked:
                continue

            active   = "✓" if is_active else ""
            clust    = str(o.get("cluster", "?"))
            orig     = o.get("origin")
            orig_str = (f"({orig[0]:7.1f},{orig[1]:7.1f})"
                        if orig and orig[0] is not None else "—")
            if is_tracked:
                tags = ("tracked",)
            elif is_active:
                tags = (typ,)
            else:
                tags = ("inactive",)
            vals = (idx, make_display_type(o), f"0x{salt:04X}",
                    active, clust, orig_str)
            wanted[str(idx)] = (vals, tags)

        existing = set(tree.get_children(""))

        # Remove stale rows
        for iid in existing - wanted.keys():
            tree.delete(iid)

        # Update or insert
        for iid, (vals, tags) in wanted.items():
            if tree.exists(iid):
                tree.item(iid, values=vals, tags=tags)
            else:
                tree.insert("", tk.END, iid=iid, values=vals, tags=tags)
    def _map_redraw(self):
        c  = self._map_canvas
        cw = c.winfo_width()  or 400
        ch = c.winfo_height() or 400

        # Clear previous frame's drawn items (keep bg separate)
        for iid in self._map_drawn_ids:
            c.delete(iid)
        self._map_drawn_ids = []

        # Background: real image or placeholder
        if self._map_bg_id:
            c.delete(self._map_bg_id)
            self._map_bg_id = None

        photo = self._map_load_photo(cw, ch)
        if photo:
            self._map_bg_id = c.create_image(0, 0, anchor="nw", image=photo)
        else:
            self._map_bg_id = self._map_draw_placeholder(cw, ch)

        # Centre crosshair
        cx_px, cy_px = cw // 2, ch // 2
        self._map_drawn_ids += [
            c.create_line(cx_px - 12, cy_px, cx_px + 12, cy_px,
                          fill="#2a2a4a", dash=(2, 4)),
            c.create_line(cx_px, cy_px - 12, cx_px, cy_px + 12,
                          fill="#2a2a4a", dash=(2, 4)),
        ]

        # Update trails from current objects
        show_trail = self._map_trail_var.get()
        for o in self._objects:
            idx  = o.get("index")
            orig = o.get("origin") or (None, None, None)
            if idx not in self._map_tracked or orig[0] is None:
                continue
            px, py = self._map_world_to_pixel(orig[0], orig[1])
            if px is None:
                continue
            trail_data = self._map_tracked[idx]["trail"]
            trail_data.append((px, py))
            if len(trail_data) > self._map_trail_len:
                del trail_data[0]

        # Draw tracked objects
        show_labels = self._map_show_labels.get()
        for o in self._objects:
            idx  = o.get("index")
            if idx not in self._map_tracked:
                continue
            orig = o.get("origin") or (None, None, None)
            if orig[0] is None:
                continue
            px, py = self._map_world_to_pixel(orig[0], orig[1])
            if px is None:
                continue
            # Clip to canvas bounds
            if not (0 <= px <= cw and 0 <= py <= ch):
                continue

            trail = self._map_tracked[idx]["trail"] if show_trail else None
            label = str(idx) if show_labels else ""
            ids   = _draw_icon(c, int(px), int(py),
                                o.get("type", "biped"),
                                label=label, trail=trail)
            self._map_drawn_ids += ids

        c.tag_raise("trail")   # trails below icons

    def _map_draw_placeholder(self, w, h):
        """Draw a simple grid placeholder when no image is loaded."""
        c = self._map_canvas
        # Background rect
        bg = c.create_rectangle(0, 0, w, h, fill="#0a0a14", outline="")
        # Grid lines
        spacing = 50
        for x in range(0, w, spacing):
            c.create_line(x, 0, x, h, fill="#141428", width=1)
        for y in range(0, h, spacing):
            c.create_line(0, y, w, y, fill="#141428", width=1)
        # Border
        c.create_rectangle(2, 2, w-2, h-2, outline="#1c1c3a", width=1)
        # Centre label
        c.create_text(w//2, h//2 - 10,
                      text="No map image loaded",
                      fill="#2a2a5a", font=("Consolas", 12))
        c.create_text(w//2, h//2 + 8,
                      text="Load a PNG via the panel on the left",
                      fill="#1e1e40", font=("Consolas", 9))
        return bg

    # ── Mouse interaction ──────────────────────────────────────────────────

    def _map_mouse_move(self, event):
        wx, wy = self._map_pixel_to_world(event.x, event.y)
        if wx is not None:
            self._map_coord_lbl.config(
                text=f"  pixel ({event.x}, {event.y})   "
                     f"world ({wx:.2f}, {wy:.2f})")
        else:
            self._map_coord_lbl.config(
                text=f"  pixel ({event.x}, {event.y})   "
                     f"(calibrate to see world coords)")

    def _map_mouse_click(self, event):
        """Click on canvas: if near a tracked object, select it in picker."""
        threshold = 14
        best_dist = threshold + 1
        best_idx  = None
        for o in self._objects:
            idx  = o.get("index")
            if idx not in self._map_tracked:
                continue
            orig = o.get("origin") or (None, None, None)
            if orig[0] is None:
                continue
            px, py = self._map_world_to_pixel(orig[0], orig[1])
            if px is None:
                continue
            dist = math.sqrt((event.x - px)**2 + (event.y - py)**2)
            if dist < best_dist:
                best_dist = dist
                best_idx  = idx
        if best_idx is not None and self._map_pick_tree.exists(str(best_idx)):
            self._map_pick_tree.selection_set(str(best_idx))
            self._map_pick_tree.see(str(best_idx))

    # ── Called by App._poll each tick ─────────────────────────────────────

    def _map_tick(self):
        """Called each poll tick to update the map if the tab is visible."""
        try:
            tab = self._main_nb.index(self._main_nb.select())
            if tab == 2:   # Map is the third top-level tab (0=Objects, 1=AUP, 2=Map)
                self._refresh_map_list()
                self._map_redraw()
        except Exception:
            pass
