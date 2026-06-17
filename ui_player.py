"""
Halo 2 Xbox Object Monitor — Player tab mixin.

Memory layout (confirmed from players.CEM):
  t_players_data DataArray:    0x30002AD0
    DataArray header:          0x76 bytes  (confirmed from players.CEM)
    s_player_datum[N]:         base + 0x4C + N * 0x204  (max 16 slots)
      +0x000  int16   Salt
      +0x002  byte    Flags  (bit0=connected, bit1=left_game)
      +0x004  bytes12 PlayerIdentifier
      +0x014  bytes6  MachineIdentifier
      +0x01A  int16   MachineUserIndex
      +0x01C  int32   MachineControllerIndex
      +0x024  int32   ControllerIndex
      +0x028  int16   UserIndex
      +0x028  uint32  SlaveUnitIndex  -> links to object table (confirmed +0x28)
      +0x016  wchar16 Gamertag (UTF-16LE, up to 16 chars = 32 bytes)

  s_player_control_globals:    0x30004B5C
      s_player[N] at PCG+0x154 + N*0x548  (N = user_index, 0-3)
      s_player size: 0x548 = 1352 bytes (confirmed from P1/P2 stick addresses)
        +0x00  uint32  UnitIndex       (PCG+0x154) confirmed 0xE2C60057 in capture
        +0x04  bytes5  Buttons         (PCG+0x158) confirmed button map
        +0x28  float   LeftThumb.fwd   (PCG+0x17C / 0x30004CD8) confirmed
        +0x2C  float   LeftThumb.rgt   (PCG+0x180 / 0x30004CDC) confirmed
        +0x30  float   RightTrigger    (PCG+0x184 / 0x30004CE0) confirmed
        +0x34  float   LeftTrigger     (PCG+0x188 / 0x30004CE4) confirmed
        +0x88  float   RightThumb.x    (PCG+0x1DC / 0x30004D38) confirmed
        +0x8C  float   RightThumb.y    (PCG+0x1E0 / 0x30004D3C) confirmed
      P2 stride confirmed: 0x30005220 - 0x30004CD8 = 0x548
"""

import math
import struct
import tkinter as tk
from tkinter import ttk

# ── Constants ──────────────────────────────────────────────────────────────

PLAYERS_ARRAY_BASE  = 0x30002AD0
PLAYERS_ARRAY_HDR   = 0x4C
PLAYERS_DATUM_SIZE  = 0x204
PLAYERS_MAX         = 16

PCG_BASE            = 0x30004B5C   # s_player_control_globals
PCG_PLAYERS_OFFSET  = 0x154        # s_player[0] base confirmed from UnitIndex + button bytes
PCG_PLAYER_SIZE     = 0x548        # confirmed: P2 LThumb.fwd at 0x30005220 = P1+0x548+0x28

# s_player field offsets relative to PCG_PLAYERS_OFFSET (all confirmed empirically):
PCG_P_UNIT_INDEX    = 0x00   # datum_index -> links to object table  (PCG+0x154)
PCG_P_BUTTONS       = 0x04   # 5-byte button state                   (PCG+0x158)
PCG_P_LT_FWD        = 0x28   # LeftThumb forward  float              (PCG+0x17C)
PCG_P_LT_RGT        = 0x2C   # LeftThumb strafe   float              (PCG+0x180)
PCG_P_RT_TRIG       = 0x30   # RightTrigger       float              (PCG+0x184)
PCG_P_LT_TRIG       = 0x34   # LeftTrigger        float              (PCG+0x188)
PCG_P_RT_X          = 0x88   # RightThumb.x       float              (PCG+0x1DC)
PCG_P_RT_Y          = 0x8C   # RightThumb.y       float              (PCG+0x1E0)

