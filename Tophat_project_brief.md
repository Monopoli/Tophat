# Tophat — Project Brief

Paste or upload this file at the start of a new chat (along with the project archive, since sandbox files don't persist between conversations) to get a new Claude session up to speed quickly.

## What it is

Tophat is a multi-tab Python/tkinter desktop application that attaches to **Halo 2 (Xbox version) running under the Xenia emulator** via the Windows `ReadProcessMemory`/`WriteProcessMemory` API, and monitors/visualizes live game state in real time — object table, AI state, player state, 2D map, BSP collision geometry, and a HaloScript encounter-script database cross-referenced against the live object table.

This is a reverse-engineering / live-debugging tool for the Halo 2 Xbox engine, built by manually mapping memory addresses and binary tag/BSP structures (see "Reverse-engineered structures" below). Not a cheat tool in the malicious sense — it's read/inspect tooling plus two write features (AUP and Cheats, below).

## Runtime constraint (important)

The core mechanism (`ReadProcessMemory` via `ctypes.windll.kernel32`) is **Windows-only**. The app detects this at startup and exits gracefully with `"This tool requires Windows (ReadProcessMemory API)."` on any other platform — confirmed working as intended when run under Linux/Xvfb. A Linux sandbox can be used to edit code and catch syntax errors, but **cannot actually exercise the live-attach functionality**. Real testing requires Windows + Xenia + a Halo 2 Xbox ISO running a campaign map.

## Architecture

`app.py` defines `class App(ObjectTableMixin, DetailMixin, AupMixin, MapMixin, PlayerMixin, ScriptsMixin, BspMixin, CheatsMixin, tk.Tk)` — one big multi-inheritance tkinter window built from per-tab mixins. `main.py` is just `from app import main; main()`.

| File | Purpose |
|---|---|
| `main.py` | Entry point |
| `app.py` | `App` class, poll loop, connection management |
| `constants.py` | Memory addresses, type maps, colours, shared `s_object_data` field offsets (`OBJ_*_OFF`) |
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
| `ui_cheats.py` | Cheats tab (teleport — manual X/Y/Z or to another object's position — speed manipulation — forward-direction boost or raw velocity vector — and vitality — manual HP/shield entry, Full Health/Shields, Kill — for any tracked biped/vehicle; writes via `OBJ_ORIGIN_OFF`/`OBJ_TRANS_VEL_OFF`/`OBJ_HEALTH_OFF`/`OBJ_SHIELDS_OFF` from `constants.py`) |
| `cluster_portals.py` | Render-cluster portal parser/renderer, companion mixin for `ui_bsp.py` |
| `trigger_volumes.py` | Trigger volume parser/renderer, companion mixin for `ui_bsp.py` |
| `CairoImages/` | ~200 reference PNG thumbnails (object/tag icons), ~116MB |

**Note on `overlay.py`:** the README describes a standalone "Overlay" feature (transparent always-on-top window, click-through, F9 toggle, per-corner anchoring). This file **does not exist** in the repo and there is no F9 keybinding anywhere in the code. The only thing called "overlay" in the actual codebase is canvas-drawn status text inside the BSP tab (`ui_bsp.py`'s `_bsp_draw_overlay`), which is unrelated. This looks like a documented-but-never-implemented feature — confirmed by checking the single git commit, whose message claims to add "...overlay..." but whose file list contains no `overlay.py`.

## Confirmed memory layout (Halo 2 Xbox / Xenia)

- Object array base: `0x3003CEF0`
- Player array base: `0x30002AD0`
- PCG base: `0x30004B5C`
- AUP address: `0x30004C14`
- Map string: `0x30000008`

## Supported maps (15 campaign missions, verified against `tag_database.py`)

`00a_introduction`, `01a_tutorial`, `01b_spacestation`, `03a_oldmombasa`, `03b_newmombasa`, `04a_gasgiant`, `04b_floodlab`, `05a_deltaapproach`, `05b_deltatowers`, `06a_sentinelwalls`, `06b_floodzone`, `07a_highcharity`, `07b_forerunnership`, `08a_deltacliffs`, `08b_deltacontrol`

## Reverse-engineered binary structures (worth preserving — non-obvious, hard-won)

- **Cluster portals** (`cluster_portals.py`): each sbsp meta has a CLUSTERS reflexive at `meta+0x09c`. Cluster entries aren't uniform stride end-to-end, but the first 80 bytes of each are a stable header; `+36` = `first_portal_vertex` (u16), `+38` = `portal_vertex_count` (u16). Portal vertex pool is a second reflexive at `meta+0x0f4`, stride 16. Discovered against `01b_spacestation`.
- **Trigger volumes** (`trigger_volumes.py`): scnr tag entries are 16 bytes (`+0` class tag, `+8` voff = file offset from `tag_file_off`, `+12` size). Trigger volume array stride is 68 bytes/entry (no name field in this build), located by scanning for the longest run of valid entries. Discovered against `01b_spacestation` at tag-section file offset `0xb525000`.

## Dependencies & environment

- Python 3.11+ (tested here against 3.12.3)
- `tkinter` — required, not installed by default on a bare Ubuntu box (`apt install python3-tk`)
- `Pillow` — optional, only for image-file map backgrounds / object icon thumbnails; code degrades gracefully (`try/except ImportError`, `HAS_PIL`/`_PIL_OK` flags) if absent
- **`pywin32` is listed in the README as a requirement but is not actually imported anywhere in the code.** The Windows API calls go through raw `ctypes.windll.kernel32`. README is wrong/aspirational on this point.
- To run for real: Windows + Xenia + Halo 2 Xbox campaign map loaded, run `python main.py` (likely needs admin rights for `OpenProcess`, per the in-code error message).

## Git / repo state (as of the uploaded `.rar`)

- Single squashed commit on `main`: `cdedb1c "Add scripts tab features, enemy groups, overlay, flow diagram, change log, source map, timer watch"`
- Remote: `origin → https://github.com/Monopoli/Tophat.git`
- At export time, the working tree had **uncommitted changes**: staged deletions of `.gitignore` and `gitignore`; untracked `.gitignore.gitignore` (likely an accidental duplicate from the rar export), `cluster_portals.py`, `trigger_volumes.py`, `files.zip`, `tophat_grid_patch.zip`; and `ui_bsp.py` modified vs the index.
- `files.zip` and `tophat_grid_patch.zip` are loose backup/patch bundles sitting in the repo root containing slightly different copies of files that already exist at top level (`ui_bsp.py`/`cluster_portals.py`/`trigger_volumes.py` in `files.zip`; `ui_objects.py`/`app.py` in `tophat_grid_patch.zip`). Worth cleaning up or reconciling — unclear which version is canonical.

## Setup already verified in a prior session

In a Linux sandbox: extracted the rar (needed `unrar`, not preinstalled), installed `python3-tk`, built a venv with `Pillow`, confirmed all 15 `.py` files byte-compile with no syntax errors, and ran `main.py` under Xvfb — it correctly detected the non-Windows platform and exited with the expected message rather than crashing. No functional/live testing was possible since that requires Windows + a real Xenia/Halo 2 process.

## Cheats tab (added this session)

New `ui_cheats.py` / `CheatsMixin`, wired into `app.py` as the last tab. Picker list is units only (biped/vehicle); the "teleport to target" combo can target *any* live object (by index, so the label stays stable across ticks even though the target moves). Features:
- Manual teleport (X/Y/Z entry, with a "Capture current" button to pre-fill from the selected unit's live origin)
- Teleport to another object's current position
- Speed boost along the unit's current facing direction (single speed value)
- Manual velocity vector entry, plus a one-click "Stop (zero)"
- Vitality: manual HP/shield entry + Apply, plus quick "Full Health/Shields" and "Kill" buttons (writes `OBJ_HEALTH_OFF`/`OBJ_SHIELDS_OFF` as two independent f32 writes — not assumed contiguous even though they happen to be 4 bytes apart). Note: `max_vit`/`cur_vit` (0xE4/0xE8) are also parsed in `parser.py` but their relationship to `health`/`shields` hasn't been confirmed live — worth checking on real hardware in case some object types key off vitality instead.

All writes go through `MemoryReader.write_bytes(obj_addr + OBJ_*_OFF, ...)`. The offsets (`OBJ_ORIGIN_OFF`, `OBJ_TRANS_VEL_OFF`, etc.) were pulled out of `parser.py`'s hardcoded literals into named constants in `constants.py`, and `parser.py` was refactored to use them too — same offsets, just one shared source of truth so the read and write paths can't drift apart.

Verified in this session, Linux sandbox + Xvfb: byte-compiled clean, and a full smoke test built the real `App()`, switched to every tab including Cheats, then drove every Cheats button handler (select, capture, teleport, teleport-to-target, forward boost, manual velocity, stop, and the on-map-change reset) against a fake in-memory object list and a fake `MemoryReader.write_bytes`, confirming the correct target addresses (`obj_addr + 0x64` for origin, `obj_addr + 0x88` for velocity) and payloads. Still no real Windows/Xenia/Halo 2 test — that part of the contract is unchanged.

## Merge into persisted project files (separate, later session)

The Cheats tab above was built in a sandbox session whose files never made it into the uploaded project archive — sandbox files don't persist between conversations, and the archive re-uploaded at the start of each new chat is the only thing that does. The next session only had `app.py`'s class line (`...BspMixin, tk.Tk)`, no `CheatsMixin`) as evidence anything had been attempted, with no `ui_cheats.py` and no `OBJ_*_OFF` constants anywhere in `constants.py`.

The user separately still had `ui_cheats.py` / `README.md` / `Tophat_project_brief.md` from that orphaned session (as a `files.zip` upload) and asked to merge them into the current archive. That merge is now done and re-verified against the *current* `app.py`/`constants.py`/`parser.py`, not just re-applied blindly:
- `constants.py`: added `OBJ_ORIGIN_OFF`/`OBJ_TRANS_VEL_OFF`/`OBJ_HEALTH_OFF`/`OBJ_SHIELDS_OFF`.
- `parser.py`: `origin`/`trans_vel`/`health`/`shields` now read via those constants instead of literals; confirmed byte-for-byte identical output against a fake buffer before/after.
- `app.py`: `CheatsMixin` imported and added to `App`'s bases, Cheats tab added to the notebook (last tab), `_refresh_cheats_list()` added to the poll tick, and a map-change reset block added (mirrors the existing AUP reset) so a stale selection doesn't survive a level change.
- Re-ran the same style of smoke test as the original session (fresh `App()`, fake objects, fake `write_bytes`) against the merged tree — all checks passed, including the picker correctly excluding non-unit types and the target combo correctly including them.

**This is still only proven in the Linux/Xvfb sandbox.** The actual point of failure risk is low (the merge was a small, mechanical, three-file diff with no new offsets invented), but real Windows + Xenia + Halo 2 confirmation is still outstanding, same as every other write path in this project.

## Open items / likely next steps

- Decide whether to actually build the missing `overlay.py` feature (transparent always-on-top window) or strip it from the README.
- Reconcile/clean up `files.zip` and `tophat_grid_patch.zip` against the canonical root-level files.
- Resolve the uncommitted `.gitignore`/`gitignore`/`.gitignore.gitignore` situation before the next commit.
- Correct the README's `pywin32` requirement (either remove it or actually start using it).
