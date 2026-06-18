"""
Halo 2 Xbox Object Monitor — Tags tab.

Parses `weap` (weapon) tag definitions out of a static Halo 2 Xbox .map file,
locates their `proj` (projectile) tag-reference field(s), and lets you queue
up "swap this weapon's projectile for a different one" edits and save them
to a new copy of the map file.

Drop-in pattern note
---------------------
This follows the same "open the .map file directly" approach as ui_bsp.py /
cluster_portals.py / trigger_volumes.py, NOT the live ReadProcessMemory path
used by ui_objects.py / ui_aup.py / ui_player.py. There is no known live
address for the tag array in Xbox guest memory anywhere in this project
(constants.py only has ARRAY_BASE for *objects*), so weapon-tag content is
only readable from a .map file on disk, exactly like BSP geometry, trigger
volumes, and cluster portals already are.

Where the field offsets come from
-----------------------------------
/mnt/project/WeaponStructure.txt is an Assembly-style Halo 2 tag-plugin XML
that documents the full `weap` struct layout. Per that file:

    <tagblock name="Barrels" offset="0x2D0" elementSize="0xEC"> ... </tagblock>
      <tagRef name="Projectile" offset="0x8C" visible="true" />   (inside Barrels)

i.e. a weap tag has an 8-byte tagblock header at struct offset 0x2D0
([count: u32][pointer: u32]), each Barrel element is 0xEC bytes, and each
Barrel's Projectile tagRef sits at +0x8C within that element. Since
`withGroup` isn't set to "false" on that tagRef, it defaults to true, so the
field is 8 bytes: a 4-byte tag-group FourCC plus a 4-byte datum index (per
the same withGroup convention documented in scnrstructure.txt for the scnr
tag). This replaces the earlier version of this module, which had no
documented offset for `weap` and instead heuristically scanned every
4-byte-aligned position in a weapon's raw bytes for a value matching a known
proj-tag datum — that approach is no longer used now that the real offset is
known.

Two things are still inferred rather than hard-coded, both narrow and
self-checking rather than blind guesses:

  1. Tagblock pointer resolution. A tagblock's "pointer" field needs to be
     turned into a byte position in the file. cluster_portals.py already
     established — and validated against a real 01b_spacestation map — that
     these pointers are plain absolute indices into the full tag-data heap
     (the same buffer this module reads as `tag_section`, starting at
     tag_file_off): see its CLUSTERS/portal-vertex reflexive math, where
     `cluster_ptr - sbsp_voff` recovers an offset relative to the owning
     tag's own meta, which is algebraically the same statement as "cluster_ptr
     is already a tag_section-relative index". This module reuses that exact
     convention for the Barrels tagblock. It was validated for a different
     tag type (sbsp) in this same file format, not specifically for weap, so
     treat it as a strong precedent rather than a certainty.

  2. The 8-byte tagRef's internal byte order (is the group FourCC first or
     the datum index first?). Neither scnrstructure.txt nor WeaponStructure.txt
     spells this out. _decode_projectile_tagref() below resolves this at
     parse time per field: it checks both 4-byte halves against the active
     map's known proj-tag datum indices and uses whichever half actually
     matches (falling back to a null-tag sentinel check, then to "unresolved"
     with the raw hex value shown rather than a silent guess). This is a much
     narrower ambiguity than the old approach — the field's *location* is now
     known for certain; only a single bit of byte-order remains self-detected.

As always: validate against a real loaded map before trusting a swap to
actually do what it says — queue an obvious swap, save a copy, and confirm in
a hex editor that only the expected 4 bytes changed before pointing Xenia at
the new file.

Public API
----------
  parse_weapon_tags(map_path)        -> list[WeaponTag]
  get_weapon_tags(map_path)          -> cached version
  get_projectile_choices(map_path)   -> list[(datum_index, short_name)], sorted by name
  write_patched_map_with_swaps(map_path, out_path, weapons, pending)
      writes a full copy of map_path to out_path with every queued swap
      patched in. Never touches map_path itself.
"""

import os
import struct
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from tag_database import resolve_map_tags
import tag_database as _tag_db


# ── Low-level binary helpers (same conventions as ui_bsp.py / cluster_portals.py) ──

