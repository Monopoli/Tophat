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

## Open items / likely next steps

- Decide whether to actually build the missing `overlay.py` feature (transparent always-on-top window) or strip it from the README.
- Reconcile/clean up `files.zip` and `tophat_grid_patch.zip` against the canonical root-level files.
- Resolve the uncommitted `.gitignore`/`gitignore`/`.gitignore.gitignore` situation before the next commit.
- Correct the README's `pywin32` requirement (either remove it or actually start using it).
