"""Halo 2 Xbox Object Monitor — object table mixin."""
import os
import tkinter as tk
from tkinter import ttk
from constants import TYPE_COLORS

try:
    from PIL import Image, ImageDraw, ImageTk
    _PIL_OK = True
except ImportError:
    _PIL_OK = False

# ── Thumbnail grid geometry ────────────────────────────────────────────────
THUMB_W   = 96
THUMB_H   = 72
CELL_PAD  = 4
CELL_W    = THUMB_W + CELL_PAD * 2
CELL_H    = THUMB_H + 22          # thumb + label row
EMPTY_CLR = '#16161f'
ACTIVE_BORDER = '#2e2e48'
EMPTY_BORDER  = '#1e1e2a'

# ── Larger thumbnail used by the Objects-tab detail panel (above HP/Shield
#    bars) — same 4:3 ratio as the grid thumbnail, just bigger ─────────────
DETAIL_THUMB_W = 144
DETAIL_THUMB_H = 108


def make_display_type(o: dict) -> str:
    """Return 'type:tagname' if a resolved tag suffix is available, else just 'type'."""
    typ      = o.get("type", "?")
    def_hint = o.get("definition_tag", "") or ""
    sfx      = def_hint.split("]")[-1].strip() if def_hint and "]" in def_hint else ""
    return (typ + ":" + sfx) if sfx else typ


def _tag_to_image_path(definition_tag: str) -> str | None:
    """
    Map a definition_tag like '[bipd] masterchief'
    to 'CairoImages/masterchief.png'.
    Falls back to None if definition_tag is empty or no image exists.
    """
    if not definition_tag:
        return None
    # Extract short name: '[bipd] masterchief' → 'masterchief'
    short = definition_tag.split("]")[-1].strip() if "]" in definition_tag else definition_tag
    # The short name may be a path like 'levels\b30\masterchief' — take only the leaf
    leaf = short.replace("\\", "/").rsplit("/", 1)[-1]
    return os.path.join("CairoImages", leaf + ".png")