def _ri32(d, o):
    return struct.unpack_from('<I', d, o)[0]


def _read_4cc(d, o):
    return d[o:o + 4][::-1].decode('ascii', errors='replace')


# ── Structural constants for the `weap` tag (from WeaponStructure.txt) ──────

BARRELS_TAGBLOCK_OFFSET  = 0x2D0   # weap struct: tagblock header (count:u32, ptr:u32)
BARRELS_ELEMENT_SIZE     = 0xEC    # bytes per Barrel element
PROJECTILE_TAGREF_OFFSET = 0x8C    # Projectile tagRef offset within one Barrel element
TAGREF_SIZE              = 8       # withGroup=true tagRef: group FourCC (4) + datum (4)
_NULL_DATUMS             = (0, 0xFFFFFFFF)   # conventional "no tag assigned" sentinels


# ── Data classes ────────────────────────────────────────────────────────────

class ProjectileField:
    """One Barrel's Projectile tag-reference inside a weap tag."""
    __slots__ = ('barrel_index', 'offset', 'proj_datum', 'proj_name', 'status')

    def __init__(self, barrel_index, offset, proj_datum, proj_name, status):
        self.barrel_index = barrel_index  # which Barrel element (0, 1, ...)
        self.offset        = offset        # abs index into tag_section of the datum word
                                            # (i.e. file offset = tag_file_off + offset)
        self.proj_datum     = proj_datum    # current datum_index value at that offset
        self.proj_name       = proj_name     # resolved short_name, or a raw-hex fallback
        self.status           = status        # 'resolved' | 'no_projectile' | 'unresolved'


class WeaponTag:
    """One `weap` tag instance found in the loaded map's tag array."""
    __slots__ = (
        'datum_index', 'name', 'full_path', 'tag_entry_index',
        'voff', 'size', 'name_resolved', 'projectile_fields', 'tag_file_off',
    )

    def __init__(self, datum_index, name, full_path, tag_entry_index,
                 voff, size, name_resolved, projectile_fields, tag_file_off):
        self.datum_index       = datum_index       # None if name lookup failed
        self.name               = name
        self.full_path          = full_path
        self.tag_entry_index    = tag_entry_index   # position in the file's tag array
        self.voff                = voff             # meta offset from tag_file_off
        self.size                = size              # meta byte length
        self.name_resolved       = name_resolved
        self.projectile_fields   = projectile_fields  # list[ProjectileField], one per Barrel
        self.tag_file_off        = tag_file_off         # for display: file offset = this + field.offset


# ── Map-file scoped tag-database lookup ───────────────────────────────────────

def _scenario_path_from_file(map_path: str) -> str:
    with open(map_path, 'rb') as f:
        hdr = f.read(0x800)
    return hdr[0x1C8:0x208].split(b'\x00')[0].decode('ascii', errors='replace')


def _resolve_for_file(scenario_path: str) -> dict:
    """Resolve scenario_path to its tag dict via tag_database.resolve_map_tags(),
    WITHOUT disturbing the live _active_tag_map / _active_map_name globals that
    the Objects/Detail tabs rely on for whatever map a connected game process
    is actually on right now. The .map file loaded here is a user-chosen file
    on disk and may not match — or there may be no live connection at all
    (this whole module works fine offline, like the BSP tab)."""
    saved_map  = _tag_db._active_tag_map
    saved_name = _tag_db._active_map_name
    try:
        resolve_map_tags(scenario_path)
        return dict(_tag_db._active_tag_map)
    finally:
        _tag_db._active_tag_map  = saved_map
        _tag_db._active_map_name = saved_name


# ── Tagblock / tagRef resolution ─────────────────────────────────────────────

def _read_tagblock_header(tag_section: bytes, struct_abs_off: int, field_offset: int):
    """Read an 8-byte tagblock header (count:u32, ptr:u32) at
    struct_abs_off + field_offset. `ptr`, per the convention validated in
    cluster_portals.py for this same map-file format, is a direct absolute
    index into tag_section (not relative to anything else)."""
    hdr_off = struct_abs_off + field_offset
    if hdr_off + 8 > len(tag_section):
        return 0, None
    count = _ri32(tag_section, hdr_off)
    ptr   = _ri32(tag_section, hdr_off + 4)
    if count <= 0 or ptr <= 0:
        return 0, None
    return count, ptr


