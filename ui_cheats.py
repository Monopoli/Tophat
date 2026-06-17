"""Halo 2 Xbox Object Monitor — Cheats tab mixin.

Misc live object manipulation: teleport a unit (manual coordinates or to
another object's position), set its velocity (forward-direction boost or
a raw vector), and set its health/shields. All writes go through
MemoryReader.write_bytes() at obj_addr + OBJ_*_OFF, the same per-object
field offsets parser.py reads (see constants.py) — so this tab can only
touch fields parser.py can already see.
"""
import math
import struct
import tkinter as tk
from tkinter import ttk, messagebox

from constants import (
    TYPE_COLORS, OBJ_ORIGIN_OFF, OBJ_TRANS_VEL_OFF,
    OBJ_HEALTH_OFF, OBJ_SHIELDS_OFF,
)
from ui_objects import make_display_type

# Object types selectable as the thing being cheated on. Any live object
# (including this list's targets) can still be used as a teleport *target*.
CHEAT_UNIT_TYPES = ("biped", "vehicle")
DEFAULT_BOOST_SPEED = 40.0


class CheatsMixin:
    """Cheats tab: teleport and speed manipulation for tracked units."""

    # ── UI construction ────────────────────────────────────────────────

    def _build_cheats_panel(self, parent):
        desc = ttk.Frame(parent)
        desc.pack(fill=tk.X, padx=12, pady=(10, 6))
        ttk.Label(desc,
                  text="Select a biped or vehicle, then teleport it, set its velocity, "
                       "or adjust health/shields.",
                  foreground="#9898b8", font=("Consolas", 9)).pack(anchor="w")
        ttk.Label(desc,
                  text="Writes go straight to live game memory — undo by re-teleporting "
                       "or applying Stop.",
                  foreground="#9898b8", font=("Consolas", 9)).pack(anchor="w")

        body = ttk.Frame(parent)
        body.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 4))

        # ── Left: unit picker ────────────────────────────────────────
        left = ttk.Frame(body)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        cheat_cols = ("idx", "type", "active", "origin", "speed", "health", "shields")
        self._cheats_tree = ttk.Treeview(left, columns=cheat_cols,
                                         show="headings", selectmode="browse")
        cheat_col_cfg = [
            ("idx",     "Idx",              50,  tk.W),
            ("type",    "Type",             110, tk.W),
            ("active",  "Act",              34,  tk.CENTER),
            ("origin",  "Origin (x, y, z)", 200, tk.W),
            ("speed",   "|v|",              60,  tk.E),
            ("health",  "HP",               50,  tk.CENTER),
            ("shields", "SH",               50,  tk.CENTER),
        ]
        for col, heading, width, anchor in cheat_col_cfg:
            self._cheats_tree.heading(col, text=heading)
            self._cheats_tree.column(col, width=width, anchor=anchor, minwidth=30)

        cheats_vsb = ttk.Scrollbar(left, orient=tk.VERTICAL,
                                    command=self._cheats_tree.yview)
        self._cheats_tree.configure(yscrollcommand=cheats_vsb.set)
        self._cheats_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        cheats_vsb.pack(side=tk.RIGHT, fill=tk.Y)

        for tname, color in TYPE_COLORS.items():
            self._cheats_tree.tag_configure(tname, foreground=color)
        self._cheats_tree.tag_configure("inactive", foreground="#3a3a5a")
        self._cheats_tree.bind("<<TreeviewSelect>>", self._on_cheats_select)
        self._cheats_tree.bind("<Up>",   lambda e: self.after(0, self._on_cheats_select))
        self._cheats_tree.bind("<Down>", lambda e: self.after(0, self._on_cheats_select))

        # ── Right: action panel ──────────────────────────────────────
        right = ttk.Frame(body, width=320)
        right.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))

        self._cheats_sel_lbl = ttk.Label(right, text="No unit selected.",
                                          foreground="#9898b8", font=("Consolas", 9),
                                          wraplength=300, justify=tk.LEFT)
        self._cheats_sel_lbl.pack(anchor="w", pady=(0, 8))

        def coord_row(parent_, label, var):
            row = ttk.Frame(parent_)
            row.pack(fill=tk.X, padx=6, pady=2)
            ttk.Label(row, text=label, width=3).pack(side=tk.LEFT)
            ttk.Entry(row, textvariable=var, width=14).pack(side=tk.LEFT)

        # ── Teleport group ──────────────────────────────────────────
        tp = ttk.LabelFrame(right, text="Teleport")
        tp.pack(fill=tk.X, pady=(0, 8))

        self._cheats_x_var = tk.StringVar(value="0.000")
        self._cheats_y_var = tk.StringVar(value="0.000")
        self._cheats_z_var = tk.StringVar(value="0.000")
        coord_row(tp, "X", self._cheats_x_var)
        coord_row(tp, "Y", self._cheats_y_var)
        coord_row(tp, "Z", self._cheats_z_var)

        btn_row = ttk.Frame(tp)
        btn_row.pack(fill=tk.X, padx=6, pady=(4, 6))
        self._cheats_capture_btn = ttk.Button(
            btn_row, text="Capture current", command=self._cheats_capture_position,
            state=tk.DISABLED)
        self._cheats_capture_btn.pack(side=tk.LEFT)
        self._cheats_teleport_btn = ttk.Button(
            btn_row, text="Teleport", command=self._cheats_teleport,
            state=tk.DISABLED)
        self._cheats_teleport_btn.pack(side=tk.RIGHT)

        ttk.Separator(tp).pack(fill=tk.X, padx=6, pady=2)

        ttk.Label(tp, text="Teleport to another object:", foreground="#9898b8",
                  font=("Consolas", 8)).pack(anchor="w", padx=6, pady=(4, 2))
        self._cheats_target_var = tk.StringVar()
        self._cheats_target_combo = ttk.Combobox(
            tp, textvariable=self._cheats_target_var, width=26, state="readonly")
        self._cheats_target_combo.pack(fill=tk.X, padx=6, pady=(0, 4))
        self._cheats_teleport_target_btn = ttk.Button(
            tp, text="Teleport to target", command=self._cheats_teleport_to_target,
            state=tk.DISABLED)
        self._cheats_teleport_target_btn.pack(fill=tk.X, padx=6, pady=(0, 6))

        # ── Speed group ──────────────────────────────────────────────
        sp = ttk.LabelFrame(right, text="Speed")
        sp.pack(fill=tk.X)

        boost_row = ttk.Frame(sp)
        boost_row.pack(fill=tk.X, padx=6, pady=(6, 2))
        ttk.Label(boost_row, text="Boost:").pack(side=tk.LEFT)
        self._cheats_boost_var = tk.StringVar(value=str(DEFAULT_BOOST_SPEED))
        ttk.Entry(boost_row, textvariable=self._cheats_boost_var, width=8).pack(
            side=tk.LEFT, padx=(4, 4))
        self._cheats_boost_btn = ttk.Button(
            boost_row, text="Apply forward boost", command=self._cheats_apply_forward_boost,
            state=tk.DISABLED)
        self._cheats_boost_btn.pack(side=tk.LEFT)

        ttk.Separator(sp).pack(fill=tk.X, padx=6, pady=4)

        ttk.Label(sp, text="Manual velocity (world units/tick):",
                  foreground="#9898b8", font=("Consolas", 8)).pack(anchor="w", padx=6)

        self._cheats_vx_var = tk.StringVar(value="0.000")
        self._cheats_vy_var = tk.StringVar(value="0.000")
        self._cheats_vz_var = tk.StringVar(value="0.000")
        coord_row(sp, "Vx", self._cheats_vx_var)
        coord_row(sp, "Vy", self._cheats_vy_var)
        coord_row(sp, "Vz", self._cheats_vz_var)

        vbtn_row = ttk.Frame(sp)
        vbtn_row.pack(fill=tk.X, padx=6, pady=(4, 6))
        self._cheats_velocity_btn = ttk.Button(
            vbtn_row, text="Apply velocity", command=self._cheats_apply_velocity,
            state=tk.DISABLED)
        self._cheats_velocity_btn.pack(side=tk.LEFT)
        self._cheats_stop_btn = ttk.Button(
            vbtn_row, text="Stop (zero)", command=self._cheats_zero_velocity,
            state=tk.DISABLED)
        self._cheats_stop_btn.pack(side=tk.RIGHT)

        # ── Vitality group ──────────────────────────────────────────
        vt = ttk.LabelFrame(right, text="Vitality")
        vt.pack(fill=tk.X, pady=(8, 0))

        self._cheats_hp_var = tk.StringVar(value="1.000")
        self._cheats_sh_var = tk.StringVar(value="1.000")
        coord_row(vt, "HP", self._cheats_hp_var)
        coord_row(vt, "SH", self._cheats_sh_var)

        vit_row = ttk.Frame(vt)
        vit_row.pack(fill=tk.X, padx=6, pady=(4, 2))
        self._cheats_vitality_btn = ttk.Button(
            vit_row, text="Apply", command=self._cheats_apply_vitality,
            state=tk.DISABLED)
        self._cheats_vitality_btn.pack(side=tk.LEFT)

        quick_vit_row = ttk.Frame(vt)
        quick_vit_row.pack(fill=tk.X, padx=6, pady=(0, 6))
        self._cheats_heal_btn = ttk.Button(
            quick_vit_row, text="Full Health/Shields", command=self._cheats_heal,
            state=tk.DISABLED)
        self._cheats_heal_btn.pack(side=tk.LEFT)
        self._cheats_kill_btn = ttk.Button(
            quick_vit_row, text="Kill", command=self._cheats_kill,
            state=tk.DISABLED)
        self._cheats_kill_btn.pack(side=tk.RIGHT)

        # ── Bottom status line ──────────────────────────────────────
        self._cheats_action_lbl = ttk.Label(parent, text="", foreground="#9898b8",
                                            font=("Consolas", 9))
        self._cheats_action_lbl.pack(anchor="w", padx=12, pady=(0, 8))

        self._cheats_selected_index: int | None = None
        self._cheats_target_map: dict[str, int] = {}

    # ── Selection ─────────────────────────────────────────────────────

    def _cheats_action_buttons(self):
        return (
            self._cheats_teleport_btn, self._cheats_capture_btn,
            self._cheats_teleport_target_btn, self._cheats_boost_btn,
            self._cheats_velocity_btn, self._cheats_stop_btn,
            self._cheats_vitality_btn, self._cheats_heal_btn, self._cheats_kill_btn,
        )

    def _on_cheats_select(self, _event=None):
        sel = self._cheats_tree.selection()
        if not sel:
            return
        try:
            idx = int(sel[0])
        except ValueError:
            return
        self._cheats_selected_index = idx
        for btn in self._cheats_action_buttons():
            btn.config(state=tk.NORMAL)
        self._update_cheats_status_line()

    def _update_cheats_status_line(self):
        obj = next((o for o in self._objects
                    if o.get("index") == self._cheats_selected_index), None)
        if not obj:
            self._cheats_sel_lbl.config(text="Selected unit no longer exists.",
                                         foreground="#f07878")
            return
        orig = obj.get("origin") or (None, None, None)
        orig_str = (f"({orig[0]:.2f}, {orig[1]:.2f}, {orig[2]:.2f})"
                    if orig[0] is not None else "—")
        spd = obj.get("speed")
        spd_str = f"{spd:.2f}" if spd is not None else "—"
        self._cheats_sel_lbl.config(
            text=f"Selected: [{self._cheats_selected_index:04d}]  "
                 f"{make_display_type(obj)}  @ {orig_str}   |v|={spd_str}",
            foreground="#9898b8")

    # ── List / target combo refresh (called once per poll tick) ────────

    def _refresh_cheats_list(self):
        tree = self._cheats_tree
        wanted = {}

        for o in self._objects:
            if o.get("type") not in CHEAT_UNIT_TYPES:
                continue
            idx    = o.get("index", "?")
            active = "✓" if o.get("active") else ""
            orig   = o.get("origin")
            orig_str = (f"({orig[0]:8.2f}, {orig[1]:8.2f}, {orig[2]:8.2f})"
                        if orig and orig[0] is not None else "—")
            spd = o.get("speed")
            spd_str = f"{spd:.2f}" if spd is not None else "—"
            hp = o.get("health")
            sh = o.get("shields")
            hp_str = f"{hp:.2f}" if hp is not None else "—"
            sh_str = f"{sh:.2f}" if sh is not None else "—"
            tag  = o.get("type") if o.get("active") else "inactive"
            vals = (idx, make_display_type(o), active, orig_str, spd_str, hp_str, sh_str)
            wanted[str(idx)] = (vals, (tag,))

        existing = set(tree.get_children(""))
        for iid in existing - wanted.keys():
            tree.delete(iid)
        for iid, (vals, tags) in wanted.items():
            if tree.exists(iid):
                tree.item(iid, values=vals, tags=tags)
            else:
                tree.insert("", tk.END, iid=iid, values=vals, tags=tags)

        # Target combo: ANY live object, by index (label stays stable across
        # ticks even though the object moves, so the user's combo selection
        # doesn't keep resetting — the live position is re-fetched at use time).
        items = []
        target_map = {}
        for o in self._objects:
            idx = o.get("index")
            label = f"{idx:04d}  {make_display_type(o)}"
            items.append(label)
            target_map[label] = idx
        self._cheats_target_map = target_map
        self._cheats_target_combo["values"] = items

        if self._cheats_selected_index is not None:
            self._update_cheats_status_line()

    # ── Shared helpers ───────────────────────────────────────────────

    def _cheats_get_selected_obj(self):
        if self._cheats_selected_index is None:
            messagebox.showwarning("Cheats", "No unit selected.")
            return None
        if not self._mem:
            messagebox.showerror("Cheats", "Not connected to process.")
            return None
        obj = next((o for o in self._objects
                    if o.get("index") == self._cheats_selected_index), None)
        if not obj:
            messagebox.showerror("Cheats", "Selected unit no longer exists.")
            return None
        if obj.get("addr", 0) < 0x10000:
            messagebox.showerror("Cheats", "Selected unit has no valid memory address.")
            return None
        return obj

    def _cheats_write_vec3(self, addr, off, vec):
        payload = struct.pack("<3f", *vec)
        return self._mem.write_bytes(addr + off, payload)

    def _cheats_write_vitality(self, addr, health, shields):
        ok_h = self._mem.write_bytes(addr + OBJ_HEALTH_OFF, struct.pack("<f", health))
        ok_s = self._mem.write_bytes(addr + OBJ_SHIELDS_OFF, struct.pack("<f", shields))
        return ok_h and ok_s

    def _cheats_set_status(self, text, ok):
        self._cheats_action_lbl.config(
            text=text, foreground="#3dcc96" if ok else "#f07878")

    # ── Teleport actions ─────────────────────────────────────────────

    def _cheats_capture_position(self):
        obj = self._cheats_get_selected_obj()
        if not obj:
            return
        orig = obj.get("origin") or (None, None, None)
        if orig[0] is None:
            self._cheats_set_status("✗ No valid origin to capture.", False)
            return
        self._cheats_x_var.set(f"{orig[0]:.3f}")
        self._cheats_y_var.set(f"{orig[1]:.3f}")
        self._cheats_z_var.set(f"{orig[2]:.3f}")
        self._cheats_set_status("Captured current position into fields.", True)

    def _cheats_teleport(self):
        obj = self._cheats_get_selected_obj()
        if not obj:
            return
        try:
            x = float(self._cheats_x_var.get())
            y = float(self._cheats_y_var.get())
            z = float(self._cheats_z_var.get())
        except ValueError:
            self._cheats_set_status("✗ X/Y/Z must be numbers.", False)
            return
        ok = self._cheats_write_vec3(obj["addr"], OBJ_ORIGIN_OFF, (x, y, z))
        if ok:
            self._cheats_set_status(
                f"✓ Teleported [{obj['index']:04d}] to ({x:.2f}, {y:.2f}, {z:.2f})", True)
        else:
            self._cheats_set_status("✗ Teleport write failed.", False)

    def _cheats_teleport_to_target(self):
        obj = self._cheats_get_selected_obj()
        if not obj:
            return
        label = self._cheats_target_var.get()
        target_idx = self._cheats_target_map.get(label)
        if target_idx is None:
            self._cheats_set_status("✗ Pick a target object first.", False)
            return
        target = next((o for o in self._objects if o.get("index") == target_idx), None)
        if not target:
            self._cheats_set_status("✗ Target object no longer exists.", False)
            return
        t_orig = target.get("origin") or (None, None, None)
        if t_orig[0] is None:
            self._cheats_set_status("✗ Target has no valid origin.", False)
            return
        ok = self._cheats_write_vec3(obj["addr"], OBJ_ORIGIN_OFF, t_orig)
        if ok:
            self._cheats_set_status(
                f"✓ Teleported [{obj['index']:04d}] to [{target_idx:04d}] "
                f"{make_display_type(target)} @ "
                f"({t_orig[0]:.2f}, {t_orig[1]:.2f}, {t_orig[2]:.2f})", True)
            self._cheats_x_var.set(f"{t_orig[0]:.3f}")
            self._cheats_y_var.set(f"{t_orig[1]:.3f}")
            self._cheats_z_var.set(f"{t_orig[2]:.3f}")
        else:
            self._cheats_set_status("✗ Teleport write failed.", False)

    # ── Speed actions ────────────────────────────────────────────────

    def _cheats_apply_forward_boost(self):
        obj = self._cheats_get_selected_obj()
        if not obj:
            return
        try:
            speed = float(self._cheats_boost_var.get())
        except ValueError:
            self._cheats_set_status("✗ Boost speed must be a number.", False)
            return
        fwd = obj.get("forward") or (None, None, None)
        if fwd[0] is None:
            self._cheats_set_status("✗ No valid facing direction to boost along.", False)
            return
        fx, fy, fz = fwd
        mag = math.sqrt(fx * fx + fy * fy + fz * fz) or 1.0
        vec = (fx / mag * speed, fy / mag * speed, fz / mag * speed)
        ok = self._cheats_write_vec3(obj["addr"], OBJ_TRANS_VEL_OFF, vec)
        if ok:
            self._cheats_set_status(
                f"✓ Boosted [{obj['index']:04d}] to speed {speed:.2f} (facing direction)",
                True)
        else:
            self._cheats_set_status("✗ Boost write failed.", False)

    def _cheats_apply_velocity(self):
        obj = self._cheats_get_selected_obj()
        if not obj:
            return
        try:
            vx = float(self._cheats_vx_var.get())
            vy = float(self._cheats_vy_var.get())
            vz = float(self._cheats_vz_var.get())
        except ValueError:
            self._cheats_set_status("✗ Velocity X/Y/Z must be numbers.", False)
            return
        ok = self._cheats_write_vec3(obj["addr"], OBJ_TRANS_VEL_OFF, (vx, vy, vz))
        if ok:
            self._cheats_set_status(
                f"✓ Set velocity of [{obj['index']:04d}] to "
                f"({vx:.2f}, {vy:.2f}, {vz:.2f})", True)
        else:
            self._cheats_set_status("✗ Velocity write failed.", False)

    def _cheats_zero_velocity(self):
        obj = self._cheats_get_selected_obj()
        if not obj:
            return
        ok = self._cheats_write_vec3(obj["addr"], OBJ_TRANS_VEL_OFF, (0.0, 0.0, 0.0))
        if ok:
            self._cheats_set_status(f"✓ Zeroed velocity of [{obj['index']:04d}]", True)
        else:
            self._cheats_set_status("✗ Velocity write failed.", False)

    # ── Vitality actions ─────────────────────────────────────────────

    def _cheats_apply_vitality(self):
        obj = self._cheats_get_selected_obj()
        if not obj:
            return
        try:
            hp = float(self._cheats_hp_var.get())
            sh = float(self._cheats_sh_var.get())
        except ValueError:
            self._cheats_set_status("✗ HP/SH must be numbers.", False)
            return
        ok = self._cheats_write_vitality(obj["addr"], hp, sh)
        if ok:
            self._cheats_set_status(
                f"✓ Set HP/SH of [{obj['index']:04d}] to ({hp:.2f}, {sh:.2f})", True)
        else:
            self._cheats_set_status("✗ Vitality write failed.", False)

    def _cheats_heal(self):
        obj = self._cheats_get_selected_obj()
        if not obj:
            return
        ok = self._cheats_write_vitality(obj["addr"], 1.0, 1.0)
        self._cheats_hp_var.set("1.000")
        self._cheats_sh_var.set("1.000")
        if ok:
            self._cheats_set_status(f"✓ Fully healed [{obj['index']:04d}]", True)
        else:
            self._cheats_set_status("✗ Heal write failed.", False)

    def _cheats_kill(self):
        obj = self._cheats_get_selected_obj()
        if not obj:
            return
        ok = self._cheats_write_vitality(obj["addr"], 0.0, 0.0)
        self._cheats_hp_var.set("0.000")
        self._cheats_sh_var.set("0.000")
        if ok:
            self._cheats_set_status(
                f"✓ Killed [{obj['index']:04d}] (health & shields zeroed)", True)
        else:
            self._cheats_set_status("✗ Kill write failed.", False)
