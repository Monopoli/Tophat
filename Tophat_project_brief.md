# Tophat — Project Brief

Paste or upload this file at the start of a new chat (along with the project archive, since sandbox files don't persist between conversations) to get a new Claude session up to speed quickly.

## What it is

Tophat is a multi-tab Python/tkinter desktop application that attaches to **Halo 2 (Xbox version) running under the Xenia emulator** via the Windows `ReadProcessMemory`/`WriteProcessMemory` API, and monitors/visualizes live game state in real time — object table, AI state, player state, 2D map, BSP collision geometry, and a HaloScript encounter-script database cross-referenced against the live object table.

This is a reverse-engineering / live-debugging tool for the Halo 2 Xbox engine, built by manually mapping memory addresses and binary tag/BSP structures (see "Reverse-engineered structures" below). Not a cheat tool in the malicious sense — it's read/inspect tooling plus one write feature (AUP, below).

## Runtime constraint (important)

The core mechanism (`ReadProcessMemory` via `ctypes.windll.kernel32`) is **Windows-only**. The app detects this at startup and exits gracefully with `"This tool requires Windows (ReadProcessMemory API)."` on any other platform — confirmed working as intended when run under Linux/Xvfb. A Linux sandbox can be used to edit code and catch syntax errors, but **cannot actually exercise the live-attach functionality**. Real testing requires Windows + Xenia + a Halo 2 Xbox ISO running a campaign map.

## Architecture

`app.py` defines `class App(ObjectTableMixin, DetailMixin, AupMixin, MapMixin, PlayerMixin, ScriptsMixin, BspMixin, tk.Tk)` — one big multi-inheritance tkinter window built from per-tab mixins. `main.py` is just `from app import main; main()`.

| File | Purpose |
|---|---|
| `main.py` | Entry point |
| `app.py` | `App` class, poll loop, connection management |
| `constants.py` | Memory addresses, type maps, colours |
| `memory.py` | `MemoryReader` (raw `ctypes.windll.kernel32`, **not** pywin32), process enumeration |
| `parser.py` | Object table parser |
| `tag_database.py` | Per-map tag name resolution (auto-generated, ~340KB, do not hand-edit) |
| `ui_objects.py` | Objects tab |
| `ui_detail.py` | Detail panel |
| `ui_aup.py` | AUP tab (Artificially Unintelligent Player — writes a datum index+salt into the active unit pointer to puppet any biped/vehicle) |
| `ui_map.py` | Map tab (2D top-down, optional Pillow-rendered BSP background) |
| `ui_player.py` | Player tab (PCG globals, stick visualizer, button grid) |
| `ui_scripts.py` | Scripts tab + HaloScript entity database (~957KB, by far the largest module) |
| `ui_bsp.py` | BSP collision-geometry tab (Top/Front/Side/Iso projections, pan/zoom/rotate, live object overlay) |
| `cluster_portals.py` | Render-cluster portal parser/renderer, companion mixin for `ui_bsp.py` |
| `trigger_volumes.py` | Trigger volume parser/renderer, companion mixin for `ui_bsp.py` |
| `CairoImages/` | ~200 reference PNG thumbnails (object/tag icons), ~116MB |

**Note on `overlay.py`:** the README previously described a standalone "Overlay" feature (transparent always-on-top window, click-through, F9 toggle, per-corner anchoring) as if it shipped. This file **does not exist** in the repo and there is no F9 keybinding anywhere in the code. The only thing called "overlay" in the actual codebase is canvas-drawn status text inside the BSP tab (`ui_bsp.py`'s `_bsp_draw_overlay`), which is unrelated. This looks like a documented-but-never-implemented feature — confirmed by checking the single git commit, whose message claims to add "...overlay..." but whose file list contains no `overlay.py`. **Resolved this session:** the README now marks it explicitly `(planned — not yet implemented)` in both the Features list and the file table, instead of describing it as already working. The feature itself still hasn't been built — that's a separate, still-open decision.

## Confirmed memory layout (Halo 2 Xbox / Xenia)

- Object array base: `0x3003CEF0`
- Player array base: `0x30002AD0`
- PCG base: `0x30004B5C`
- AUP address: `0x30004C14`
- Map string: `0x30000008`

## Supported maps (15 campaign missions, verified against `tag_database.py`)

`00a_introduction`, `01a_tutorial`, `01b_spacestation`, `03a_oldmombasa`, `03b_newmombasa`, `04a_gasgiant`, `04b_floodlab`, `05a_deltaapproach`, `05b_deltatowers`, `06a_sentinelwalls`, `06b_floodzone`, `07a_highcharity`, `07b_forerunnership`, `08a_deltacliffs`, `08b_deltacontrol`

## Reverse-engineered binary structures (worth preserving — non-obvious, hard-won)

- **Trigger volumes** (`trigger_volumes.py`) — confirmed against the user-provided `scnrstructure.txt` (Halo 2 `scnr` tag plugin layout). The block is officially **Kill Trigger Volumes**, a reflexive (count, ptr) at `scnr meta+0x108`, stride `0x44` (68) bytes/entry: `+0x00` name_id (stringid, raw/unresolved — no string-table decoder exists in this codebase yet), `+0x04` object_name_index (int16), `+0x06` node_index (int16), `+0x08` node_name_id (stringid), `+0x0C` forward (vector3), `+0x18` up (vector3), `+0x24` position (point3), `+0x30` extents (point3), `+0x40` kill_trigger_volume_index (int16, distinct from array position). The parser now reads the reflexive directly — translating the pointer via `ptr - voff`, the same convention validated below for cluster portals — instead of brute-force byte-scanning. History: the original scan found the right 68-byte stride but locked onto the vector data 12 bytes into each record, skipping the name/node header (those bytes don't look like floats). Rendered geometry was never wrong because the 12-byte shift was constant, but the name field was invisible and the "20 unused trailing bytes" were actually a mix of one record's tail and the next record's header. The old scan is kept as a fallback (shifted back 12 bytes onto the true record start) in case the reflexive ever fails to validate on a different build.

- **Cluster portals** (`cluster_portals.py`) — confirmed against the user-provided `Sbsp.txt` (Halo 2 `sbsp` tag plugin layout). **The previous model here was wrong, not just imprecise.** Portals are their own standalone reflexive at `sbsp meta+0x5C`, stride `0x24` (36) bytes/entry: `+0x00` back_cluster (int16, `-1` = none/outside), `+0x02` front_cluster (int16), `+0x04` plane_index (int32, unresolved), `+0x08` centroid (point3), `+0x14` radius (float32), `+0x18` flags (flags32 — AI-cannot-hear / one-way / door / no-way / one-way-reversed / no-one-can-hear), `+0x1C` a nested vertices reflexive (count, ptr) → point3 array, stride `0xC`, XYZ only, no extra trailing float. The structure previously assumed here — scan the separate "Clusters" render-mesh reflexive at `meta+0x9C`, treat a `first_portal_vertex`/`portal_vertex_count` u16 pair at cluster-entry `+36`/`+38` as indexing into a shared vertex pool at `meta+0xF4` — is now confirmed wrong: `Clusters` is real and fixed-stride (`0xB0` bytes) at that offset, but its actual fields at `+0x24`/`+0x26` are `Total Subpart Count`/`Section Lighting Flags`, unrelated to portals. The ~31 polygons the old heuristic recovered for `01b_spacestation` were coincidental aliasing with mesh-resource fields, not real portal data. The parser now reads the confirmed structure directly; the old coplanarity/extent heuristic has been removed entirely rather than kept as a fallback, since its underlying model was wrong rather than merely imprecise. Each render `Cluster` entry separately carries its own portal-index list (`Clusters`-entry `+0x8C`, int16 array) for per-cluster portal membership — not read yet, but available if a future feature needs it.

- Reference plugin dumps `scnrstructure.txt` and `Sbsp.txt` (Reclaimer/Assembly-style Halo 2 tag layouts, user-provided) are the ground truth behind both fixes above. Worth checking into the repo (e.g. a `reference/` folder) alongside the modules they informed — not yet done.

- Both rewritten parsers were verified with synthetic round-trip tests (hand-built binary blobs exercising the reflexive/offset math) since no live Windows + Xenia session was available in the sandbox that produced them. Live validation against an actual running map is still outstanding.

## Dependencies & environment

- Python 3.11+ (tested here against 3.12.3)
- `tkinter` — required, not installed by default on a bare Ubuntu box (`apt install python3-tk`)
- `Pillow` — optional, only for image-file map backgrounds / object icon thumbnails; code degrades gracefully (`try/except ImportError`, `HAS_PIL`/`_PIL_OK` flags) if absent
- **`pywin32` was listed in the README as a requirement but is not actually imported anywhere in the code.** The Windows API calls go through raw `ctypes.windll.kernel32`. **Resolved this session** — README now lists only `Pillow` and notes the `ctypes`-based approach explicitly.
- To run for real: Windows + Xenia + Halo 2 Xbox campaign map loaded, run `python main.py` (likely needs admin rights for `OpenProcess`, per the in-code error message).

## Git / repo state (as of the uploaded `.rar`)

- Single squashed commit on `main`: `cdedb1c "Add scripts tab features, enemy groups, overlay, flow diagram, change log, source map, timer watch"`
- Remote: `origin → https://github.com/Monopoli/Tophat.git`
- At export time, the working tree had **uncommitted changes**: staged deletions of `.gitignore` and `gitignore`; untracked `.gitignore.gitignore` (likely an accidental duplicate from the rar export), `cluster_portals.py`, `trigger_volumes.py`, `files.zip`, `tophat_grid_patch.zip`; and `ui_bsp.py` modified vs the index.
- `files.zip` and `tophat_grid_patch.zip` are loose backup/patch bundles sitting in the repo root containing slightly different copies of files that already exist at top level (`ui_bsp.py`/`cluster_portals.py`/`trigger_volumes.py` in `files.zip`; `ui_objects.py`/`app.py` in `tophat_grid_patch.zip`). Worth cleaning up or reconciling — unclear which version is canonical.
- **Status as of this session:** the above reflects the repo state *as previously documented*, not a fresh `git status` — time has passed since that snapshot was taken, and this session had no access to the actual local clone (only the read-only project-knowledge file copies, plus the user-uploaded `Sbsp.txt`). This session produced the exact commands to resolve the `.gitignore` triple, inspect/reconcile the two zip bundles, drop in the corrected parsers, commit, and push, but did not — and couldn't — run them. Confirm current state with `git status` before following them.

## Setup already verified in a prior session

In a Linux sandbox: extracted the rar (needed `unrar`, not preinstalled), installed `python3-tk`, built a venv with `Pillow`, confirmed all 15 `.py` files byte-compile with no syntax errors, and ran `main.py` under Xvfb — it correctly detected the non-Windows platform and exited with the expected message rather than crashing. No functional/live testing was possible since that requires Windows + a real Xenia/Halo 2 process.

## Open items / likely next steps

**Resolved this session:**
- Trigger volume and cluster portal structures confirmed against `scnrstructure.txt`/`Sbsp.txt`; both parsers rewritten accordingly (see "Reverse-engineered binary structures" above).
- README's `pywin32` requirement removed; Overlay feature now marked `(planned — not yet implemented)` instead of described as already working.

**Still open:**
- Decide whether to actually build the planned `overlay.py` feature, or drop the Features-list mention entirely — only the documentation framing was resolved this session, not the underlying scope decision.
- Reconcile/clean up `files.zip` and `tophat_grid_patch.zip` against the canonical root-level files — exact inspection/cleanup commands were given this session but not run (no access to the real clone from this sandbox).
- Resolve the uncommitted `.gitignore`/`gitignore`/`.gitignore.gitignore` situation before the next commit — commands given this session, not yet run.
- Validate `trigger_volumes.py` and `cluster_portals.py` against a live Windows + Xenia session — only synthetic round-trip tests were possible without that environment.
- Decide whether to check `scnrstructure.txt`/`Sbsp.txt` into the repo as reference docs (e.g. under a `reference/` folder).