def _decode_projectile_tagref(tag_section: bytes, tagref_abs_off: int, active: dict):
    """Decode the 8-byte [group][datum] (or [datum][group]) tagRef at
    tagref_abs_off. Tries both 4-byte halves against the active map's known
    proj-tag datum indices and uses whichever one actually resolves; falls
    back to a null-tag sentinel check, then to a raw/unresolved result.
    Returns (datum_value, datum_abs_off, status, name) — datum_abs_off is
    the exact absolute position of the matched 4-byte word, which may be
    tagref_abs_off or tagref_abs_off + 4 depending on which half matched."""
    word0 = _ri32(tag_section, tagref_abs_off)
    word1 = _ri32(tag_section, tagref_abs_off + 4)

    hit1 = active.get(word1)
    if hit1 and hit1[0] == 'proj':
        return word1, tagref_abs_off + 4, 'resolved', hit1[1]
    hit0 = active.get(word0)
    if hit0 and hit0[0] == 'proj':
        return word0, tagref_abs_off, 'resolved', hit0[1]

    # Conventional slot for a bare datum in a [group][datum] layout is the
    # second word; check it first for the "no projectile assigned" sentinel.
    if word1 in _NULL_DATUMS:
        return word1, tagref_abs_off + 4, 'no_projectile', '(none)'
    if word0 in _NULL_DATUMS:
        return word0, tagref_abs_off, 'no_projectile', '(none)'

    # Neither half is a known proj tag nor a null sentinel — surface the
    # conventional (+4) word's raw value rather than silently guessing.
    return word1, tagref_abs_off + 4, 'unresolved', f'0x{word1:08X} (unresolved)'


# ── Parser ─────────────────────────────────────────────────────────────────

def parse_weapon_tags(map_path: str) -> list[WeaponTag]:
    """Parse every `weap` tag in map_path and read its Barrels' Projectile
    tagRef field(s) per the documented WeaponStructure.txt layout. Returns
    [] on any structural failure (not a recognised Halo 2 Xbox v8 map,
    truncated file, etc.)."""
    try:
        with open(map_path, 'rb') as f:
            hdr = f.read(0x800)
        if _ri32(hdr, 0x004) != 8:
            return []

        scenario_path = hdr[0x1C8:0x208].split(b'\x00')[0].decode('ascii', errors='replace')
        active = _resolve_for_file(scenario_path)

        tag_file_off = _ri32(hdr, 0x010)
        tag_length   = _ri32(hdr, 0x014)
        with open(map_path, 'rb') as f:
            f.seek(tag_file_off)
            tag_section = f.read(tag_length)

        tag_entries_offset = _ri32(tag_section, 0x08)
        tag_count           = _ri32(tag_section, 0x18)

        # datum_index's low 16 bits are conventionally the tag's position in
        # the tag array (same salt:index split used for object datum indices
        # elsewhere in this project) — build a reverse lookup on that basis,
        # used only to resolve a weap tag's own display name.
        index_lookup = {
            datum & 0xFFFF: (datum, grp, short, path)
            for datum, (grp, short, path) in active.items()
        }

        weapons = []
        for i in range(tag_count):
            off = tag_entries_offset + i * 16
            if off + 16 > len(tag_section):
                break
            if _read_4cc(tag_section, off) != 'weap':
                continue

            voff = _ri32(tag_section, off + 8)
            size = _ri32(tag_section, off + 12)
            if size <= 0 or voff <= 0 or voff + size > len(tag_section):
                continue

            entry = index_lookup.get(i)
            if entry is not None and entry[1] == 'weap':
                datum_index, _grp, short_name, full_path = entry
                resolved = True
            else:
                datum_index, short_name, full_path = None, f'weap_{i:04d} (unresolved)', ''
                resolved = False

            fields = []
            count, ptr = _read_tagblock_header(tag_section, voff, BARRELS_TAGBLOCK_OFFSET)
            if count and ptr is not None and ptr + count * BARRELS_ELEMENT_SIZE <= len(tag_section):
                for bi in range(count):
                    barrel_off = ptr + bi * BARRELS_ELEMENT_SIZE
                    tagref_off = barrel_off + PROJECTILE_TAGREF_OFFSET
                    if tagref_off + TAGREF_SIZE > len(tag_section):
                        continue
                    datum, datum_off, status, name = _decode_projectile_tagref(
                        tag_section, tagref_off, active)
                    fields.append(ProjectileField(
                        barrel_index=bi, offset=datum_off,
                        proj_datum=datum, proj_name=name, status=status,
                    ))

            weapons.append(WeaponTag(
                datum_index=datum_index, name=short_name, full_path=full_path,
                tag_entry_index=i, voff=voff, size=size,
                name_resolved=resolved, projectile_fields=fields,
                tag_file_off=tag_file_off,
            ))

        weapons.sort(key=lambda w: w.name.lower())
        return weapons

    except Exception as e:
        print(f'Weapon tag parse error: {e}')
        return []