# player_action bit names (from Players.hpp)
# Button map confirmed empirically from 5-byte region at 0x30004CB4.
# Format: (byte_index, bitmask, label, mode)
#   mode 'on'      = active when (byte & mask) == mask
#   mode 'tap'     = low nibble bit of mask = tap
#   mode 'held'    = high nibble bit of mask = held (X and Y only)
BUTTON_MAP = [
    # byte 0
    (0, 0x01, "L3",        'on'),
    (0, 0x0E, "A (Jump)",  'on'),
    (0, 0x10, "LB",        'on'),
    (0, 0xC0, "B (Melee)", 'on'),
    # byte 1
    (1, 0x01, "RT",        'on'),
    (1, 0x02, "DPad \u2190",'on'),
    (1, 0x04, "DPad \u2192",'on'),
    (1, 0x20, "LT",        'on'),
    # byte 2
    (2, 0x01, "DPad \u2193",'on'),
    (2, 0x04, "RT (held)", 'on'),
    (2, 0x08, "LB (held)", 'on'),
    (2, 0x40, "LB (alt)",  'on'),
    (2, 0x80, "LT (alt)",  'on'),
    # byte 3
    (3, 0x08, "LB (b3)",   'on'),
    (3, 0x10, "LT (b3)",   'on'),
    (3, 0x80, "B (held)",  'on'),
    # byte 4 — X and Y have tap/held pairs
    (4, 0x01, "X (tap)",   'on'),
    (4, 0x02, "X (held)",  'on'),
    (4, 0x10, "Y (tap)",   'on'),
    (4, 0x20, "Y (held)",  'on'),
]

GRENADE_NAMES = {0: "Frag", 1: "Plasma", 2: "Spike", 3: "Firebomb"}


def _read_player_datum(mem, slot: int) -> dict | None:
    """Read one s_player_datum from memory."""
    addr = PLAYERS_ARRAY_BASE + PLAYERS_ARRAY_HDR + slot * PLAYERS_DATUM_SIZE
    raw  = mem.read(addr, PLAYERS_DATUM_SIZE)
    if not raw:
        return None

    def ri16(o):  return struct.unpack_from("<H", raw, o)[0]
    def ri16s(o): return struct.unpack_from("<h", raw, o)[0]
    def ri32(o):  return struct.unpack_from("<I", raw, o)[0]

    salt  = ri16(0x00)
    if salt == 0:
        return None   # null/empty slot

    flags = raw[0x02]
    connected = bool(flags & 0x01)
    left_game = bool(flags & 0x02)
    if not connected:
        return None   # slot unused

    slave = ri32(0x28)   # SlaveUnitIndex confirmed at +0x28 (salt=0xE54C idx=0x02CC)

    # Gamertag: UTF-16LE, 16 chars = 32 bytes at +0x40
    gt_raw  = raw[0x40:0x40+32]
    null_at = gt_raw.find(b"\x00\x00")
    if null_at > 0 and null_at % 2 == 0:
        gt_raw = gt_raw[:null_at]
    try:
        gamertag = gt_raw.decode("utf-16-le", errors="replace").rstrip("\x00")
    except Exception:
        gamertag = "?"

    return {
        "slot":            slot,
        "salt":            salt,
        "flags":           flags,
        "connected":       connected,
        "left_game":       left_game,
        "user_index":      ri16s(0x28),
        "controller_index":ri32(0x24),
        "machine_user_idx":ri16s(0x1A),
        "slave_unit_index": slave,
        "gamertag":         gamertag,
    }


