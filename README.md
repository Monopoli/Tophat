# Halo 2 Xbox Live Object Monitor

Real-time GUI that reads the Halo 2 object state directly from process memory,
mapping raw bytes to the C++ structs in Objects.hpp / ObjectDefinitions.hpp.

## Requirements

- Windows (ReadProcessMemory API)
- Python 3.10+  (standard library only — tkinter + ctypes, no pip install needed)
- **Run as Administrator** — cross-process memory access requires elevated privileges
- Halo 2 running in **Xenia** (recommended), XQEMU, or on a debug Xbox

## Usage

1. Start Halo 2 in your emulator / on hardware
2. Double-click `launch_monitor.bat` (handles UAC elevation automatically)
   — OR — right-click `h2_object_monitor.py` → "Run as administrator"
3. The app auto-detects Xenia/XQEMU by process name; click **⟳ Refresh**
   if it doesn't appear, select it manually, then click **Connect**
4. Object table populates and refreshes every 500 ms (adjustable)

## Memory layout used

Based on CheatEngine .CEM captures and the Yelo Open Sauce SDK headers:

| Region                    | Address        | Structure               |
|---------------------------|----------------|-------------------------|
| Object header DataArray   | `0x3003CEF0`   | `t_object_data`         |
| Datum entries start       | `+0x34`        | `s_object_header_datum` |
| Each datum                | 12 bytes each  | salt/flags/type/cluster/addr |
| Object data (per pointer) | via `addr` ptr | `s_object_data` (0xFC bytes) |

Key offsets in `s_object_data` (Xbox non-alpha):
- `+0x64`  Origin (real_point3d)
- `+0x70`  Forward (real_vector3d)
- `+0xA0`  Scale
- `+0xEC`  Health (0.0–1.0)
- `+0xF0`  Shields (0.0–1.0)
- `+0xE4`  MaximumVitality
- `+0xE8`  CurrentVitality

## Features

- **Live object table** — all 2048 slots scanned each refresh, non-null shown
- **Type filter** — biped, weapon, scenery, vehicle, etc.
- **Active-only toggle** — hide inactive/child objects
- **Search** — filter by index, address, type string, cluster
- **Detail panel** — full struct dump for selected object with health/shield bars
- **Column sort** — click any column header
- **Adjustable poll rate** — 100–5000 ms
- **Color-coded by type** — each object type has a distinct colour
- **Health colours** — green > 50%, amber 20–50%, red < 20%

## Notes on emulator compatibility

The base addresses (`0x3003CEF0` for the header array) are hardcoded from the
CEM captures. If your emulator maps Halo 2's memory to a different host address
space, you may need to adjust the `ARRAY_BASE` constant near the top of the script.
Xenia typically presents guest addresses directly, but add a base offset if needed:

```python
# In h2_object_monitor.py, change:
ARRAY_BASE = 0x3003CEF0
# to e.g.:
ARRAY_BASE = XENIA_BASE_OFFSET + 0x3003CEF0
```