# ── Cache ──────────────────────────────────────────────────────────────────

_wt_cache: dict[str, list[WeaponTag]] = {}


def get_weapon_tags(map_path: str) -> list[WeaponTag]:
    if map_path not in _wt_cache:
        _wt_cache[map_path] = parse_weapon_tags(map_path)
    return _wt_cache.get(map_path, [])


def get_projectile_choices(map_path: str) -> list[tuple[int, str]]:
    """All proj-group tags known for map_path's scenario, as
    (datum_index, short_name), sorted by name."""
    scenario_path = _scenario_path_from_file(map_path)
    active = _resolve_for_file(scenario_path)
    return sorted(
        ((datum, short) for datum, (grp, short, path) in active.items() if grp == 'proj'),
        key=lambda t: t[1].lower(),
    )


# ── Writer ─────────────────────────────────────────────────────────────────

def write_patched_map_with_swaps(map_path: str, out_path: str,
                                  weapons: list[WeaponTag],
                                  pending: dict[tuple[int, int], int]) -> int:
    """Write a full copy of map_path to out_path with every queued swap
    patched into the relevant weap tag's Projectile tagRef datum word.
    `pending` maps (tag_entry_index, field_offset) -> new_datum_index, where
    field_offset is the absolute tag_section index recorded on the matching
    ProjectileField. Never writes to map_path itself. Returns the number of
    fields patched."""
    with open(map_path, 'rb') as f:
        hdr = f.read(0x800)
    tag_file_off = _ri32(hdr, 0x010)

    with open(map_path, 'rb') as f:
        data = bytearray(f.read())

    by_entry = {w.tag_entry_index: w for w in weapons}
    patched = 0
    for (entry_idx, offset), new_datum in pending.items():
        w = by_entry.get(entry_idx)
        if w is None:
            continue
        abs_off = tag_file_off + offset
        if abs_off + 4 > len(data):
            raise ValueError(f'Patch offset out of range for {w.name} @0x{offset:08X}')
        struct.pack_into('<I', data, abs_off, new_datum)
        patched += 1

    with open(out_path, 'wb') as f:
        f.write(data)
    return patched


# ── TagsMixin ────────────────────────────────────────────────────────────────