def _read_pcg_player(mem, slot: int) -> dict | None:
    """Read player input state from s_player_control_globals.
    s_player[0] confirmed at PCG+0x154 with all field offsets empirically verified.
    """
    base_off = PCG_PLAYERS_OFFSET + slot * PCG_PLAYER_SIZE
    # Read from s_player[0] base, covering all confirmed fields (+0x8C is furthest)
    raw = mem.read(PCG_BASE + base_off, 0x90)
    if not raw:
        return None

    def rf(rel):
        if rel + 4 > len(raw): return 0.0
        v = struct.unpack_from("<f", raw, rel)[0]
        return 0.0 if (v != v) or abs(v) > 1e6 else v

    def ri32(rel):
        if rel + 4 > len(raw): return 0xFFFFFFFF
        return struct.unpack_from("<I", raw, rel)[0]

    def ri16s(rel):
        if rel + 2 > len(raw): return 0
        return struct.unpack_from("<h", raw, rel)[0]

    return {
        "unit_index":     ri32(PCG_P_UNIT_INDEX),
        "buttons":        bytes(raw[PCG_P_BUTTONS:PCG_P_BUTTONS+5]),
        "left_thumb_fwd": rf(PCG_P_LT_FWD),
        "left_thumb_rgt": rf(PCG_P_LT_RGT),
        "right_trigger":  rf(PCG_P_RT_TRIG),
        "left_trigger":   rf(PCG_P_LT_TRIG),
        "right_thumb_x":  rf(PCG_P_RT_X),
        "right_thumb_y":  rf(PCG_P_RT_Y),
    }


# Button bytes now read inside _read_pcg_player at s_player+0x04


def read_all_players(mem) -> list[dict]:
    """Read all active player slots, merging datum + control data.
    The PCG s_player index matches the player's user_index (0-3),
    not their position in the datum array (0-15).
    """
    players = []
    for slot in range(PLAYERS_MAX):
        datum = _read_player_datum(mem, slot)
        if datum is None:
            continue
        # Use user_index as the PCG slot — confirmed by P2 stick address
        pcg_slot = datum.get("user_index", 0)
        if pcg_slot < 0 or pcg_slot > 3:
            pcg_slot = 0  # clamp to valid range
        ctrl = _read_pcg_player(mem, pcg_slot) or {}
        datum["action_buttons"] = ctrl.get("buttons", bytes(5))
        datum["ctrl"] = ctrl
        datum["pcg_slot"] = pcg_slot
        players.append(datum)
    return players


# ── PlayerMixin ────────────────────────────────────────────────────────────

