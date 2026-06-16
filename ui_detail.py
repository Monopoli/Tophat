"""Halo 2 Xbox Object Monitor — detail panel mixin (all tabs)."""
import math
import datetime
import tkinter as tk
from tkinter import ttk
from constants import HEADER_FLAG_NAMES, TYPE_COLORS
from tag_database import tag_name_from_datum


class DetailMixin:
    """Detail panel: Fields, History, Alerts, Spawn Log, Clusters, Vectors tabs."""

    def _build_detail_panel(self, parent):
        # ── Title row with pin button ──────────────────────────────────────
        title_row = ttk.Frame(parent)
        title_row.pack(fill=tk.X, pady=(6, 2), padx=8)

        self._detail_title = ttk.Label(
            title_row, text="— select an object —",
            font=("Consolas", 11, "bold"), foreground="#777")
        self._detail_title.pack(side=tk.LEFT)

        self._pin_btn = ttk.Button(title_row, text="📌 Pin",
                                   command=self._toggle_pin, width=7)
        self._pin_btn.pack(side=tk.RIGHT)

        sep = ttk.Separator(parent, orient=tk.HORIZONTAL)
        sep.pack(fill=tk.X, padx=8, pady=(2, 4))

        # ── HP/Shield bars ─────────────────────────────────────────────────
        self._bar_canvas = tk.Canvas(parent, height=44, bg="#0d0d12",
                                     highlightthickness=0)
        self._bar_canvas.pack(fill=tk.X, padx=8, pady=(0, 4))

        # ── Notebook: Fields / History / Alerts ───────────────────────────
        self._detail_nb = ttk.Notebook(parent)
        self._detail_nb.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 4))

        # Tab 1: fields
        tab_fields = ttk.Frame(self._detail_nb)
        self._detail_nb.add(tab_fields, text="Fields")

        frame = ttk.Frame(tab_fields)
        frame.pack(fill=tk.BOTH, expand=True)
        self._detail_text = tk.Text(
            frame, bg="#14141c", fg="#e8e8f0", font=("Consolas", 10),
            relief=tk.FLAT, state=tk.DISABLED, wrap=tk.NONE,
            insertbackground="#cccccc", cursor="arrow",
            padx=6, pady=4)
        vsb = ttk.Scrollbar(frame, orient=tk.VERTICAL,
                            command=self._detail_text.yview)
        self._detail_text.configure(yscrollcommand=vsb.set)
        self._detail_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)

        # Text tags
        for tag, fg in [("section","#4a4a7a"),("key","#7ab4e0"),("val","#e8e8f0"),
                        ("addr","#60a8f0"),("good","#3dcc96"),("bad","#f07878"),
                        ("warn","#f0b040"),("alert","#f0b040"),("tele","#f0b040")]:
            self._detail_text.tag_configure(tag, foreground=fg,
                font=("Consolas", 9, "bold") if tag == "section" else ("Consolas", 10))

        # Tab 2: history sparklines
        tab_hist = ttk.Frame(self._detail_nb)
        self._detail_nb.add(tab_hist, text="History")

        self._hist_canvas = tk.Canvas(tab_hist, bg="#0d0d12",
                                      highlightthickness=0)
        self._hist_canvas.pack(fill=tk.BOTH, expand=True)
        self._hist_canvas.bind("<Configure>", lambda e: self._redraw_history())

        # Tab 3: flag alerts
        tab_alerts = ttk.Frame(self._detail_nb)
        self._detail_nb.add(tab_alerts, text="Alerts")

        alert_ctrl = ttk.Frame(tab_alerts)
        alert_ctrl.pack(fill=tk.X, pady=(4, 0))
        ttk.Button(alert_ctrl, text="Clear alerts",
                   command=self._clear_alerts).pack(side=tk.LEFT, padx=4)

        af = ttk.Frame(tab_alerts)
        af.pack(fill=tk.BOTH, expand=True)
        self._alert_text = tk.Text(
            af, bg="#14141c", fg="#e8e8f0", font=("Consolas", 9),
            relief=tk.FLAT, state=tk.DISABLED, wrap=tk.NONE,
            padx=6, pady=4)
        avsb = ttk.Scrollbar(af, orient=tk.VERTICAL,
                             command=self._alert_text.yview)
        self._alert_text.configure(yscrollcommand=avsb.set)
        self._alert_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        avsb.pack(side=tk.RIGHT, fill=tk.Y)
        self._alert_text.tag_configure("ts",  foreground="#9898b8")
        self._alert_text.tag_configure("obj", foreground="#7fa8d0")
        self._alert_text.tag_configure("chg", foreground="#EF9F27")

        # Tab 4: spawn / death log
        tab_spawn = ttk.Frame(self._detail_nb)
        self._detail_nb.add(tab_spawn, text="Spawn Log")

        spawn_ctrl = ttk.Frame(tab_spawn)
        spawn_ctrl.pack(fill=tk.X, pady=(4, 0))
        ttk.Button(spawn_ctrl, text="Clear", width=7,
                   command=self._clear_spawn_log).pack(side=tk.LEFT, padx=4)
        self._spawn_filter_var = tk.StringVar(value="all")
        for val, lbl in [("all","All"),("spawn","Spawns"),("death","Deaths")]:
            ttk.Radiobutton(spawn_ctrl, text=lbl, variable=self._spawn_filter_var,
                            value=val,
                            command=self._refresh_spawn_tab).pack(side=tk.LEFT, padx=2)

        sf = ttk.Frame(tab_spawn)
        sf.pack(fill=tk.BOTH, expand=True)
        self._spawn_text = tk.Text(sf, bg="#14141c", fg="#e8e8f0",
                                   font=("Consolas", 9), relief=tk.FLAT,
                                   state=tk.DISABLED, wrap=tk.NONE, padx=6, pady=4)
        svsb = ttk.Scrollbar(sf, orient=tk.VERTICAL, command=self._spawn_text.yview)
        self._spawn_text.configure(yscrollcommand=svsb.set)
        self._spawn_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        svsb.pack(side=tk.RIGHT, fill=tk.Y)
        self._spawn_text.tag_configure("ts",    foreground="#9898b8")
        self._spawn_text.tag_configure("spawn", foreground="#5DCAA5")
        self._spawn_text.tag_configure("death", foreground="#F09595")
        self._spawn_text.tag_configure("label", foreground="#cccccc")

        # Tab 5: cluster transition log
        tab_clust = ttk.Frame(self._detail_nb)
        self._detail_nb.add(tab_clust, text="Clusters")

        clust_ctrl = ttk.Frame(tab_clust)
        clust_ctrl.pack(fill=tk.X, pady=(4, 0))
        ttk.Button(clust_ctrl, text="Clear", width=7,
                   command=self._clear_cluster_log).pack(side=tk.LEFT, padx=4)
        self._clust_all_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(clust_ctrl, text="All objects (not just selected)",
                        variable=self._clust_all_var,
                        command=self._refresh_cluster_tab).pack(side=tk.LEFT, padx=4)

        cf2 = ttk.Frame(tab_clust)
        cf2.pack(fill=tk.BOTH, expand=True)
        self._clust_text = tk.Text(cf2, bg="#14141c", fg="#e8e8f0",
                                   font=("Consolas", 9), relief=tk.FLAT,
                                   state=tk.DISABLED, wrap=tk.NONE, padx=6, pady=4)
        cvsb = ttk.Scrollbar(cf2, orient=tk.VERTICAL, command=self._clust_text.yview)
        self._clust_text.configure(yscrollcommand=cvsb.set)
        self._clust_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        cvsb.pack(side=tk.RIGHT, fill=tk.Y)
        self._clust_text.tag_configure("ts",  foreground="#9898b8")
        self._clust_text.tag_configure("obj", foreground="#7fa8d0")
        self._clust_text.tag_configure("trn", foreground="#EF9F27")
        self._clust_text.tag_configure("sel", foreground="#AFA9EC")

        # Tab 6: vector compass
        tab_vec = ttk.Frame(self._detail_nb)
        self._detail_nb.add(tab_vec, text="Vectors")
        self._vec_canvas = tk.Canvas(tab_vec, bg="#0d0d12", highlightthickness=0)
        self._vec_canvas.pack(fill=tk.BOTH, expand=True)
        self._vec_canvas.bind("<Configure>", lambda e: self._redraw_vectors())

    # ── Process management ─────────────────────────────────────────────────────

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

    def _apply_filter(self, *_):
        ftype   = self._filter_type.get()
        active  = self._filter_active.get()
        query   = self._search_var.get().lower().strip()

        filtered = []
        for o in self._objects:
            if ftype != "all" and o.get("type") != ftype:
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

    def _populate_tree(self, objects):
        # Preserve selection
        sel_iid = self._tree.selection()
        sel_tag = sel_iid[0] if sel_iid else None

        self._tree.delete(*self._tree.get_children())

        for o in objects:
            idx   = o.get("index", "?")
            typ   = o.get("type", "?")
            def_hint = o.get("definition_tag", "") or ""
            _sfx = def_hint.split("]")[-1].strip() if def_hint and "]" in def_hint else ""
            display_type = (typ + ":" + _sfx) if _sfx else typ
            act   = "✓" if o.get("active") else ""
            clust = str(o.get("cluster", "?"))
            addr  = f"0x{o.get('addr', 0):08X}"

            orig  = o.get("origin")
            if orig and orig[0] is not None:
                ox, oy, oz = orig
                orig_str = f"({ox:8.2f}, {oy:8.2f}, {oz:8.2f})"
            else:
                orig_str = "—"

            hp  = o.get("health")
            sh  = o.get("shields")
            hp_str  = f"{hp:.2f}" if hp is not None else "—"
            sh_str  = f"{sh:.2f}" if sh is not None else "—"

            spd = o.get("speed")
            spd_str = f"{spd:.3f}" if spd is not None else "—"

            dm  = o.get("pos_delta_mag")
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

            # Row colour: teleport = amber, pinned = blue, else type colour
            if idx in self._pinned:
                tag = "pinned"
            elif o.get("teleported"):
                tag = "teleport"
            elif not o.get("active"):
                tag = "inactive"
            else:
                tag = typ if typ in TYPE_COLORS else "inactive"

            iid = str(idx)
            self._tree.insert("", tk.END, iid=iid,
                values=(idx, display_type, act, clust, addr, orig_str,
                        hp_str, sh_str, spd_str, delta_str, flags_str),
                tags=(tag,))

        # Restore selection
        if sel_tag and self._tree.exists(sel_tag):
            self._tree.selection_set(sel_tag)
            self._tree.see(sel_tag)

    def _sort_by(self, col):
        data = [(self._tree.set(iid, col), iid)
                for iid in self._tree.get_children("")]
        try:
            data.sort(key=lambda x: float(x[0].replace("✓", "1").replace("—", "0")
                                          .replace("0x", "0")) if x[0] else 0)
        except ValueError:
            data.sort()
        for i, (_, iid) in enumerate(data):
            self._tree.move(iid, "", i)

    # ── Selection / detail ─────────────────────────────────────────────────────

    # ── Pin / history / alerts helpers ───────────────────────────────────────

    def _toggle_pin(self):
        idx = self._selected_index
        if idx is None:
            return
        if idx in self._pinned:
            self._pinned.discard(idx)
            self._pin_btn.config(text="📌 Pin")
        else:
            self._pinned.add(idx)
            self._pin_btn.config(text="📌 Unpin")

    def _clear_alerts(self):
        self._flag_alerts.clear()
        self._alert_text.config(state=tk.NORMAL)
        self._alert_text.delete("1.0", tk.END)
        self._alert_text.config(state=tk.DISABLED)

    def _update_alert_tab(self):
        """Refresh the Alerts text widget with current flag_alerts list."""
        txt = self._alert_text
        txt.config(state=tk.NORMAL)
        txt.delete("1.0", tk.END)
        import datetime
        for ts, idx, typ, old_f, new_f in reversed(self._flag_alerts[-100:]):
            t = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S.%f")[:-3]
            txt.insert(tk.END, f"{t}  ", "ts")
            txt.insert(tk.END, f"[{idx:04d}]{typ:<12} ", "obj")
            # decode flag bits
            def decode(f):
                bits = []
                for b, n in HEADER_FLAG_NAMES.items():
                    if f & (1 << b): bits.append(n)
                return ",".join(bits) or "none"
            txt.insert(tk.END,
                f"0x{old_f:02X}({decode(old_f)}) → 0x{new_f:02X}({decode(new_f)})\n",
                "chg")
        txt.config(state=tk.DISABLED)

    def _redraw_history(self):
        """Draw sparklines for the selected object's recorded history."""
        c = self._hist_canvas
        c.delete("all")
        idx = self._selected_index
        if idx is None:
            c.create_text(10, 10, text="No object selected",
                          fill="#9898b8", font=("Consolas", 10), anchor="nw")
            return
        hist = self._history.get(idx, [])
        if len(hist) < 2:
            c.create_text(10, 10, text="Collecting data…",
                          fill="#9898b8", font=("Consolas", 10), anchor="nw")
            return

        W = c.winfo_width()  or 400
        H = c.winfo_height() or 300
        pad_l, pad_r, pad_t, pad_b = 52, 8, 8, 8
        cw = W - pad_l - pad_r
        ch_each = max(40, (H - pad_t - pad_b - 24) // 4)  # 4 sparklines

        def sparkline(series, y_top, color, label, fmt="{:.2f}", fixed_min=None, fixed_max=None):
            vals = [v for v in series if v is not None]
            if not vals:
                return
            mn = fixed_min if fixed_min is not None else min(vals)
            mx = fixed_max if fixed_max is not None else max(vals)
            rng = mx - mn or 1.0
            n = len(series)

            # background
            c.create_rectangle(pad_l, y_top, pad_l+cw, y_top+ch_each,
                                fill="#0a0a14", outline="#1c1c2e")
            # label
            c.create_text(pad_l - 4, y_top + ch_each//2,
                          text=label, fill="#6060a0", font=("Consolas", 8),
                          anchor="e")
            # line
            pts = []
            for i, v in enumerate(series):
                if v is None: continue
                x = pad_l + int(i / max(n-1,1) * cw)
                y = y_top + ch_each - int((v - mn) / rng * (ch_each - 4)) - 2
                pts.append((x, y))
            if len(pts) >= 2:
                c.create_line(*[coord for pt in pts for coord in pt],
                              fill=color, width=1)
            # current value
            last = next((v for v in reversed(series) if v is not None), None)
            if last is not None:
                c.create_text(W - pad_r, y_top + ch_each//2,
                              text=fmt.format(last), fill=color,
                              font=("Consolas", 9), anchor="e")

        ticks   = len(hist)
        health  = [h[2] for h in hist]
        shields = [h[3] for h in hist]
        speeds  = [h[4] for h in hist]
        # Position delta between consecutive ticks
        deltas  = []
        for i in range(1, ticks):
            o1, o2 = hist[i-1][1], hist[i][1]
            if o1[0] is not None and o2[0] is not None:
                dx,dy,dz = o2[0]-o1[0], o2[1]-o1[1], o2[2]-o1[2]
                deltas.append(math.sqrt(dx*dx+dy*dy+dz*dz))
            else:
                deltas.append(None)
        deltas.insert(0, None)

        y = pad_t
        sparkline(health,  y, "#1D9E75", "HP",    "{:.2f}", 0.0, 1.0);  y += ch_each + 4
        sparkline(shields, y, "#185FA5", "SH",    "{:.2f}", 0.0, 1.0);  y += ch_each + 4
        sparkline(speeds,  y, "#7F77DD", "|v|",   "{:.3f}");             y += ch_each + 4
        sparkline(deltas,  y, "#EF9F27", "Δpos",  "{:.3f}")

        # tick count label
        duration = hist[-1][0] - hist[0][0]
        c.create_text(pad_l, H - 2,
                      text=f"{ticks} ticks  {duration:.1f}s",
                      fill="#3a3a5a", font=("Consolas", 8), anchor="sw")

    def _arrow_up(self, event):
        """Move selection up and update detail panel."""
        tree = self._tree
        sel  = tree.selection()
        if sel:
            prev = tree.prev(sel[0])
            if prev:
                tree.selection_set(prev)
                tree.see(prev)
                self._on_select()
        return "break"   # prevent default scroll-jump

    def _arrow_down(self, event):
        """Move selection down and update detail panel."""
        tree = self._tree
        sel  = tree.selection()
        if sel:
            nxt = tree.next(sel[0])
            if nxt:
                tree.selection_set(nxt)
                tree.see(nxt)
                self._on_select()
        return "break"   # prevent default scroll-jump

    def _on_select(self, _event=None):
        sel = self._tree.selection()
        if not sel:
            return
        iid = sel[0]
        try:
            idx = int(iid)
        except ValueError:
            return
        self._selected_index = idx
        # Update pin button label
        self._pin_btn.config(text="📌 Unpin" if idx in self._pinned else "📌 Pin")
        obj = next((o for o in self._objects if o.get("index") == idx), None)
        if obj and idx not in self._pinned:
            self._show_detail(obj)
        # Always redraw whichever tab is active
        tab = self._detail_nb.index(self._detail_nb.select())
        if tab == 1:
            self._redraw_history()
        elif tab == 2:
            self._update_alert_tab()

    def _update_detail_if_selected(self):
        if self._selected_index is None:
            return
        # Pinned objects: don't refresh the Fields tab, but do update
        # history sparklines and alerts regardless
        obj = next((o for o in self._objects
                    if o.get("index") == self._selected_index), None)
        if obj and self._selected_index not in self._pinned:
            self._show_detail(obj)
        # Always refresh the live tabs
        tab = self._detail_nb.index(self._detail_nb.select())
        if tab == 1:
            self._redraw_history()
        elif tab == 2:
            self._update_alert_tab()
        elif tab == 3:
            self._refresh_spawn_tab()
        elif tab == 4:
            self._refresh_cluster_tab()
        elif tab == 5:
            self._redraw_vectors()

    def _show_detail(self, o):
        typ  = o.get("type", "?")
        idx  = o.get("index", "?")
        salt = o.get("salt", 0)

        color = TYPE_COLORS.get(typ, "#aaaaaa")
        self._detail_title.config(
            text=f"[{idx:04d}:{salt:04X}]  {typ}",
            foreground=color)

        # Health/shield bars
        self._draw_bars(o)

        # Field dump
        txt = self._detail_text
        txt.config(state=tk.NORMAL)
        txt.delete("1.0", tk.END)

        def row(label, value, tag="val"):
            txt.insert(tk.END, f"  {label:<22}", "key")
            txt.insert(tk.END, f"{value}\n", tag)

        def section(title):
            txt.insert(tk.END, f"\n  {'─' * 40}\n", "section")
            txt.insert(tk.END, f"  {title}\n", "section")
            txt.insert(tk.END, f"  {'─' * 40}\n", "section")

        # Header datum
        section("s_object_header_datum")
        hflags = o.get("flags", 0)
        flag_names = [n for b, n in HEADER_FLAG_NAMES.items() if hflags & (1 << b)]
        row("salt",          f"0x{salt:04X}", "addr")
        row("flags",         f"0x{hflags:02X}  [{', '.join(flag_names) or 'none'}]")
        row("type (enum)",   f"{o.get('type_id', '?')}  →  {typ}")
        row("ClusterIndex",  str(o.get("cluster", "?")))
        row("Address",       f"0x{o.get('addr', 0):08X}", "addr")

        # s_object_data
        section("s_object_data")
        def_idx = o.get('definition', 0) or 0
        def_tag = o.get('definition_tag', '') or tag_name_from_datum(def_idx)
        row("Definition",    f"0x{def_idx:08X}  {def_tag}", "addr")
        row("PlacementIndex",str(o.get("placement_idx", "?")))
        row("NameListIndex", str(o.get("name_idx", "?")))

        orig = o.get("origin")
        if orig and orig[0] is not None:
            row("Origin",    f"({orig[0]:9.4f}, {orig[1]:9.4f}, {orig[2]:9.4f})")
        fwd = o.get("forward")
        if fwd and fwd[0] is not None:
            row("Forward",   f"({fwd[0]:9.4f}, {fwd[1]:9.4f}, {fwd[2]:9.4f})")
        up = o.get("up")
        if up and up[0] is not None:
            row("Up",        f"({up[0]:9.4f}, {up[1]:9.4f}, {up[2]:9.4f})")
        vel = o.get("trans_vel")
        if vel and vel[0] is not None:
            speed = o.get("speed") or math.sqrt(sum((v or 0)**2 for v in vel))
            row("Trans.Velocity", f"({vel[0]:7.4f}, {vel[1]:7.4f}, {vel[2]:7.4f})")
            spd_tag = "good" if speed < 0.5 else ("warn" if speed < 5.0 else "bad")
            row("Speed |v|",      f"{speed:.5f}  wu/tick", spd_tag)
        av = o.get("ang_vel")
        if av and av[0] is not None:
            row("Ang.Velocity",   f"({av[0]:7.4f}, {av[1]:7.4f}, {av[2]:7.4f})")

        dm = o.get("pos_delta_mag")
        if dm is not None:
            dd = o.get("pos_delta") or (0,0,0)
            tele = o.get("teleported", False)
            dtag = "tele" if tele else "val"
            prefix = "⚡ TELEPORT  " if tele else ""
            row("Pos delta",      f"{prefix}({dd[0]:7.3f},{dd[1]:7.3f},{dd[2]:7.3f})  |Δ|={dm:.4f}", dtag)

        sc = o.get("scale")
        row("Scale",     f"{sc:.4f}" if sc is not None else "—")


        # Vitality section
        hp  = o.get("health")
        sh  = o.get("shields")
        mv  = o.get("max_vit")
        cv  = o.get("cur_vit")
        if hp is not None:
            section("vitality")
            htag = "good" if (hp or 0) > 0.5 else ("warn" if (hp or 0) > 0.2 else "bad")
            stag = "good" if (sh or 0) > 0.5 else ("warn" if (sh or 0) > 0.2 else "bad")
            row("Health",          f"{(hp or 0):.4f}  ({(hp or 0)*100:.1f}%)", htag)
            row("Shields",         f"{(sh or 0):.4f}  ({(sh or 0)*100:.1f}%)", stag)
            row("MaximumVitality", f"{mv:.2f}" if mv is not None else "—")
            row("CurrentVitality", f"{cv:.2f}" if cv is not None else "—")

        # Flags
        cf = o.get("collision_flags")
        hf = o.get("health_flags")
        if cf is not None:
            section("flags (object_data)")
            row("CollisionFlags", f"0x{cf:02X}")
            row("HealthFlags",    f"0x{hf:02X}" if hf is not None else "—")

        # Parent linkage + object hierarchy tree
        parent_raw = o.get("parent_index") or 0xFFFFFFFF
        nxt = o.get("next_index") or 0xFFFFFFFF
        if parent_raw != 0xFFFFFFFF or nxt != 0xFFFFFFFF:
            section("datum linkage")
            if parent_raw != 0xFFFFFFFF:
                # In Halo 2, datum_index high-16 = salt (unique), low-16 = internal sub-index
                # Match parent by salt only since the low-16 doesn't equal the array slot
                p_salt = (parent_raw >> 16) & 0xFFFF
                p_obj  = next((x for x in self._objects if x.get("salt") == p_salt), None)
                if p_obj:
                    p_label = f"[{p_obj.get('index',0):04d}:{p_salt:04X}] {p_obj.get('type','?')}"
                else:
                    p_label = f"0x{parent_raw:08X}"
                row("ParentIndex",  p_label, "addr")
            if nxt != 0xFFFFFFFF:
                row("NextIndex",    f"0x{nxt:08X}", "addr")

        # Hierarchy tree: find children by matching parent_index high-16 (salt) to this object's salt
        my_idx  = o.get("index", -1)
        my_salt = o.get("salt", 0)
        children = [x for x in self._objects
                    if ((x.get("parent_index") or 0xFFFFFFFF) >> 16) & 0xFFFF == my_salt
                    and x.get("index") != my_idx]
        if children:
            section("children")
            for ch in children:
                cidx = ch.get("index", "?")
                ctyp = ch.get("type","?")
                ctag = ch.get("definition_tag","") or ""
                csfx = ctag.split("]")[-1].strip() if "]" in ctag else ""
                clabel = f"{ctyp}:{csfx}" if csfx else ctyp
                chp = ch.get("health")
                extras = []
                if chp is not None: extras.append(f"hp={chp:.2f}")
                extra_str = "  " + "  ".join(extras) if extras else ""
                row(f"  └─ [{cidx:04d}]", f"{clabel}{extra_str}", "addr")

        txt.config(state=tk.DISABLED)

    def _draw_bars(self, o):
        c = self._bar_canvas
        c.delete("all")
        w = c.winfo_width() or 300

        def bar(x, y, label, value, color_full, color_empty):
            bar_w = w - 90
            fill_w = int(bar_w * max(0.0, min(1.0, value or 0.0)))
            c.create_text(x, y + 7, text=label, fill="#777",
                          font=("Consolas", 9), anchor="e")
            c.create_rectangle(x+4, y, x+4+bar_w, y+14,
                                fill=color_empty, outline="")
            if fill_w > 0:
                c.create_rectangle(x+4, y, x+4+fill_w, y+14,
                                   fill=color_full, outline="")
            pct = f"{(value or 0)*100:.0f}%"
            c.create_text(x+4+bar_w+4, y+7, text=pct, fill="#aaaaaa",
                          font=("Consolas", 9), anchor="w")

        hp = o.get("health")
        sh = o.get("shields")
        bar(60, 4,  "HP", hp, "#2ab87a", "#0e2218")
        bar(60, 24, "SH", sh, "#3a80d0", "#081428")

    # ── Spawn log ─────────────────────────────────────────────────────────────

    def _clear_spawn_log(self):
        self._spawn_log.clear()
        self._refresh_spawn_tab()

    def _refresh_spawn_tab(self):
        import datetime
        filt = self._spawn_filter_var.get()
        txt  = self._spawn_text
        txt.config(state=tk.NORMAL)
        txt.delete("1.0", tk.END)
        for ts, kind, idx, label in reversed(self._spawn_log[-200:]):
            if filt != "all" and kind != filt:
                continue
            t = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S.%f")[:-3]
            icon = "+" if kind == "spawn" else "✕"
            txt.insert(tk.END, f"{t}  ", "ts")
            txt.insert(tk.END, f"{icon} ", kind)
            txt.insert(tk.END, f"[{idx:04d}] {label}\n", "label")
        txt.config(state=tk.DISABLED)

    # ── Cluster log ────────────────────────────────────────────────────────────

    def _clear_cluster_log(self):
        self._cluster_log.clear()
        self._refresh_cluster_tab()

    def _refresh_cluster_tab(self):
        import datetime
        show_all = self._clust_all_var.get()
        sel_idx  = self._selected_index
        txt      = self._clust_text
        txt.config(state=tk.NORMAL)
        txt.delete("1.0", tk.END)
        for entry in reversed(self._cluster_log[-300:]):
            ts, idx, typ, old_c, new_c = entry
            if not show_all and idx != sel_idx:
                continue
            t = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S.%f")[:-3]
            txt.insert(tk.END, f"{t}  ", "ts")
            tag = "sel" if idx == sel_idx else "obj"
            txt.insert(tk.END, f"[{idx:04d}]{typ:<12} ", tag)
            txt.insert(tk.END, f"cluster {old_c} \u2192 {new_c}\n", "trn")
        txt.config(state=tk.DISABLED)

    # ── Vector compass ─────────────────────────────────────────────────────────

    def _redraw_vectors(self):
        c = self._vec_canvas
        c.delete("all")
        W = c.winfo_width()  or 300
        H = c.winfo_height() or 300

        idx = self._selected_index
        if idx is None:
            c.create_text(W//2, H//2, text="No object selected",
                          fill="#9898b8", font=("Consolas", 10))
            return
        obj = next((o for o in self._objects if o.get("index") == idx), None)
        if not obj:
            c.create_text(W//2, H//2, text="Object not in current frame",
                          fill="#9898b8", font=("Consolas", 10))
            return

        fwd = obj.get("forward") or (None, None, None)
        vel = obj.get("trans_vel") or (None, None, None)
        spd = obj.get("speed") or 0.0

        if fwd[0] is None:
            c.create_text(W//2, H//2, text="No vector data",
                          fill="#9898b8", font=("Consolas", 10))
            return

        # ── Top-down (XY) compass ──────────────────────────────────────────
        cx, cy = W // 4, H // 2
        r = min(cx, cy) - 20

        # compass ring
        c.create_oval(cx-r, cy-r, cx+r, cy+r, outline="#1c1c2e", width=1)
        for deg, lbl in [(0,"N"),(90,"E"),(180,"S"),(270,"W")]:
            rad = math.radians(deg - 90)
            tx  = cx + (r + 10) * math.cos(rad)
            ty  = cy + (r + 10) * math.sin(rad)
            c.create_text(tx, ty, text=lbl, fill="#3a3a5a", font=("Consolas", 8))

        # Cross-hairs
        c.create_line(cx-r, cy, cx+r, cy, fill="#14141e")
        c.create_line(cx, cy-r, cx, cy+r, fill="#14141e")

        def draw_arrow(vec_x, vec_y, color, label, dash=()):
            # project XY plane (negate Y because screen Y is down)
            mag = math.sqrt(vec_x**2 + vec_y**2)
            if mag < 1e-6:
                return
            nx, ny = vec_x / mag, -vec_y / mag
            ex = cx + nx * r
            ey = cy + ny * r
            c.create_line(cx, cy, ex, ey, fill=color, width=2, dash=dash,
                          arrow=tk.LAST, arrowshape=(10, 12, 4))
            c.create_text(ex + nx * 12, ey + ny * 12, text=label,
                          fill=color, font=("Consolas", 8))

        # Forward vector (solid purple)
        draw_arrow(fwd[0], fwd[1], "#7F77DD", "Fwd")

        # Velocity vector (amber dashed) - only if moving
        if vel[0] is not None and spd > 0.001:
            draw_arrow(vel[0], vel[1], "#EF9F27", "Vel", dash=(4, 2))

        c.create_text(cx, cy - r - 18, text="Top-down (XY)",
                      fill="#3a3a5a", font=("Consolas", 8))

        # ── Side-view (XZ) ────────────────────────────────────────────────
        cx2 = (W * 3) // 4
        c.create_oval(cx2-r, cy-r, cx2+r, cy+r, outline="#1c1c2e", width=1)
        c.create_line(cx2-r, cy, cx2+r, cy, fill="#14141e")
        c.create_line(cx2, cy-r, cx2, cy+r, fill="#14141e")
        for deg, lbl in [(0,"U"),(180,"D")]:
            rad = math.radians(deg - 90)
            tx  = cx2 + (r + 10) * math.cos(rad)
            ty  = cy  + (r + 10) * math.sin(rad)
            c.create_text(tx, ty, text=lbl, fill="#3a3a5a", font=("Consolas", 8))

        def draw_arrow_xz(vx, vz, color, label, dash=()):
            mag = math.sqrt(vx**2 + vz**2)
            if mag < 1e-6:
                return
            nx, nz = vx / mag, -vz / mag
            ex = cx2 + nx * r
            ey = cy  + nz * r
            c.create_line(cx2, cy, ex, ey, fill=color, width=2, dash=dash,
                          arrow=tk.LAST, arrowshape=(10, 12, 4))
            c.create_text(ex + nx * 12, ey + nz * 12, text=label,
                          fill=color, font=("Consolas", 8))

        draw_arrow_xz(fwd[0], fwd[2], "#7F77DD", "Fwd")
        if vel[0] is not None and spd > 0.001:
            draw_arrow_xz(vel[0], vel[2], "#EF9F27", "Vel", dash=(4, 2))

        c.create_text(cx2, cy - r - 18, text="Side-view (XZ)",
                      fill="#3a3a5a", font=("Consolas", 8))

        # ── Angle between forward and velocity ─────────────────────────────
        if vel[0] is not None and spd > 0.001:
            dot = sum((fwd[i] or 0) * (vel[i] or 0) for i in range(3))
            fmag = math.sqrt(sum((fwd[i] or 0)**2 for i in range(3)))
            vmag = spd
            if fmag > 1e-6 and vmag > 1e-6:
                cos_a = max(-1.0, min(1.0, dot / (fmag * vmag)))
                angle = math.degrees(math.acos(cos_a))
                aligned = angle < 15
                col = "#5DCAA5" if aligned else ("#EF9F27" if angle < 45 else "#F09595")
                c.create_text(W//2, H - 24,
                              text=f"Fwd∠Vel = {angle:.1f}°  {'(aligned)' if aligned else ''}",
                              fill=col, font=("Consolas", 10))

        # ── Speed readout ──────────────────────────────────────────────────
        c.create_text(W//2, H - 8,
                      text=f"|v| = {spd:.4f} wu/tick",
                      fill="#6060a0", font=("Consolas", 9))

        # ── Legend ─────────────────────────────────────────────────────────
        lx, ly = 8, 8
        c.create_line(lx, ly+4, lx+18, ly+4, fill="#7F77DD", width=2,
                      arrow=tk.LAST, arrowshape=(6,8,3))
        c.create_text(lx+22, ly+4, text="Forward", fill="#7F77DD",
                      font=("Consolas", 8), anchor="w")
        c.create_line(lx, ly+16, lx+18, ly+16, fill="#EF9F27", width=2,
                      dash=(4,2), arrow=tk.LAST, arrowshape=(6,8,3))
        c.create_text(lx+22, ly+16, text="Velocity", fill="#EF9F27",
                      font=("Consolas", 8), anchor="w")

    # ── Map-change reset ───────────────────────────────────────────────────────

