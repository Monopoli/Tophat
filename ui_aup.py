"""Halo 2 Xbox Object Monitor — AUP tab mixin."""
import struct
import tkinter as tk
from tkinter import ttk, messagebox
from constants import AUP_ADDR, TYPE_COLORS
from ui_objects import make_display_type


class AupMixin:
    """AUP tab: select a biped/vehicle and write its datum to memory."""

    def _build_aup_panel(self, parent):
        """Build the AUP tab: biped/vehicle list + Apply AUP button."""
        # ── Description ───────────────────────────────────────────────────
        desc = ttk.Frame(parent)
        desc.pack(fill=tk.X, padx=12, pady=(10, 6))
        ttk.Label(desc,
                  text="Select a biped or vehicle and press Apply AUP to write its",
                  foreground="#9898b8", font=("Consolas", 9)).pack(anchor="w")
        ttk.Label(desc,
                  text=f"salt + slot index to 0x{AUP_ADDR:08X}.",
                  foreground="#9898b8", font=("Consolas", 9)).pack(anchor="w")

        # ── Unit list ─────────────────────────────────────────────────────
        list_frame = ttk.Frame(parent)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 6))

        aup_cols = ("idx", "type", "salt", "active", "origin", "health", "shields")
        self._aup_tree = ttk.Treeview(list_frame, columns=aup_cols,
                                      show="headings", selectmode="browse")
        aup_col_cfg = [
            ("idx",     "Idx",              60,  tk.W),
            ("type",    "Type",             110, tk.W),
            ("salt",    "Salt",             70,  tk.W),
            ("active",  "Act",              36,  tk.CENTER),
            ("origin",  "Origin (x, y, z)", 220, tk.W),
            ("health",  "HP",               50,  tk.CENTER),
            ("shields", "SH",               50,  tk.CENTER),
        ]
        for col, heading, width, anchor in aup_col_cfg:
            self._aup_tree.heading(col, text=heading)
            self._aup_tree.column(col, width=width, anchor=anchor, minwidth=30)

        aup_vsb = ttk.Scrollbar(list_frame, orient=tk.VERTICAL,
                                 command=self._aup_tree.yview)
        self._aup_tree.configure(yscrollcommand=aup_vsb.set)
        self._aup_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        aup_vsb.pack(side=tk.RIGHT, fill=tk.Y)

        # Row colour tags
        for tname, color in TYPE_COLORS.items():
            self._aup_tree.tag_configure(tname, foreground=color)
        self._aup_tree.tag_configure("inactive", foreground="#3a3a5a")
        self._aup_tree.bind("<<TreeviewSelect>>", self._on_aup_select)
        self._aup_tree.bind("<Up>",   lambda e: self.after(0, self._on_aup_select))
        self._aup_tree.bind("<Down>", lambda e: self.after(0, self._on_aup_select))

        # ── Bottom control row ─────────────────────────────────────────────
        ctrl = ttk.Frame(parent)
        ctrl.pack(fill=tk.X, padx=12, pady=(0, 10))

        self._aup_status_lbl = ttk.Label(ctrl, text="No unit selected.",
                                          foreground="#9898b8",
                                          font=("Consolas", 10))
        self._aup_status_lbl.pack(side=tk.LEFT)

        self._aup_btn = ttk.Button(ctrl, text="Apply AUP",
                                   command=self._apply_aup, state=tk.DISABLED,
                                   width=14)
        self._aup_btn.pack(side=tk.RIGHT)

        # Track selected AUP object
        self._aup_selected_index: int | None = None

    def _on_aup_select(self, _event=None):
        sel = self._aup_tree.selection()
        if not sel:
            return
        try:
            idx = int(sel[0])
        except ValueError:
            return
        self._aup_selected_index = idx
        obj = next((o for o in self._objects if o.get("index") == idx), None)
        if obj:
            salt = obj.get("salt", 0)
            typ  = obj.get("type", "?")
            self._aup_status_lbl.config(
                text=f"Selected: [{idx:04d}:{salt:04X}]  {make_display_type(obj)}  "
                     f"→ will write salt=0x{salt:04X}  idx=0x{idx:04X}")
            self._aup_btn.config(state=tk.NORMAL)
        else:
            self._aup_selected_index = None
            self._aup_btn.config(state=tk.DISABLED)

    def _apply_aup(self):
        """Write salt (2 bytes) + slot index (2 bytes) to AUP_ADDR."""
        if self._aup_selected_index is None:
            messagebox.showwarning("AUP", "No unit selected.")
            return
        if not self._mem:
            messagebox.showerror("AUP", "Not connected to process.")
            return

        obj = next((o for o in self._objects
                    if o.get("index") == self._aup_selected_index), None)
        if not obj:
            messagebox.showerror("AUP", "Selected object no longer exists.")
            return

        salt  = obj.get("salt", 0)   # uint16
        idx   = obj.get("index", 0)  # uint16 slot

        # Pack as little-endian: [salt_lo, salt_hi, idx_lo, idx_hi]
        payload = struct.pack("<HH", idx, salt)

        ok = self._mem.write_bytes(AUP_ADDR, payload)
        if ok:
            self._aup_status_lbl.config(
                text=f"✓ Written  salt=0x{salt:04X}  idx=0x{idx:04X}  "
                     f"→ 0x{AUP_ADDR:08X}",
                foreground="#3dcc96")
        else:
            err = kernel32.GetLastError()
            self._aup_status_lbl.config(
                text=f"✗ Write failed  (WinError {err})",
                foreground="#f07878")

    def _refresh_aup_list(self):
        """Update the AUP tree in-place (no delete/reinsert = no scroll jump)."""
        tree    = self._aup_tree
        wanted  = {}

        for o in self._objects:
            typ = o.get("type", "")
            if typ not in ("biped", "vehicle"):
                continue
            idx    = o.get("index", "?")
            salt   = o.get("salt", 0)
            active = "✓" if o.get("active") else ""
            orig   = o.get("origin")
            orig_str = (f"({orig[0]:8.2f}, {orig[1]:8.2f}, {orig[2]:8.2f})"
                        if orig and orig[0] is not None else "—")
            hp = o.get("health")
            sh = o.get("shields")
            hp_str = f"{hp:.2f}" if hp is not None else "—"
            sh_str = f"{sh:.2f}" if sh is not None else "—"
            tag    = typ if o.get("active") else "inactive"
            vals   = (idx, make_display_type(o), f"0x{salt:04X}", active,
                      orig_str, hp_str, sh_str)
            wanted[str(idx)] = (vals, (tag,))

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