class PlayerMixin:
    """Player tab: live player data, input state, stick visualiser."""

    def _build_player_panel(self, parent):
        self._player_data:   list[dict] = []
        self._player_sel_slot: int | None = None

        # ── Top: player slot list ──────────────────────────────────────────
        top = ttk.Frame(parent)
        top.pack(fill=tk.X, padx=8, pady=(8, 4))

        slot_cols = ("slot", "gamertag", "salt", "status",
                     "user", "controller", "unit")
        self._player_tree = ttk.Treeview(
            top, columns=slot_cols, show="headings",
            height=4, selectmode="browse")

        slot_col_cfg = [
            ("slot",       "Slot",       38,  tk.CENTER),
            ("gamertag",   "Gamertag",   130, tk.W),
            ("salt",       "Salt",       62,  tk.W),
            ("status",     "Status",     80,  tk.W),
            ("user",       "User",       40,  tk.CENTER),
            ("controller", "Controller", 60,  tk.CENTER),
            ("unit",       "Unit Index", 90,  tk.W),
        ]
        for col, hd, w, anc in slot_col_cfg:
            self._player_tree.heading(col, text=hd)
            self._player_tree.column(col, width=w, anchor=anc, minwidth=24)

        self._player_tree.tag_configure("connected", foreground="#3dcc96")
        self._player_tree.tag_configure("left",      foreground="#f07878")
        self._player_tree.tag_configure("inactive",  foreground="#3a3a5a")

        pt_vsb = ttk.Scrollbar(top, orient=tk.VERTICAL,
                                command=self._player_tree.yview)
        self._player_tree.configure(yscrollcommand=pt_vsb.set)
        self._player_tree.pack(side=tk.LEFT, fill=tk.X, expand=True)
        pt_vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self._player_tree.bind("<<TreeviewSelect>>", self._on_player_select)

        ttk.Separator(parent, orient=tk.HORIZONTAL).pack(
            fill=tk.X, padx=8, pady=(0, 4))

        # ── Bottom: detail area split left/right ───────────────────────────
        detail = ttk.Frame(parent)
        detail.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 8))

        # Left column: identity + unit state
        left = ttk.Frame(detail)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Identity fields
        id_frame = ttk.LabelFrame(left, text="Identity")
        id_frame.pack(fill=tk.X, pady=(0, 6))
        self._player_id_text = tk.Text(
            id_frame, height=7, bg="#14141c", fg="#e8e8f0",
            font=("Consolas", 10), relief=tk.FLAT,
            state=tk.DISABLED, cursor="arrow", padx=6, pady=4)
        self._player_id_text.pack(fill=tk.X)
        self._player_id_text.tag_configure("key",  foreground="#7ab4e0")
        self._player_id_text.tag_configure("val",  foreground="#e8e8f0")
        self._player_id_text.tag_configure("good", foreground="#3dcc96")
        self._player_id_text.tag_configure("bad",  foreground="#f07878")

        # Unit state (live from object table)
        unit_frame = ttk.LabelFrame(left, text="Unit state  (from object table)")
        unit_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 0))

        # HP/shield bars
        self._player_bar_canvas = tk.Canvas(
            unit_frame, height=44, bg="#0d0d12", highlightthickness=0)
        self._player_bar_canvas.pack(fill=tk.X)

        self._player_unit_text = tk.Text(
            unit_frame, bg="#14141c", fg="#e8e8f0",
            font=("Consolas", 10), relief=tk.FLAT,
            state=tk.DISABLED, cursor="arrow", padx=6, pady=4)
        self._player_unit_text.pack(fill=tk.BOTH, expand=True)
        for tag, fg in [("key","#7ab4e0"),("val","#e8e8f0"),("good","#3dcc96"),
                        ("bad","#f07878"),("warn","#f0b040"),("addr","#60a8f0")]:
            self._player_unit_text.tag_configure(tag, foreground=fg)

        # Right column: input state
        right = ttk.Frame(detail)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(12, 0))

        # Stick visualiser
        stick_frame = ttk.LabelFrame(right, text="Sticks & Triggers")
        stick_frame.pack(fill=tk.X, pady=(0, 6))
        self._player_stick_canvas = tk.Canvas(
            stick_frame, height=160, bg="#0d0d12", highlightthickness=0)
        self._player_stick_canvas.pack(fill=tk.X)
        self._player_stick_canvas.bind(
            "<Configure>", lambda e: self._player_redraw_sticks())

        # Action flags grid
        action_frame = ttk.LabelFrame(right, text="Action flags")
        action_frame.pack(fill=tk.BOTH, expand=True)
        self._player_action_canvas = tk.Canvas(
            action_frame, bg="#0d0d12", highlightthickness=0)
        self._player_action_canvas.pack(fill=tk.BOTH, expand=True)
        self._player_action_canvas.bind(
            "<Configure>", lambda e: self._player_redraw_actions())
        self._player_action_canvas.bind(
            "<ButtonPress-1>", self._player_on_action_press)
        self._player_action_canvas.bind(
            "<ButtonRelease-1>", self._player_on_action_release)

        self._player_force_status = ttk.Label(
            right,
            text="Click & hold a flag to force-write that bit live and "
                 "see if the action fires in-game.",
            foreground="#9898b8", font=("Consolas", 8),
            wraplength=360, justify=tk.LEFT)
        self._player_force_status.pack(fill=tk.X, pady=(4, 0))

        self._player_action_buttons   = bytes(5)
        self._player_action_pcg_slot  = 0
        self._player_action_cells     = []   # hit-test rects from last redraw
        self._player_force_active     = None # (byte_idx, mask, name) being forced
        self._player_force_job        = None # after() id for the write loop
        self._player_force_count      = 0

    # ── Refresh ────────────────────────────────────────────────────────────

    def _refresh_player_tab(self):
        """Called each poll tick. Reads players from memory and updates UI."""
        if not self._mem:
            return
        try:
            self._player_data = read_all_players(self._mem)
        except Exception:
            return
        self._player_update_tree()
        self._player_update_detail()

    def _player_update_tree(self):
        tree    = self._player_tree
        wanted  = {}

        for p in self._player_data:
            slot = p["slot"]
            slave = p.get("slave_unit_index", 0xFFFFFFFF)
            unit_str = (f"0x{slave:08X}" if slave != 0xFFFFFFFF else "—")
            status = "left" if p.get("left_game") else "connected"
            vals = (
                slot,
                p.get("gamertag", "?"),
                f"0x{p.get('salt',0):04X}",
                status,
                p.get("user_index", "?"),
                p.get("controller_index", "?"),
                unit_str,
            )
            wanted[str(slot)] = (vals, (status,))

        existing = set(tree.get_children(""))
        for iid in existing - wanted.keys():
            tree.delete(iid)
        for iid, (vals, tags) in wanted.items():
            if tree.exists(iid):
                tree.item(iid, values=vals, tags=tags)
            else:
                tree.insert("", tk.END, iid=iid, values=vals, tags=tags)

    def _player_update_detail(self):
        """Update the detail panels for the selected player."""
        sel = self._player_tree.selection()
        if not sel:
            # If only one player, auto-select
            kids = self._player_tree.get_children()
            if len(kids) == 1:
                self._player_tree.selection_set(kids[0])
                sel = kids
            else:
                return
        try:
            slot = int(sel[0])
        except (ValueError, IndexError):
            return

        p = next((x for x in self._player_data if x["slot"] == slot), None)
        if not p:
            return

        self._player_sel_slot = slot
        self._player_action_buttons  = p.get("action_buttons", bytes(5))
        self._player_action_pcg_slot = p.get("pcg_slot", 0)

        self._player_draw_identity(p)
        self._player_draw_unit_state(p)
        self._player_redraw_sticks()
        self._player_redraw_actions()

    def _on_player_select(self, _event=None):
        self._player_on_action_release()   # don't keep forcing into a stale slot
        self._player_update_detail()

    # ── Identity panel ─────────────────────────────────────────────────────

    def _player_draw_identity(self, p: dict):
        txt = self._player_id_text
        txt.config(state=tk.NORMAL)
        txt.delete("1.0", tk.END)

        def row(label, value, tag="val"):
            txt.insert(tk.END, f"  {label:<22}", "key")
            txt.insert(tk.END, f"{value}\n", tag)

        row("Gamertag",       p.get("gamertag", "?"),
            "good" if not p.get("left_game") else "bad")
        row("Slot",           str(p["slot"]))
        row("Salt",           f"0x{p.get('salt',0):04X}")
        row("User index",     str(p.get("user_index", "?")))
        row("Controller idx", str(p.get("controller_index", "?")))
        row("Machine user",   str(p.get("machine_user_idx", "?")))
        flags = p.get("flags", 0)
        flag_strs = []
        if flags & 0x01: flag_strs.append("connected")
        if flags & 0x02: flag_strs.append("left_game")
        row("Flags",          f"0x{flags:02X}  [{', '.join(flag_strs) or 'none'}]")

        txt.config(state=tk.DISABLED)

    # ── Unit state panel ───────────────────────────────────────────────────

    def _player_draw_unit_state(self, p: dict):
        slave = p.get("slave_unit_index", 0xFFFFFFFF)
        txt   = self._player_unit_text
        txt.config(state=tk.NORMAL)
        txt.delete("1.0", tk.END)

        def row(label, value, tag="val"):
            txt.insert(tk.END, f"  {label:<22}", "key")
            txt.insert(tk.END, f"{value}\n", tag)

        if slave == 0xFFFFFFFF:
            txt.insert(tk.END, "  No unit assigned (not spawned)\n", "bad")
            txt.config(state=tk.DISABLED)
            self._player_draw_bars(None, None)
            return

        row("SlaveUnitIndex",
            f"0x{slave:08X}  (salt=0x{slave>>16:04X}, idx=0x{slave&0xFFFF:04X})",
            "addr")

        # Cross-reference the object table.
        # Primary:  SlaveUnitIndex at datum+0x28 (salt in high 16 bits)
        # Fallback: UnitIndex from s_player_control_globals (PCG+0x154)
        slave_salt  = (slave >> 16) & 0xFFFF
        ctrl        = p.get("ctrl", {})
        pcg_unit    = ctrl.get("unit_index", 0xFFFFFFFF)
        pcg_salt    = (pcg_unit >> 16) & 0xFFFF if pcg_unit != 0xFFFFFFFF else 0

        unit_obj = next(
            (o for o in self._objects if o.get("salt") == slave_salt), None)
        if unit_obj is None and pcg_salt:
            unit_obj = next(
                (o for o in self._objects if o.get("salt") == pcg_salt), None)

        if unit_obj:
            hp  = unit_obj.get("health")
            sh  = unit_obj.get("shields")
            orig = unit_obj.get("origin") or (None, None, None)
            fwd  = unit_obj.get("forward") or (None, None, None)
            vel  = unit_obj.get("trans_vel") or (None, None, None)
            spd  = unit_obj.get("speed")
            sc   = unit_obj.get("scale")
            clus = unit_obj.get("cluster")
            defn = unit_obj.get("definition_tag", "")

            self._player_draw_bars(hp, sh)

            row("Type",       unit_obj.get("type", "?"))
            row("Tag",        defn or "—")
            if orig[0] is not None:
                row("Origin",
                    f"({orig[0]:.3f}, {orig[1]:.3f}, {orig[2]:.3f})")
            if fwd[0] is not None:
                row("Forward",
                    f"({fwd[0]:.3f}, {fwd[1]:.3f}, {fwd[2]:.3f})")
            if spd is not None:
                stag = ("good" if spd < 0.5 else
                        "warn" if spd < 5.0 else "bad")
                row("Speed |v|",  f"{spd:.4f} wu/tick", stag)
            if hp is not None:
                htag = ("good" if hp > 0.5 else
                        "warn" if hp > 0.2 else "bad")
                stag = ("good" if (sh or 0) > 0.5 else
                        "warn" if (sh or 0) > 0.2 else "bad")
                row("Health",     f"{hp:.4f}  ({hp*100:.1f}%)", htag)
                row("Shields",    f"{(sh or 0):.4f}  ({(sh or 0)*100:.1f}%)", stag)
            if sc is not None:
                row("Scale",      f"{sc:.4f}")
            if clus is not None:
                row("Cluster",    str(clus))

            # Weapon/grenade from control globals
            ctrl = p.get("ctrl", {})
            g_idx = ctrl.get("grenade_index", -1)
            z_idx = ctrl.get("zoom_index", 0)
            row("Grenade",    GRENADE_NAMES.get(g_idx, f"idx {g_idx}"))
            row("Zoom level", str(z_idx))
        else:
            self._player_draw_bars(None, None)
            txt.insert(tk.END,
                f"  Unit 0x{slave:08X} not found in object table\n",
                "warn")

        txt.config(state=tk.DISABLED)

    def _player_draw_bars(self, hp, sh):
        c = self._player_bar_canvas
        c.delete("all")
        w = c.winfo_width() or 300

        def bar(x, y, label, value, color_full, color_empty):
            bw   = w - 90
            fill = int(bw * max(0.0, min(1.0, value or 0.0)))
            c.create_text(x, y+7, text=label, fill="#777",
                          font=("Consolas", 9), anchor="e")
            c.create_rectangle(x+4, y, x+4+bw, y+14, fill=color_empty, outline="")
            if fill > 0:
                c.create_rectangle(x+4, y, x+4+fill, y+14,
                                   fill=color_full, outline="")
            pct = f"{(value or 0)*100:.0f}%"
            c.create_text(x+4+bw+4, y+7, text=pct, fill="#aaaaaa",
                          font=("Consolas", 9), anchor="w")

        bar(60, 4,  "HP", hp, "#2ab87a", "#0e2218")
        bar(60, 24, "SH", sh, "#3a80d0", "#081428")

    # ── Stick visualiser ───────────────────────────────────────────────────

    def _player_redraw_sticks(self):
        c  = self._player_stick_canvas
        c.delete("all")
        W  = c.winfo_width()  or 340
        H  = c.winfo_height() or 160

        # Find control data for selected player
        p    = next((x for x in self._player_data
                     if x.get("slot") == self._player_sel_slot), None)
        ctrl = (p.get("ctrl", {}) if p else {})

        rx  = ctrl.get("right_thumb_x",  0.0) or 0.0   # PCG+0x1DC
        ry  = ctrl.get("right_thumb_y",  0.0) or 0.0   # PCG+0x1E0
        lfw = ctrl.get("left_thumb_fwd", 0.0) or 0.0   # PCG+0x17C
        lrt = ctrl.get("left_thumb_rgt", 0.0) or 0.0   # PCG+0x180
        rt  = ctrl.get("right_trigger",  0.0) or 0.0   # PCG+0x184
        lt  = ctrl.get("left_trigger",   0.0) or 0.0   # PCG+0x188

        stick_r = min(W // 5, H // 2) - 12
        gap     = 12

        def draw_stick(cx, cy, vx, vy, label):
            # Outer ring
            c.create_oval(cx-stick_r, cy-stick_r, cx+stick_r, cy+stick_r,
                          outline="#1c1c2e", width=1)
            # Dead-zone ring
            dz = int(stick_r * 0.15)
            c.create_oval(cx-dz, cy-dz, cx+dz, cy+dz,
                          outline="#2a2a4a", width=1, dash=(2, 4))
            # Cross-hairs
            c.create_line(cx-stick_r, cy, cx+stick_r, cy, fill="#14141e")
            c.create_line(cx, cy-stick_r, cx, cy+stick_r, fill="#14141e")
            # Dot
            dx = int(vx * stick_r)
            dy = int(-vy * stick_r)
            dot_r = 5
            c.create_oval(cx+dx-dot_r, cy+dy-dot_r,
                          cx+dx+dot_r, cy+dy+dot_r,
                          fill="#9F99FF", outline="#ffffff", width=1)
            # Values
            c.create_text(cx, cy + stick_r + 12,
                          text=f"{vx:+.2f} / {vy:+.2f}",
                          fill="#6060a0", font=("Consolas", 8))
            c.create_text(cx, cy - stick_r - 10,
                          text=label, fill="#9898b8", font=("Consolas", 9))

        # Left stick
        lcx = W // 4
        draw_stick(lcx, H // 2, lrt, lfw, "Left Stick")

        # Right stick
        rcx = W * 3 // 4
        draw_stick(rcx, H // 2, rx, ry, "Right Stick")

        # Trigger bars (between sticks)
        mid_x = W // 2
        bh    = H - 40
        by    = 20

        def draw_trigger(tx, val, label):
            fill_h = int(bh * max(0.0, min(1.0, val)))
            c.create_rectangle(tx-8, by, tx+8, by+bh,
                               fill="#0a0a14", outline="#1c1c2e")
            if fill_h > 0:
                c.create_rectangle(tx-8, by+bh-fill_h, tx+8, by+bh,
                                   fill="#3a80d0", outline="")
            c.create_text(tx, by + bh + 10, text=label,
                          fill="#9898b8", font=("Consolas", 8))
            c.create_text(tx, by - 8, text=f"{val:.2f}",
                          fill="#6060a0", font=("Consolas", 8))

        draw_trigger(mid_x - 12, lt, "L")
        draw_trigger(mid_x + 12, rt, "R")

    # ── Action flags grid ──────────────────────────────────────────────────

    def _player_redraw_actions(self):
        c  = self._player_action_canvas
        c.delete("all")
        W  = c.winfo_width()  or 280
        H  = c.winfo_height() or 180

        buttons = self._player_action_buttons or bytes(5)  # 5 bytes from s_player+0x04
        cols    = 4
        rows    = math.ceil(len(BUTTON_MAP) / cols)
        cell_w  = W // cols
        cell_h  = max(28, H // rows)

        forced = self._player_force_active   # (byte_idx, mask, name) or None
        self._player_action_cells = []

        for i, (byte_idx, mask, name, _mode) in enumerate(BUTTON_MAP):
            col    = i % cols
            row    = i // cols
            x0     = col * cell_w + 3
            y0     = row * cell_h + 3
            x1     = x0 + cell_w - 6
            y1     = y0 + cell_h - 6
            self._player_action_cells.append((x0, y0, x1, y1, byte_idx, mask, name))

            bval      = buttons[byte_idx] if byte_idx < len(buttons) else 0
            active    = bool(bval & mask)
            is_forced = forced is not None and forced[0] == byte_idx and forced[1] == mask

            if is_forced:
                bg, fg, ol, lw = "#6e2a1e", "#ffffff", "#f0703a", 2
            elif active:
                bg, fg, ol, lw = "#1e3a6e", "#ffffff", "#3a80d0", 1
            else:
                bg, fg, ol, lw = "#0a0a14", "#3a3a5a", "#1c1c2e", 1

            c.create_rectangle(x0, y0, x1, y1, fill=bg, outline=ol, width=lw)
            c.create_text((x0+x1)//2, (y0+y1)//2,
                          text=name, fill=fg,
                          font=("Consolas", 7), justify=tk.CENTER)
        # Raw byte display at bottom
        hex_str = ' '.join(f'{b:02X}' for b in buttons)
        c.create_text(4, H - 4, text=f"raw: {hex_str}",
                      fill="#3a3a5a", font=("Consolas", 8), anchor="sw")

    # ── Action-flag write test ───────────────────────────────────────────
    # Click-and-hold a flag in the grid to force that bit on at the source
    # (s_player_control_globals.Buttons, the same bytes _read_pcg_player
    # decodes) and watch the game. The real controller/engine refreshes
    # this buffer every tick, so a single write can be overwritten before
    # anything reads it; holding re-asserts the bit every ~10ms, far
    # faster than the game's own tick rate, to give it a real chance of
    # being observed by whatever consumes this buffer. This only tells you
    # whether THIS field is the one driving the action — it does not
    # guarantee it (it could be a downstream mirror of an action that's
    # decided elsewhere).

    def _player_on_action_press(self, event):
        if not self._mem or self._player_sel_slot is None:
            return
        for (x0, y0, x1, y1, byte_idx, mask, name) in self._player_action_cells:
            if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                self._player_force_active = (byte_idx, mask, name)
                self._player_force_count  = 0
                self._player_force_tick()
                return

    def _player_on_action_release(self, _event=None):
        if self._player_force_job is not None:
            try:
                self.after_cancel(self._player_force_job)
            except Exception:
                pass
            self._player_force_job = None
        if self._player_force_active is not None:
            _, _, name = self._player_force_active
            self._player_force_status.config(
                text=f"Released '{name}' after {self._player_force_count} "
                     f"forced write(s). Did the unit do that on-screen?",
                foreground="#9898b8")
        self._player_force_active = None
        self._player_redraw_actions()

    def _player_force_tick(self):
        if self._player_force_active is None or not self._mem:
            return
        byte_idx, mask, name = self._player_force_active
        pcg_slot = self._player_action_pcg_slot or 0
        addr = (PCG_BASE + PCG_PLAYERS_OFFSET
                + pcg_slot * PCG_PLAYER_SIZE + PCG_P_BUTTONS + byte_idx)

        cur = self._mem.read(addr, 1)
        if cur is not None:
            if self._mem.write_bytes(addr, bytes([cur[0] | mask])):
                self._player_force_count += 1

        self._player_force_status.config(
            text=f"Forcing '{name}'  (byte {byte_idx}, mask 0x{mask:02X}) "
                 f"\u2192 0x{addr:08X}   [{self._player_force_count} writes]",
            foreground="#f0b040")
        self._player_redraw_actions()
        self._player_force_job = self.after(10, self._player_force_tick)