class ObjectTableMixin:
    """Object list table: filtering, population, sorting, and grid view."""

    # ── Called once from app.py _build_ui, before the tree is built ───────
    def _init_grid_state(self):
        self._obj_view        = tk.StringVar(value="table")
        self._obj_img_cache   = {}       # definition_tag → PhotoImage
        self._obj_placeholder = None     # lazily created
        self._obj_canvas      = None
        self._obj_canvas_vsb  = None
        self._obj_grid_frame  = None     # frame holding canvas + scrollbar
        # Larger variant for the detail-panel thumbnail (separate cache so
        # it doesn't collide with / resize the grid-view's 96×72 images)
        self._obj_img_cache_large   = {}
        self._obj_placeholder_large = None

    # ── Filter / populate (table view) ────────────────────────────────────

    def _apply_filter(self, *_):
        active = self._filter_active.get()
        query  = self._search_var.get().lower().strip()

        # Build set of enabled types from checkboxes
        type_vars = getattr(self, "_type_vars", None)
        if type_vars:
            enabled_types = {t for t, v in type_vars.items() if v.get()}
        else:
            # Fallback: legacy single-type combobox
            ftype = self._filter_type.get()
            enabled_types = None  # None means "all"

        filtered = []
        for o in self._objects:
            obj_type = o.get("type")
            if type_vars:
                if obj_type not in enabled_types:
                    continue
            else:
                if ftype != "all" and obj_type != ftype:
                    continue
            if active and not o.get("active"):
                continue
            if query:
                haystack = (
                    f"{o.get('index')} {o.get('type')} "
                    f"{o.get('addr', 0):08X} {o.get('salt', 0):04X} "
                    f"{o.get('cluster')} {o.get('placement_idx')}"
                ).lower()
                if query not in haystack:
                    continue
            filtered.append(o)

        self._populate_tree(filtered)

        # Keep grid in sync if it's visible
        if self._obj_view.get() == "grid":
            self._obj_grid_redraw(filtered)

    def _row_values(self, o):
        """Compute the tuple of column values for one object."""
        idx      = o.get("index", "?")
        typ          = o.get("type", "?")
        display_type = make_display_type(o)
        act   = "✓" if o.get("active") else ""
        clust = str(o.get("cluster", "?"))
        addr  = f"0x{o.get('addr', 0):08X}"

        orig = o.get("origin")
        if orig and orig[0] is not None:
            ox, oy, oz = orig
            orig_str = f"({ox:8.2f}, {oy:8.2f}, {oz:8.2f})"
        else:
            orig_str = "—"

        hp  = o.get("health")
        sh  = o.get("shields")
        hp_str = f"{hp:.2f}" if hp is not None else "—"
        sh_str = f"{sh:.2f}" if sh is not None else "—"

        spd = o.get("speed")
        spd_str = f"{spd:.3f}" if spd is not None else "—"

        dm = o.get("pos_delta_mag")
        if dm is None:
            delta_str = "—"
        elif o.get("teleported"):
            delta_str = f"!{dm:.2f}"
        else:
            delta_str = f"{dm:.3f}"

        hflags = o.get("flags", 0)
        flag_abbrs = []
        if hflags & 0x01: flag_abbrs.append("A")
        if hflags & 0x08: flag_abbrs.append("D")
        if hflags & 0x20: flag_abbrs.append("C")
        if hflags & 0x40: flag_abbrs.append("ch")
        flags_str = "".join(flag_abbrs) or "·"

        return (idx, display_type, act, clust, addr, orig_str,
                hp_str, sh_str, spd_str, delta_str, flags_str)

    def _row_tag(self, o):
        idx = o.get("index")
        typ = o.get("type", "?")
        if idx in self._pinned:
            return "pinned"
        if o.get("teleported"):
            return "teleport"
        if not o.get("active"):
            return "inactive"
        return typ if typ in TYPE_COLORS else "inactive"

    def _populate_tree(self, objects):
        """Update the tree in-place: add new rows, update changed rows,
        remove stale rows — without touching scroll position or focus."""
        tree = self._tree

        # Build index of what should be visible
        wanted = {str(o.get("index")): o for o in objects}
        existing = set(tree.get_children(""))

        # Remove rows no longer in the filtered set
        to_remove = existing - wanted.keys()
        for iid in to_remove:
            tree.delete(iid)

        # Update or insert rows, preserving order
        prev = ""
        for o in objects:
            iid  = str(o.get("index"))
            vals = self._row_values(o)
            tag  = self._row_tag(o)

            if tree.exists(iid):
                tree.item(iid, values=vals, tags=(tag,))
                tree.move(iid, "", "end" if prev == "" else prev)
            else:
                tree.insert("", "end", iid=iid, values=vals, tags=(tag,))

            prev = iid

    def _sort_by(self, col):
        data = [(self._tree.set(iid, col), iid)
                for iid in self._tree.get_children("")]
        try:
            data.sort(key=lambda x: float(
                x[0].replace("✓", "1").replace("—", "0")
                    .replace("0x", "0").replace("!", "")) if x[0] else 0)
        except ValueError:
            data.sort()
        for i, (_, iid) in enumerate(data):
            self._tree.move(iid, "", i)

    # ── View toggle ────────────────────────────────────────────────────────

    def _obj_toggle_view(self):
        if self._obj_view.get() == "table":
            self._obj_view.set("grid")
            self._obj_toggle_btn.config(text="☰ Table")
            self._obj_tree_frame.pack_forget()
            self._obj_ensure_grid_frame()
            self._obj_grid_frame.pack(fill=tk.BOTH, expand=True)
            # Draw immediately with whatever objects are currently filtered
            self._apply_filter()
        else:
            self._obj_view.set("table")
            self._obj_toggle_btn.config(text="⊞ Grid")
            if self._obj_grid_frame:
                self._obj_grid_frame.pack_forget()
            self._obj_tree_frame.pack(fill=tk.BOTH, expand=True)

    def _obj_ensure_grid_frame(self):
        """Lazily create the canvas + scrollbar frame."""
        if self._obj_grid_frame is not None:
            return
        parent = self._obj_tree_frame.master   # same parent as the tree frame
        self._obj_grid_frame = tk.Frame(parent, bg="#0d0d12")

        vsb = ttk.Scrollbar(self._obj_grid_frame, orient=tk.VERTICAL)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)

        self._obj_canvas = tk.Canvas(
            self._obj_grid_frame,
            bg="#0d0d12",
            highlightthickness=0,
            yscrollcommand=vsb.set,
        )
        vsb.config(command=self._obj_canvas.yview)
        self._obj_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self._obj_canvas.bind("<Configure>", lambda e: self._apply_filter())
        self._obj_canvas.bind("<Button-1>", self._obj_grid_on_click)
        self._obj_canvas.bind(
            "<MouseWheel>",
            lambda e: self._obj_canvas.yview_scroll(-1 if e.delta > 0 else 1, "units")
        )
        self._obj_canvas.bind(
            "<Button-4>",
            lambda e: self._obj_canvas.yview_scroll(-1, "units")
        )
        self._obj_canvas.bind(
            "<Button-5>",
            lambda e: self._obj_canvas.yview_scroll(1, "units")
        )

    # ── Grid click ─────────────────────────────────────────────────────────

    def _obj_grid_on_click(self, event):
        """Convert a canvas click to an object index and fire the detail panel."""
        c = self._obj_canvas
        if c is None:
            return
        # Canvas coords account for scroll offset
        cx = c.canvasx(event.x)
        cy = c.canvasy(event.y)

        cw   = c.winfo_width() or 600
        cols = max(1, cw // CELL_W)

        col = int(cx // CELL_W)
        row = int(cy // CELL_H)
        slot = row * cols + col

        # Find matching object
        obj = next((o for o in self._objects if o.get("index") == slot), None)
        if obj is None:
            return

        # Set selection state (same as _on_select does for the treeview)
        idx = obj.get("index")
        self._selected_index = idx
        self._pin_btn.config(text="📌 Unpin" if idx in self._pinned else "📌 Pin")

        if idx not in self._pinned:
            self._show_detail(obj)

        tab = self._detail_nb.index(self._detail_nb.select())
        if tab == 1:
            self._redraw_history()
        elif tab == 2:
            self._update_alert_tab()

        # Redraw grid to show selection highlight
        self._apply_filter()

    # ── Grid rendering ─────────────────────────────────────────────────────

    def _obj_grid_redraw(self, objects):
        """Render the thumbnail grid from the current filtered object list."""
        c = self._obj_canvas
        if c is None:
            return
        c.delete("all")

        if not objects:
            c.create_text(
                12, 12, anchor="nw",
                fill="#3a3a5a",
                font=("Consolas", 10),
                text="No objects match the current filter.",
            )
            c.configure(scrollregion=(0, 0, 100, 40))
            return

        # Build slot map: object index (lower 16 bits) → object
        slot_map = {o.get("index", 0): o for o in objects}
        if not slot_map:
            return

        max_slot = max(slot_map.keys())
        cw = c.winfo_width() or 600
        cols = max(1, cw // CELL_W)
        placeholder = self._obj_get_placeholder()

        for slot in range(max_slot + 1):
            col = slot % cols
            row = slot // cols
            x0  = col * CELL_W + CELL_PAD
            y0  = row * CELL_H + CELL_PAD

            if slot in slot_map:
                obj = slot_map[slot]
                def_tag  = obj.get("definition_tag", "") or ""
                obj_type = obj.get("type", "?")
                # Short label: tag leaf name, or type as fallback
                if "]" in def_tag:
                    leaf = def_tag.split("]")[-1].strip().rsplit("\\", 1)[-1]
                else:
                    leaf = obj_type
                label = leaf[:13]

                type_color = TYPE_COLORS.get(obj_type, "#9898b8")
                img = self._obj_get_thumb(def_tag)

                # Cell background — highlight if selected
                is_selected = (slot == self._selected_index)
                border_color = "#ffffff" if is_selected else type_color
                border_width = 2 if is_selected else 1
                c.create_rectangle(
                    x0, y0, x0 + THUMB_W, y0 + THUMB_H,
                    fill="#1c1c28", outline=border_color, width=border_width,
                )
                # Thumbnail (placeholder or real image)
                c.create_image(x0, y0, anchor="nw", image=img)
                # Type colour strip along top edge
                c.create_rectangle(
                    x0, y0, x0 + THUMB_W, y0 + 3,
                    fill=type_color, outline="",
                )
                # Label below thumb
                c.create_text(
                    x0 + THUMB_W // 2, y0 + THUMB_H + 2,
                    anchor="n",
                    fill="#c8c8e0",
                    font=("Consolas", 7),
                    text=label,
                )
                # Slot index chip (top-left corner)
                c.create_text(
                    x0 + 3, y0 + 5,
                    anchor="nw",
                    fill="#606080",
                    font=("Consolas", 7),
                    text=str(slot),
                )
            else:
                # Empty slot
                c.create_rectangle(
                    x0, y0, x0 + THUMB_W, y0 + THUMB_H,
                    fill=EMPTY_CLR, outline=EMPTY_BORDER, width=1,
                )
                c.create_text(
                    x0 + THUMB_W // 2, y0 + THUMB_H // 2,
                    anchor="center",
                    fill="#1e1e30",
                    font=("Consolas", 8),
                    text=str(slot),
                )

        total_rows = (max_slot // cols) + 1
        total_h    = total_rows * CELL_H + CELL_PAD * 2
        c.configure(scrollregion=(0, 0, cw, total_h))

    # ── Image helpers ──────────────────────────────────────────────────────

    def _obj_get_thumb(self, definition_tag: str):
        """Return a PhotoImage for this tag, loading from disk or placeholder."""
        if definition_tag in self._obj_img_cache:
            return self._obj_img_cache[definition_tag]

        img = None
        path = _tag_to_image_path(definition_tag)
        if path and _PIL_OK and os.path.isfile(path):
            try:
                pil = Image.open(path).convert("RGBA").resize(
                    (THUMB_W, THUMB_H), Image.LANCZOS
                )
                img = ImageTk.PhotoImage(pil)
            except Exception:
                img = None

        if img is None:
            img = self._obj_get_placeholder()

        self._obj_img_cache[definition_tag] = img
        return img

    def _obj_get_placeholder(self):
        """Lazily create and return the placeholder PhotoImage."""
        if self._obj_placeholder is not None:
            return self._obj_placeholder

        if _PIL_OK:
            pil = Image.new("RGB", (THUMB_W, THUMB_H), color=(22, 22, 32))
            draw = ImageDraw.Draw(pil)
            # Dashed border
            dash_clr = (40, 40, 60)
            for x in range(0, THUMB_W, 8):
                draw.rectangle([x, 0, min(x + 4, THUMB_W - 1), 0], fill=dash_clr)
                draw.rectangle([x, THUMB_H - 1, min(x + 4, THUMB_W - 1), THUMB_H - 1], fill=dash_clr)
            for y in range(0, THUMB_H, 8):
                draw.rectangle([0, y, 0, min(y + 4, THUMB_H - 1)], fill=dash_clr)
                draw.rectangle([THUMB_W - 1, y, THUMB_W - 1, min(y + 4, THUMB_H - 1)], fill=dash_clr)
            # Crossed diagonals
            draw.line([(6, 6), (THUMB_W - 6, THUMB_H - 6)], fill=(35, 35, 55), width=1)
            draw.line([(THUMB_W - 6, 6), (6, THUMB_H - 6)], fill=(35, 35, 55), width=1)
            self._obj_placeholder = ImageTk.PhotoImage(pil)
        else:
            # No Pillow — use a 1×1 transparent image; cell bg colour is the visual
            self._obj_placeholder = tk.PhotoImage(width=1, height=1)

        return self._obj_placeholder

    # ── Larger variant, used by the Objects-tab detail panel ───────────────
    # (kept separate from _obj_get_thumb/_obj_get_placeholder above so the
    # grid view's 96×72 cells are completely unaffected by this size.)

    def _obj_get_thumb_large(self, definition_tag: str):
        """Return a larger PhotoImage for the detail panel, loading from disk or placeholder."""
        if definition_tag in self._obj_img_cache_large:
            return self._obj_img_cache_large[definition_tag]

        img = None
        path = _tag_to_image_path(definition_tag)
        if path and _PIL_OK and os.path.isfile(path):
            try:
                pil = Image.open(path).convert("RGBA").resize(
                    (DETAIL_THUMB_W, DETAIL_THUMB_H), Image.LANCZOS
                )
                img = ImageTk.PhotoImage(pil)
            except Exception:
                img = None

        if img is None:
            img = self._obj_get_placeholder_large()

        self._obj_img_cache_large[definition_tag] = img
        return img

    def _obj_get_placeholder_large(self):
        """Lazily create and return the larger placeholder PhotoImage."""
        if self._obj_placeholder_large is not None:
            return self._obj_placeholder_large

        if _PIL_OK:
            pil = Image.new("RGB", (DETAIL_THUMB_W, DETAIL_THUMB_H), color=(22, 22, 32))
            draw = ImageDraw.Draw(pil)
            # Dashed border
            dash_clr = (40, 40, 60)
            for x in range(0, DETAIL_THUMB_W, 8):
                draw.rectangle([x, 0, min(x + 4, DETAIL_THUMB_W - 1), 0], fill=dash_clr)
                draw.rectangle([x, DETAIL_THUMB_H - 1, min(x + 4, DETAIL_THUMB_W - 1), DETAIL_THUMB_H - 1], fill=dash_clr)
            for y in range(0, DETAIL_THUMB_H, 8):
                draw.rectangle([0, y, 0, min(y + 4, DETAIL_THUMB_H - 1)], fill=dash_clr)
                draw.rectangle([DETAIL_THUMB_W - 1, y, DETAIL_THUMB_W - 1, min(y + 4, DETAIL_THUMB_H - 1)], fill=dash_clr)
            # Crossed diagonals
            draw.line([(6, 6), (DETAIL_THUMB_W - 6, DETAIL_THUMB_H - 6)], fill=(35, 35, 55), width=1)
            draw.line([(DETAIL_THUMB_W - 6, 6), (6, DETAIL_THUMB_H - 6)], fill=(35, 35, 55), width=1)
            self._obj_placeholder_large = ImageTk.PhotoImage(pil)
        else:
            # No Pillow — use a 1×1 transparent image; label bg colour is the visual
            self._obj_placeholder_large = tk.PhotoImage(width=1, height=1)

        return self._obj_placeholder_large