class TagsMixin:
    """Tags tab: load a .map file, list weap tags + their Barrels' projectile
    field(s), and queue/save projectile swaps."""

    def _build_tags_panel(self, parent):
        self._tags_map_path: str = ''
        self._tags_weapons: list[WeaponTag] = []
        self._tags_proj_choices: list[tuple[int, str]] = []
        self._tags_pending: dict[tuple[int, int], int] = {}   # (entry_idx, offset) -> new_datum
        self._tags_selected = None   # (WeaponTag, ProjectileField) | None

        # ── Description ──────────────────────────────────────────────────
        desc = ttk.Frame(parent)
        desc.pack(fill=tk.X, padx=12, pady=(10, 4))
        ttk.Label(desc,
                  text="Load a Halo 2 Xbox .map file, read each weap tag's Barrels for their "
                       "Projectile reference, and optionally queue a swap.",
                  foreground="#9898b8", font=("Consolas", 9)).pack(anchor="w")
        ttk.Label(desc,
                  text="Field location is from WeaponStructure.txt (documented offset, not a "
                       "scan) — see ui_tags.py module docstring for the one remaining "
                       "self-detected detail before relying on this for a real edit.",
                  foreground="#EF9F27", font=("Consolas", 9)).pack(anchor="w", pady=(2, 0))

        # ── Control bar ──────────────────────────────────────────────────
        ctrl = ttk.Frame(parent)
        ctrl.pack(fill=tk.X, padx=12, pady=(0, 6))
        ttk.Button(ctrl, text="Load .map file…",
                   command=self._tags_load_file).pack(side=tk.LEFT)
        self._tags_file_lbl = ttk.Label(ctrl, text="No .map loaded.",
                                         foreground="#9898b8", font=("Consolas", 9))
        self._tags_file_lbl.pack(side=tk.LEFT, padx=(8, 0))

        self._tags_stat_lbl = ttk.Label(ctrl, text="", foreground="#9898b8",
                                         font=("Consolas", 9))
        self._tags_stat_lbl.pack(side=tk.RIGHT)

        # ── Main split: weapon/field tree (left) + swap panel (right) ─────
        pane = ttk.PanedWindow(parent, orient=tk.HORIZONTAL)
        pane.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 10))

        left = ttk.Frame(pane)
        pane.add(left, weight=3)

        cols = ("field", "current_proj", "status", "addr")
        self._tags_tree = ttk.Treeview(left, columns=cols, show="tree headings",
                                        selectmode="browse")
        self._tags_tree.heading("#0", text="Weapon")
        self._tags_tree.column("#0", width=200, anchor=tk.W, minwidth=120)
        col_cfg = [
            ("field",        "Field",              90,  tk.W),
            ("current_proj", "Current Projectile", 200, tk.W),
            ("status",       "Status",             70,  tk.CENTER),
            ("addr",         "File Offset",         90,  tk.E),
        ]
        for col, heading, width, anchor in col_cfg:
            self._tags_tree.heading(col, text=heading)
            self._tags_tree.column(col, width=width, anchor=anchor, minwidth=40)

        vsb = ttk.Scrollbar(left, orient=tk.VERTICAL, command=self._tags_tree.yview)
        self._tags_tree.configure(yscrollcommand=vsb.set)
        self._tags_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)

        self._tags_tree.tag_configure("pending", foreground="#EF9F27")
        self._tags_tree.tag_configure("noproj",  foreground="#5a5a7a")
        self._tags_tree.tag_configure("unresolved", foreground="#f07878")
        self._tags_tree.bind("<<TreeviewSelect>>", self._tags_on_select)

        # ── Right: swap controls ───────────────────────────────────────────
        right = ttk.Frame(pane)
        pane.add(right, weight=2)

        ttk.Label(right, text="Selected field:", foreground="#9898b8",
                  font=("Consolas", 9)).pack(anchor="w", pady=(0, 2))
        self._tags_sel_lbl = ttk.Label(right, text="(none selected)",
                                        foreground="#e8e8f0", font=("Consolas", 10, "bold"),
                                        wraplength=260, justify=tk.LEFT)
        self._tags_sel_lbl.pack(anchor="w", pady=(0, 10))

        ttk.Label(right, text="New projectile:", foreground="#9898b8",
                  font=("Consolas", 9)).pack(anchor="w")
        self._tags_swap_var = tk.StringVar()
        self._tags_swap_combo = ttk.Combobox(right, textvariable=self._tags_swap_var,
                                              state="readonly", width=34)
        self._tags_swap_combo.pack(anchor="w", pady=(2, 8))

        self._tags_swap_btn = ttk.Button(right, text="Queue Swap",
                                          command=self._tags_queue_swap,
                                          state=tk.DISABLED)
        self._tags_swap_btn.pack(anchor="w")

        ttk.Separator(right, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=12)

        ttk.Label(right, text="Pending changes:", foreground="#9898b8",
                  font=("Consolas", 9)).pack(anchor="w")
        self._tags_pending_lbl = ttk.Label(right, text="none", foreground="#e8e8f0",
                                            font=("Consolas", 9), wraplength=260,
                                            justify=tk.LEFT)
        self._tags_pending_lbl.pack(anchor="w", pady=(2, 10))

        self._tags_save_btn = ttk.Button(right, text="Save Modified Copy As…",
                                          command=self._tags_save_modified,
                                          state=tk.DISABLED)
        self._tags_save_btn.pack(anchor="w", pady=(0, 4))
        ttk.Button(right, text="Discard Pending Changes",
                   command=self._tags_discard_pending).pack(anchor="w")

        ttk.Label(right,
                  text="Saves a new file — never overwrites the loaded .map.\n"
                       "Xenia has to load that new file to see the change;\n"
                       "this tool never touches a live process for tags.",
                  foreground="#5a5a7a", font=("Consolas", 8),
                  justify=tk.LEFT).pack(anchor="w", pady=(14, 0))

    # ── File loading ────────────────────────────────────────────────────────

    def _tags_load_file(self):
        path = filedialog.askopenfilename(
            title="Select Halo 2 Xbox .map file",
            filetypes=[("Map files", "*.map"), ("All files", "*.*")])
        if not path:
            return

        self._tags_map_path = path
        short = os.path.basename(path)
        self._tags_file_lbl.config(text=f"Loading {short}…")
        self.update_idletasks()

        self._tags_pending.clear()
        self._tags_selected = None
        self._tags_swap_btn.config(state=tk.DISABLED)
        self._tags_sel_lbl.config(text="(none selected)")

        weapons = get_weapon_tags(path)
        if not weapons:
            self._tags_file_lbl.config(
                text=f"No weap tags found in {short} (not a Halo 2 Xbox v8 map?)")
            self._tags_weapons = []
            self._tags_proj_choices = []
            self._tags_tree.delete(*self._tags_tree.get_children())
            self._tags_update_pending_label()
            return

        self._tags_weapons = weapons
        self._tags_proj_choices = get_projectile_choices(path)
        self._tags_swap_combo.configure(
            values=[f"[{d:08X}] {n}" for d, n in self._tags_proj_choices])

        n_fields = sum(len(w.projectile_fields) for w in weapons)
        self._tags_file_lbl.config(
            text=f"{short}  ({len(weapons)} weap tags, {n_fields} barrel(s) with a projectile field)")
        self._tags_refresh_tree()
        self._tags_update_pending_label()

    # ── Tree ───────────────────────────────────────────────────────────────

    def _tags_refresh_tree(self):
        tree = self._tags_tree
        tree.delete(*tree.get_children())
        for w in self._tags_weapons:
            parent_iid = f"w{w.tag_entry_index}"
            n = len(w.projectile_fields)
            parent_tags = () if w.name_resolved else ("unresolved",)
            tree.insert("", tk.END, iid=parent_iid, text=w.name,
                        values=("", "" if n else "(no Barrels found)", "", ""),
                        open=False, tags=parent_tags)
            for field in w.projectile_fields:
                key = (w.tag_entry_index, field.offset)
                pending_datum = self._tags_pending.get(key)
                file_off = w.tag_file_off + field.offset
                if pending_datum is not None:
                    pending_name = next(
                        (nm for d, nm in self._tags_proj_choices if d == pending_datum),
                        f"0x{pending_datum:08X}")
                    current_str = f"{field.proj_name}  →  {pending_name}"
                    row_tags, status = ("pending",), "QUEUED"
                elif field.status == "resolved":
                    current_str, row_tags, status = field.proj_name, (), ""
                elif field.status == "no_projectile":
                    current_str, row_tags, status = field.proj_name, ("noproj",), ""
                else:
                    current_str, row_tags, status = field.proj_name, ("unresolved",), "?"
                child_iid = f"w{w.tag_entry_index}:{field.offset}"
                tree.insert(parent_iid, tk.END, iid=child_iid, text="",
                            values=(f"Barrel {field.barrel_index}", current_str,
                                    status, f"0x{file_off:X}"),
                            tags=row_tags)

    def _tags_on_select(self, _event=None):
        sel = self._tags_tree.selection()
        if not sel or ":" not in sel[0]:
            self._tags_selected = None
            self._tags_swap_btn.config(state=tk.DISABLED)
            self._tags_sel_lbl.config(text="(select a projectile field below a weapon)")
            return

        w_part, off_part = sel[0].split(":", 1)
        try:
            entry_idx, offset = int(w_part[1:]), int(off_part)
        except ValueError:
            return

        weapon = next((w for w in self._tags_weapons if w.tag_entry_index == entry_idx), None)
        field = next((f for f in (weapon.projectile_fields if weapon else [])
                      if f.offset == offset), None)
        if not weapon or not field:
            self._tags_selected = None
            self._tags_swap_btn.config(state=tk.DISABLED)
            self._tags_sel_lbl.config(text="(field no longer available)")
            return

        self._tags_selected = (weapon, field)
        file_off = weapon.tag_file_off + field.offset
        self._tags_sel_lbl.config(
            text=f"{weapon.name} — Barrel {field.barrel_index}\n"
                 f"file offset 0x{file_off:X}  (currently: {field.proj_name})")
        self._tags_swap_btn.config(state=tk.NORMAL)

    # ── Swap queue ────────────────────────────────────────────────────────

    def _tags_queue_swap(self):
        if not self._tags_selected:
            return
        weapon, field = self._tags_selected
        sel = self._tags_swap_combo.current()
        if sel < 0 or sel >= len(self._tags_proj_choices):
            messagebox.showwarning("Swap projectile", "Pick a projectile first.")
            return

        new_datum, new_name = self._tags_proj_choices[sel]
        if new_datum == field.proj_datum:
            messagebox.showinfo("Swap projectile",
                                 f"{weapon.name} Barrel {field.barrel_index} already uses {new_name}.")
            return

        self._tags_pending[(weapon.tag_entry_index, field.offset)] = new_datum
        self._tags_refresh_tree()
        self._tags_update_pending_label()

    def _tags_discard_pending(self):
        if not self._tags_pending:
            return
        self._tags_pending.clear()
        self._tags_refresh_tree()
        self._tags_update_pending_label()

    def _tags_update_pending_label(self):
        n = len(self._tags_pending)
        if n == 0:
            self._tags_pending_lbl.config(text="none")
            self._tags_save_btn.config(state=tk.DISABLED)
            return

        lines = []
        for (entry_idx, offset), new_datum in self._tags_pending.items():
            w = next((w for w in self._tags_weapons if w.tag_entry_index == entry_idx), None)
            new_name = next((nm for d, nm in self._tags_proj_choices if d == new_datum),
                             f"0x{new_datum:08X}")
            wname = w.name if w else f"weap#{entry_idx}"
            lines.append(f"{wname} → {new_name}")
        self._tags_pending_lbl.config(text="\n".join(lines))
        self._tags_save_btn.config(state=tk.NORMAL)

    # ── Save ──────────────────────────────────────────────────────────────

    def _tags_save_modified(self):
        if not self._tags_pending or not self._tags_map_path:
            return

        src = self._tags_map_path
        base, ext = os.path.splitext(src)
        default_name = os.path.basename(base) + "_modified" + (ext or ".map")
        out_path = filedialog.asksaveasfilename(
            title="Save modified .map as…",
            initialfile=default_name,
            defaultextension=ext or ".map",
            filetypes=[("Map files", "*.map"), ("All files", "*.*")])
        if not out_path:
            return
        if os.path.abspath(out_path) == os.path.abspath(src):
            messagebox.showerror("Save modified copy",
                                  "Pick a different filename — this tool never "
                                  "overwrites the loaded .map.")
            return

        try:
            n = write_patched_map_with_swaps(
                src, out_path, self._tags_weapons, self._tags_pending)
            self._tags_stat_lbl.config(text=f"Saved {os.path.basename(out_path)}",
                                        foreground="#3dcc96")
            messagebox.showinfo(
                "Save modified copy",
                f"Wrote {n} change(s) to:\n{out_path}\n\n"
                "The original .map file was left untouched. Point Xenia at the "
                "new file (or back up and replace the original yourself) to "
                "actually see the change in-game.")
        except Exception as e:
            self._tags_stat_lbl.config(text="Save failed", foreground="#f07878")
            messagebox.showerror("Save modified copy", f"Write failed: {e}")
