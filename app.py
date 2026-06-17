"""Halo 2 Xbox Object Monitor — main App class."""
import tkinter as tk
from tkinter import ttk, messagebox
import math
import time
import sys
import struct

from constants import (
    OBJECT_TYPES, TYPE_COLORS, HEADER_FLAG_NAMES,
    MAP_STRING_ADDR, MAP_STRING_MAXLEN,
    TELEPORT_THRESHOLD, HISTORY_MAX_TICKS,
)
from memory import MemoryReader, list_processes, find_halo2_pid
from parser import read_all_objects
from tag_database import resolve_map_tags
import tag_database as _tag_db  # _tag_db._active_map_name, _tag_db._active_tag_map
from ui_objects import ObjectTableMixin
from ui_detail import DetailMixin
from ui_aup import AupMixin
from ui_map import MapMixin
from ui_player import PlayerMixin, read_all_players
from ui_scripts import ScriptsMixin, get_script_db
from ui_bsp import BspMixin, get_bsp_sections, get_bsp_geometry
from ui_cheats import CheatsMixin


class App(ObjectTableMixin, DetailMixin, AupMixin, MapMixin, PlayerMixin, ScriptsMixin, BspMixin,
          CheatsMixin, tk.Tk):
    REFRESH_MS = 500

    def __init__(self):
        super().__init__()
        self.title("Halo 2 – Live Object Monitor")
        self.geometry("1280x800")
        self.minsize(900, 600)
        self.configure(bg="#1a1a1a")

        self._mem: MemoryReader | None = None
        self._pid: int | None = None
        self._running = False
        self._objects = []
        self._filter_type = tk.StringVar(value="all")   # kept for compat; not used by filter
        self._filter_active = tk.BooleanVar(value=False)
        # One BooleanVar per object type; True = show that type
        self._type_vars: dict[str, tk.BooleanVar] = {
            t: tk.BooleanVar(value=True) for t in TYPE_COLORS
        }
        self._search_var = tk.StringVar()
        self._selected_index = None
        self._after_id = None
        self._current_map_raw = ""

        # ── Feature state ──────────────────────────────────────────────────
        self._prev_objects: dict[int, dict] = {}
        self._history:      dict[int, list] = {}
        self._pinned:       set[int]         = set()
        self._flag_alerts:  list[tuple]      = []
        # spawn/death log: list of (timestamp, 'spawn'|'death', index, type, tag)
        self._spawn_log:    list[tuple]      = []
        # cluster log: list of (timestamp, index, old_cluster, new_cluster)
        self._cluster_log:  list[tuple]      = []
        # birth time: {index: time.time()} when object first appeared
        self._birth_time:   dict[int, float] = {}
        # known index set from previous tick for spawn/death detection
        self._prev_indices: set[int]         = set()

        self._init_grid_state()
        self._build_ui()
        self._try_auto_connect()


    def _on_map_change(self, map_str: str):
        """Called when the map scenario string changes in memory."""
        self._current_map_raw = map_str
        found = resolve_map_tags(map_str)
        disp  = _tag_db._active_map_name
        color = "#4caf50" if found else "#EF9F27"
        self._map_lbl.config(text=f"Map: {disp}", foreground=color)
        if not found:
            self._bottom_lbl.config(text=f"No tag database for: {map_str}")
        # Clear per-map state on level change
        self._history.clear()
        self._prev_objects.clear()
        self._flag_alerts.clear()
        self._pinned.clear()
        self._spawn_log.clear()
        self._cluster_log.clear()
        self._birth_time.clear()
        self._prev_indices.clear()
        self._aup_selected_index = None
        if hasattr(self, '_aup_btn'):
            self._aup_btn.config(state=tk.DISABLED)
            self._aup_status_lbl.config(text="No unit selected.", foreground="#9898b8")
        self._cheats_selected_index = None
        if hasattr(self, '_cheats_tree'):
            for btn in self._cheats_action_buttons():
                btn.config(state=tk.DISABLED)
            self._cheats_sel_lbl.config(text="No unit selected.", foreground="#9898b8")
            self._cheats_action_lbl.config(text="")
        if hasattr(self, '_player_data'):
            self._player_data.clear()
        if hasattr(self, '_scripts_db'):
            self._scripts_on_map_change(map_str)

    # ── UI construction ────────────────────────────────────────────────────────


    def _build_ui(self):
        # ── Colour palette ─────────────────────────────────────────────────
        BG       = "#0d0d12"   # window / frame background
        BG2      = "#14141c"   # widget surface (tree, text areas)
        BG3      = "#1c1c28"   # slightly raised surface (headings, buttons)
        BG4      = "#22223a"   # hover / active
        BORDER   = "#2e2e48"   # borders and separators
        SEL_BG   = "#1e3a6e"   # selection highlight
        FG       = "#e8e8f0"   # primary text — high contrast
        FG2      = "#9898b8"   # secondary text (labels, hints)
        FG3      = "#5a5a7a"   # tertiary (disabled, timestamps)
        ACC      = "#5b9bd5"   # accent blue (addresses, links)
        self.configure(bg=BG)

        style = ttk.Style(self)
        style.theme_use("clam")

        # Global defaults
        style.configure(".",
                        background=BG, foreground=FG,
                        fieldbackground=BG2,
                        bordercolor=BORDER,
                        troughcolor=BG2,
                        selectbackground=SEL_BG, selectforeground=FG,
                        font=("Consolas", 10))

        # Frames & labels
        style.configure("TFrame",       background=BG)
        style.configure("TLabel",       background=BG, foreground=FG)
        style.configure("TSeparator",   background=BORDER)
        style.configure("TCheckbutton", background=BG, foreground=FG2)
        style.configure("TRadiobutton", background=BG, foreground=FG2)

        # Buttons — clearly visible on dark bg
        style.configure("TButton",
                        background=BG3, foreground=FG,
                        bordercolor=BORDER,
                        lightcolor=BG4, darkcolor=BG2,
                        padding=(6, 3))
        style.map("TButton",
                  background=[("active", BG4), ("pressed", BG2)],
                  foreground=[("active", FG)])

        # Entry / Spinbox
        style.configure("TEntry",
                        fieldbackground=BG2, foreground=FG,
                        insertcolor=FG, bordercolor=BORDER)
        style.configure("TSpinbox",
                        fieldbackground=BG2, foreground=FG,
                        insertcolor=FG, bordercolor=BORDER,
                        arrowcolor=FG2)

        # Combobox
        style.configure("TCombobox",
                        fieldbackground=BG2, foreground=FG,
                        selectbackground=SEL_BG, selectforeground=FG,
                        bordercolor=BORDER)
        style.map("TCombobox",
                  fieldbackground=[("readonly", BG2)],
                  foreground=[("readonly", FG)])

        # Treeview — main object list
        style.configure("Treeview",
                        background=BG2, foreground=FG,
                        fieldbackground=BG2, rowheight=22,
                        font=("Consolas", 10))
        style.configure("Treeview.Heading",
                        background=BG3, foreground=FG,
                        relief="flat", bordercolor=BORDER,
                        font=("Consolas", 10, "bold"))
        style.map("Treeview",
                  background=[("selected", SEL_BG)],
                  foreground=[("selected", "#ffffff")])
        style.map("Treeview.Heading",
                  background=[("active", BG4)])

        # Notebook tabs — high contrast selected vs unselected
        style.configure("TNotebook",
                        background=BG, bordercolor=BORDER,
                        tabmargins=(2, 2, 0, 0))
        style.configure("TNotebook.Tab",
                        background=BG3, foreground=FG2,
                        padding=(10, 4),
                        bordercolor=BORDER,
                        font=("Consolas", 10))
        style.map("TNotebook.Tab",
                  background=[("selected", SEL_BG), ("active", BG4)],
                  foreground=[("selected", "#ffffff"), ("active", FG)],
                  expand=[("selected", (1, 1, 1, 0))])

        # Scrollbar
        style.configure("TScrollbar",
                        background=BG3, troughcolor=BG2,
                        bordercolor=BORDER, arrowcolor=FG2)
        style.map("TScrollbar",
                  background=[("active", BG4)])

        # PanedWindow sash
        style.configure("TPanedwindow", background=BORDER)

        # ── Top bar ────────────────────────────────────────────────────────────
        top = ttk.Frame(self)
        top.pack(fill=tk.X, padx=10, pady=(8, 0))

        ttk.Label(top, text="Process:").pack(side=tk.LEFT, padx=(0, 4))
        self._proc_var = tk.StringVar()
        self._proc_combo = ttk.Combobox(top, textvariable=self._proc_var,
                                        width=32, state="readonly")
        self._proc_combo.pack(side=tk.LEFT, padx=(0, 4))

        ttk.Button(top, text="⟳ Refresh", command=self._refresh_processes).pack(
            side=tk.LEFT, padx=(0, 4))
        self._connect_btn = ttk.Button(top, text="Connect", command=self._connect)
        self._connect_btn.pack(side=tk.LEFT, padx=(0, 12))

        self._status_lbl = ttk.Label(top, text="● Disconnected",
                                     foreground="#cc4444", font=("Consolas", 10))
        self._status_lbl.pack(side=tk.LEFT)

        # Stats on right
        self._stat_lbl = ttk.Label(top, text="", foreground="#9898b8",
                                   font=("Consolas", 10))
        self._stat_lbl.pack(side=tk.RIGHT)

        self._map_lbl = ttk.Label(top, text="Map: —", foreground="#9898b8",
                                   font=("Consolas", 10))
        self._map_lbl.pack(side=tk.RIGHT, padx=(0, 16))

        # ── Top-level notebook: Objects | AUP ─────────────────────────────────
        self._main_nb = ttk.Notebook(self)
        self._main_nb.pack(fill=tk.BOTH, expand=True, padx=10, pady=(6, 0))

        tab_objects = ttk.Frame(self._main_nb)
        self._main_nb.add(tab_objects, text="Objects")

        tab_aup = ttk.Frame(self._main_nb)
        self._main_nb.add(tab_aup, text="AUP")
        self._build_aup_panel(tab_aup)

        tab_map = ttk.Frame(self._main_nb)
        self._main_nb.add(tab_map, text="Map")
        self._build_map_panel(tab_map)

        tab_player = ttk.Frame(self._main_nb)
        self._main_nb.add(tab_player, text="Player")
        self._build_player_panel(tab_player)

        tab_scripts = ttk.Frame(self._main_nb)
        self._main_nb.add(tab_scripts, text="Scripts")
        self._build_scripts_panel(tab_scripts)

        tab_bsp = ttk.Frame(self._main_nb)
        self._main_nb.add(tab_bsp, text="BSP")
        self._build_bsp_panel(tab_bsp)

        tab_cheats = ttk.Frame(self._main_nb)
        self._main_nb.add(tab_cheats, text="Cheats")
        self._build_cheats_panel(tab_cheats)

        # ── Filter bar (inside Objects tab) ────────────────────────────────────
        fbar = ttk.Frame(tab_objects)
        fbar.pack(fill=tk.X, pady=(6, 4))

        # ── Type checkbox row ───────────────────────────────────────────────
        type_row = tk.Frame(tab_objects, bg="#0d0d12")
        type_row.pack(fill=tk.X, padx=4, pady=(0, 4))

        def _all_types():
            for v in self._type_vars.values():
                v.set(True)
            self._apply_filter()

        def _no_types():
            for v in self._type_vars.values():
                v.set(False)
            self._apply_filter()

        tk.Button(
            type_row, text="All", font=("Consolas", 7), bg="#1e1e2e", fg="#aaaacc",
            relief=tk.FLAT, padx=4, pady=1, cursor="hand2",
            command=_all_types,
        ).pack(side=tk.LEFT, padx=(0, 2))
        tk.Button(
            type_row, text="None", font=("Consolas", 7), bg="#1e1e2e", fg="#aaaacc",
            relief=tk.FLAT, padx=4, pady=1, cursor="hand2",
            command=_no_types,
        ).pack(side=tk.LEFT, padx=(0, 8))

        for type_name, color in TYPE_COLORS.items():
            var = self._type_vars[type_name]
            cb = tk.Checkbutton(
                type_row,
                text=type_name,
                variable=var,
                command=self._apply_filter,
                font=("Consolas", 7),
                bg="#0d0d12",
                fg=color,
                selectcolor="#0d0d12",
                activebackground="#0d0d12",
                activeforeground=color,
                relief=tk.FLAT,
                bd=0,
            )
            cb.pack(side=tk.LEFT, padx=(0, 6))

        ttk.Checkbutton(fbar, text="Active only", variable=self._filter_active,
                        command=self._apply_filter).pack(side=tk.LEFT, padx=(0, 12))

        ttk.Label(fbar, text="Search:").pack(side=tk.LEFT, padx=(0, 4))
        self._search_entry = ttk.Entry(fbar, textvariable=self._search_var, width=20)
        self._search_entry.pack(side=tk.LEFT)
        self._search_var.trace_add("write", lambda *_: self._apply_filter())

        # View toggle
        self._obj_toggle_btn = ttk.Button(
            fbar, text="⊞ Grid", width=8, command=self._obj_toggle_view)
        self._obj_toggle_btn.pack(side=tk.RIGHT, padx=(0, 6))

        # Interval control
        ttk.Label(fbar, text="   Interval:").pack(side=tk.LEFT)
        self._interval_var = tk.IntVar(value=500)
        iv = ttk.Spinbox(fbar, from_=100, to=5000, increment=100,
                         textvariable=self._interval_var, width=6)
        iv.pack(side=tk.LEFT, padx=(4, 2))
        ttk.Label(fbar, text="ms").pack(side=tk.LEFT)

        # ── Main pane split (inside Objects tab) ───────────────────────────────
        pane = ttk.PanedWindow(tab_objects, orient=tk.HORIZONTAL)
        pane.pack(fill=tk.BOTH, expand=True, pady=(0, 4))

        # Left: object list
        left = ttk.Frame(pane)
        pane.add(left, weight=3)

        # Wrap tree + scrollbar in a frame so the grid view can swap with it
        self._obj_tree_frame = tk.Frame(left, bg="#0d0d12")
        self._obj_tree_frame.pack(fill=tk.BOTH, expand=True)

        cols = ("idx", "type", "active", "cluster", "addr",
                "origin", "health", "shields", "speed", "delta", "flags")
        self._tree = ttk.Treeview(self._obj_tree_frame, columns=cols, show="headings",
                                  selectmode="browse")

        col_cfg = [
            ("idx",     "Idx",     48,  tk.W),
            ("type",    "Type",    110, tk.W),
            ("active",  "Act",     30,  tk.CENTER),
            ("cluster", "Clust",   48,  tk.E),
            ("addr",    "Address", 88,  tk.W),
            ("origin",  "Origin (x, y, z)",   190, tk.W),
            ("health",  "HP",      44,  tk.CENTER),
            ("shields", "SH",      44,  tk.CENTER),
            ("speed",   "|v|",     56,  tk.E),
            ("delta",   "Δpos",    60,  tk.E),
            ("flags",   "Flags",   52,  tk.W),
        ]
        for col, heading, width, anchor in col_cfg:
            self._tree.heading(col, text=heading,
                               command=lambda c=col: self._sort_by(c))
            self._tree.column(col, width=width, anchor=anchor, minwidth=30)

        vsb = ttk.Scrollbar(self._obj_tree_frame, orient=tk.VERTICAL, command=self._tree.yview)
        self._tree.configure(yscrollcommand=vsb.set)
        self._tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self._tree.bind("<<TreeviewSelect>>", self._on_select)
        # Arrow keys: let Tk move the selection first (return "break" stops
        # the default scroll-jump), then fire _on_select on the next tick
        self._tree.bind("<Up>",   self._arrow_up)
        self._tree.bind("<Down>", self._arrow_down)
        # Clicking the tree gives it keyboard focus so arrows work immediately
        self._tree.bind("<Button-1>", lambda e: self._tree.focus_set())

        # Row tags for type coloring
        for tname, color in TYPE_COLORS.items():
            self._tree.tag_configure(tname, foreground=color)
        self._tree.tag_configure("inactive",  foreground="#3a3a5a")
        self._tree.tag_configure("teleport",  foreground="#EF9F27", background="#2a1f00")
        self._tree.tag_configure("pinned",    foreground="#ffffff", background="#1a2d50")

        # Right: detail panel
        right = ttk.Frame(pane)
        pane.add(right, weight=2)
        self._build_detail_panel(right)

        # ── Bottom status bar ──────────────────────────────────────────────────
        bot = ttk.Frame(self, relief=tk.SUNKEN)
        bot.pack(fill=tk.X, side=tk.BOTTOM, padx=0)
        self._bottom_lbl = ttk.Label(bot,
            text="Not connected. Select a process and click Connect.",
            foreground="#9898b8", font=("Consolas", 9))
        self._bottom_lbl.pack(side=tk.LEFT, padx=6, pady=2)
        self._fps_lbl = ttk.Label(bot, text="", foreground="#9898b8",
                                  font=("Consolas", 9))
        self._fps_lbl.pack(side=tk.RIGHT, padx=6)

        self._refresh_processes()


    def _refresh_processes(self):
        procs = list_processes()
        procs.sort(key=lambda x: x[1].lower())
        items = [f"{name}  (pid {pid})" for pid, name in procs]
        self._proc_combo["values"] = items
        self._proc_map = {f"{name}  (pid {pid})": pid for pid, name in procs}

        # Auto-select Halo2/Xenia if found
        pid, name = find_halo2_pid()
        if pid:
            key = f"{name}  (pid {pid})"
            if key in self._proc_map:
                self._proc_var.set(key)

    def _try_auto_connect(self):
        pid, name = find_halo2_pid()
        if pid:
            self._connect_to(pid, name)

    def _connect(self):
        sel = self._proc_var.get()
        if not sel or sel not in self._proc_map:
            messagebox.showwarning("No process", "Select a process first.")
            return
        pid = self._proc_map[sel]
        name = sel.split("  (")[0]
        self._connect_to(pid, name)

    def _connect_to(self, pid, name):
        self._disconnect()
        try:
            self._mem = MemoryReader(pid)
            self._pid = pid
            self._running = True
            self._status_lbl.config(text=f"● Connected  {name} (pid {pid})",
                                    foreground="#4caf50")
            self._bottom_lbl.config(text=f"Reading from {name}, pid {pid}")
            # Read map string immediately on connect
            try:
                ms = self._mem.read_string(MAP_STRING_ADDR, MAP_STRING_MAXLEN) or ""
                if ms:
                    self._on_map_change(ms)
                    if hasattr(self, "_scripts_db"):
                        self._scripts_on_map_change(ms)
            except Exception:
                pass
            self._schedule_poll()
        except RuntimeError as e:
            messagebox.showerror("Connection failed", str(e))

    def _disconnect(self):
        self._running = False
        if self._after_id:
            self.after_cancel(self._after_id)
            self._after_id = None
        if self._mem:
            self._mem.close()
            self._mem = None
        self._status_lbl.config(text="● Disconnected", foreground="#cc4444")

    # ── Polling ────────────────────────────────────────────────────────────────

    def _schedule_poll(self):
        if not self._running:
            return
        interval = max(100, self._interval_var.get())
        self._after_id = self.after(interval, self._poll)

    def _poll(self):
        if not self._running or not self._mem:
            return
        t0 = time.perf_counter()
        try:
            objects, active_count, map_str = read_all_objects(self._mem)
            if map_str and map_str != self._current_map_raw:
                self._on_map_change(map_str)
            elif _tag_db._active_map_name:
                # Keep label current even if map string hasn't changed
                disp  = _tag_db._active_map_name
                color = "#4caf50" if _tag_db._active_tag_map else "#EF9F27"
                self._map_lbl.config(text=f"Map: {disp}", foreground=color)
            elapsed = time.perf_counter() - t0
            now = time.time()

            # ── Per-object derived data ────────────────────────────────────
            new_prev = {}
            for o in objects:
                idx   = o["index"]
                orig  = o.get("origin") or (None, None, None)
                flags = o.get("flags", 0)
                prev  = self._prev_objects.get(idx)

                # velocity magnitude
                vel = o.get("trans_vel") or (0.0, 0.0, 0.0)
                speed = math.sqrt(sum((v or 0.0)**2 for v in vel))
                o["speed"] = speed

                if prev:
                    p_orig = prev.get("origin") or (None, None, None)
                    # coordinate delta
                    if orig[0] is not None and p_orig[0] is not None:
                        dx = orig[0] - p_orig[0]
                        dy = orig[1] - p_orig[1]
                        dz = orig[2] - p_orig[2]
                        dist = math.sqrt(dx*dx + dy*dy + dz*dz)
                        o["pos_delta"] = (dx, dy, dz)
                        o["pos_delta_mag"] = dist
                        o["teleported"] = dist > TELEPORT_THRESHOLD
                    else:
                        o["pos_delta"] = None
                        o["pos_delta_mag"] = None
                        o["teleported"] = False

                    # flag change alert
                    p_flags = prev.get("flags", 0)
                    if flags != p_flags:
                        self._flag_alerts.append(
                            (now, idx, o.get("type","?"), p_flags, flags))
                        # Keep last 200 alerts
                        if len(self._flag_alerts) > 200:
                            self._flag_alerts = self._flag_alerts[-200:]
                else:
                    o["pos_delta"] = None
                    o["pos_delta_mag"] = None
                    o["teleported"] = False

                # state history
                hist = self._history.setdefault(idx, [])
                hist.append((now,
                             orig,
                             o.get("health"),
                             o.get("shields"),
                             speed,
                             flags))
                if len(hist) > HISTORY_MAX_TICKS:
                    del hist[0]

                # ── Cluster transition log ─────────────────────────────────
                if prev:
                    p_cluster = prev.get("cluster")
                    c_cluster = o.get("cluster")
                    if (p_cluster is not None and c_cluster is not None
                            and p_cluster != c_cluster):
                        self._cluster_log.append(
                            (now, idx, o.get("type","?"), p_cluster, c_cluster))
                        if len(self._cluster_log) > 500:
                            self._cluster_log = self._cluster_log[-500:]

                new_prev[idx] = o

            # ── Spawn / death detection ────────────────────────────────────
            cur_indices = {o["index"] for o in objects}
            spawned = cur_indices - self._prev_indices
            died    = self._prev_indices - cur_indices

            for idx in spawned:
                o = next((x for x in objects if x["index"] == idx), {})
                typ = o.get("type","?")
                tag = o.get("definition_tag","") or ""
                sfx = tag.split("]")[-1].strip() if "]" in tag else ""
                label = f"{typ}:{sfx}" if sfx else typ
                self._spawn_log.append((now, "spawn", idx, label))
                if len(self._spawn_log) > 500:
                    self._spawn_log = self._spawn_log[-500:]

            for idx in died:
                prev_o = self._prev_objects.get(idx, {})
                typ = prev_o.get("type","?")
                tag = prev_o.get("definition_tag","") or ""
                sfx = tag.split("]")[-1].strip() if "]" in tag else ""
                label = f"{typ}:{sfx}" if sfx else typ
                self._spawn_log.append((now, "death", idx, label))
                if len(self._spawn_log) > 500:
                    self._spawn_log = self._spawn_log[-500:]
                # clean up birth record
                self._birth_time.pop(idx, None)

            self._prev_indices = cur_indices
            self._prev_objects = new_prev
            self._objects = objects
            self._apply_filter()
            self._refresh_aup_list()
            self._refresh_cheats_list()
            self._map_tick()
            self._refresh_player_tab()
            self._scripts_tick()
            self._bsp_tick()
            n = len(objects)
            alert_str = f"  ⚑ {len(self._flag_alerts)}" if self._flag_alerts else ""
            self._stat_lbl.config(
                text=f"{n} objects  ({active_count} active){alert_str}")
            self._fps_lbl.config(text=f"read {elapsed*1000:.0f} ms")
            self._update_detail_if_selected()
        except Exception as e:
            self._bottom_lbl.config(text=f"Read error: {e}")
        self._schedule_poll()

    # ── Filtering + display ────────────────────────────────────────────────────


    def on_closing(self):
        self._running = False
        if self._after_id:
            self.after_cancel(self._after_id)
        if self._mem:
            self._mem.close()
        self.destroy()




# ── Entry point ────────────────────────────────────────────────────────────

def main():
    if sys.platform != "win32":
        print("This tool requires Windows (ReadProcessMemory API).")
        print("It is designed to attach to Halo 2 running in Xenia or XQEMU.")
        sys.exit(1)
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()


if __name__ == "__main__":
    main()
