"""
Halo 2 Xbox Object Monitor — constants
All addresses, sizes, type mappings and colour definitions.
"""
import ctypes
import ctypes.wintypes as wintypes

# ── Windows process access flags ───────────────────────────────────────────
PROCESS_VM_READ           = 0x0010
PROCESS_VM_WRITE          = 0x0020
PROCESS_VM_OPERATION      = 0x0008
PROCESS_QUERY_INFORMATION = 0x0400
TH32CS_SNAPPROCESS        = 0x00000002

# ── Xbox memory addresses ──────────────────────────────────────────────────
ARRAY_BASE       = 0x3003CEF0   # t_object_data DataArray struct
ARRAY_HDR_SIZE   = 0x4C         # bytes before first datum entry
DATUM_SIZE       = 12           # sizeof(s_object_header_datum)
MAX_OBJECTS      = 2048
OBJECT_DATA_SIZE = 0x10C        # k_object_size_object + extra fields we read
MAP_STRING_ADDR  = 0x30000008   # null-terminated scenario path
MAP_STRING_MAXLEN = 256
AUP_ADDR         = 0x30004C14   # 2-byte idx + 2-byte salt written by Apply AUP

# ── Thresholds ─────────────────────────────────────────────────────────────
TELEPORT_THRESHOLD = 5.0    # world units per tick to flag as teleport
HISTORY_MAX_TICKS  = 120    # ticks of history to keep per object

# ── Object type enum ───────────────────────────────────────────────────────
OBJECT_TYPES = {
    0:  "biped",
    1:  "vehicle",
    2:  "weapon",
    3:  "equipment",
    4:  "garbage",
    5:  "projectile",
    6:  "scenery",
    7:  "machine",
    8:  "control",
    9:  "light_fixture",
    10: "sound_scenery",
    11: "crate",
    12: "creature",
}

HEADER_FLAG_NAMES = {
    0: "active",
    1: "requires_motion",
    3: "being_deleted",
    5: "connected",
    6: "child",
}

TYPE_COLORS = {
    "biped":        "#7F77DD",
    "vehicle":      "#378ADD",
    "weapon":       "#D85A30",
    "equipment":    "#D4537E",
    "garbage":      "#888780",
    "projectile":   "#BA7517",
    "scenery":      "#639922",
    "machine":      "#1D9E75",
    "control":      "#0F6E56",
    "light_fixture":"#EF9F27",
    "sound_scenery":"#5DCAA5",
    "crate":        "#AFA9EC",
    "creature":     "#F09595",
}

# ── ctypes PROCESSENTRY32 ──────────────────────────────────────────────────
class PROCESSENTRY32(ctypes.Structure):
    _fields_ = [
        ("dwSize",              wintypes.DWORD),
        ("cntUsage",            wintypes.DWORD),
        ("th32ProcessID",       wintypes.DWORD),
        ("th32DefaultHeapID",   ctypes.POINTER(ctypes.c_ulong)),
        ("th32ModuleID",        wintypes.DWORD),
        ("cntThreads",          wintypes.DWORD),
        ("th32ParentProcessID", wintypes.DWORD),
        ("pcPriClassBase",      ctypes.c_long),
        ("dwFlags",             wintypes.DWORD),
        ("szExeFile",           ctypes.c_char * 260),
    ]
