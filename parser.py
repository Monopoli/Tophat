"""Halo 2 Xbox Object Monitor — object data parser."""
import struct
from constants import (
    ARRAY_BASE, ARRAY_HDR_SIZE, DATUM_SIZE, MAX_OBJECTS,
    OBJECT_DATA_SIZE, OBJECT_TYPES, MAP_STRING_ADDR, MAP_STRING_MAXLEN,
    OBJ_ORIGIN_OFF, OBJ_FORWARD_OFF, OBJ_UP_OFF, OBJ_TRANS_VEL_OFF,
    OBJ_ANG_VEL_OFF, OBJ_HEALTH_OFF, OBJ_SHIELDS_OFF,
)
from memory import MemoryReader
from tag_database import tag_name_from_datum


def parse_object_data(mem: MemoryReader, obj_addr: int) -> dict:
    """Read s_object_data fields from the object's memory address."""
    if obj_addr < 0x10000:
        return {}
    raw = mem.read(obj_addr, OBJECT_DATA_SIZE)
    if not raw:
        return {}

    def rf(off):
        if off + 4 > len(raw): return None
        v = struct.unpack_from("<f", raw, off)[0]
        return None if (v != v) or abs(v) > 1e10 else v

    def ri32(off):
        if off + 4 > len(raw): return None
        return struct.unpack_from("<I", raw, off)[0]

    def ri16(off):
        if off + 2 > len(raw): return None
        return struct.unpack_from("<h", raw, off)[0]

    def_idx  = ri32(0x00)
    def_tag  = tag_name_from_datum(def_idx) if def_idx else ""

    return {
        "definition":     def_idx,
        "definition_tag": def_tag,
        "next_index":     ri32(0x0C),
        "parent_index":   ri32(0x14),
        "placement_idx":  ri16(0x1A),
        "origin":        (rf(OBJ_ORIGIN_OFF),    rf(OBJ_ORIGIN_OFF+4),    rf(OBJ_ORIGIN_OFF+8)),
        "forward":       (rf(OBJ_FORWARD_OFF),   rf(OBJ_FORWARD_OFF+4),   rf(OBJ_FORWARD_OFF+8)),
        "up":            (rf(OBJ_UP_OFF),        rf(OBJ_UP_OFF+4),        rf(OBJ_UP_OFF+8)),
        "trans_vel":     (rf(OBJ_TRANS_VEL_OFF), rf(OBJ_TRANS_VEL_OFF+4), rf(OBJ_TRANS_VEL_OFF+8)),
        "ang_vel":       (rf(OBJ_ANG_VEL_OFF),   rf(OBJ_ANG_VEL_OFF+4),   rf(OBJ_ANG_VEL_OFF+8)),
        "scale":          rf(0xA0),
        "type_byte":     raw[0xAA] if 0xAA < len(raw) else None,
        "name_idx":      ri16(0xAC),
        "max_vit":        rf(0xE4),
        "cur_vit":        rf(0xE8),
        "health":         rf(OBJ_HEALTH_OFF),
        "shields":        rf(OBJ_SHIELDS_OFF),
        "collision_flags": raw[0x10A] if 0x10A < len(raw) else None,
        "health_flags":    raw[0x10B] if 0x10B < len(raw) else None,
    }


def read_all_objects(mem: MemoryReader) -> tuple[list[dict], int, str]:
    """Read the full object header array and cross-reference object data.

    Returns (objects, active_count, map_scenario_string).
    """
    map_str          = mem.read_string(MAP_STRING_ADDR, MAP_STRING_MAXLEN) or ""
    active_count_raw = mem.read_u16(ARRAY_BASE + 0x26) or 0

    objects    = []
    total_bytes = DATUM_SIZE * MAX_OBJECTS
    bulk        = mem.read(ARRAY_BASE + ARRAY_HDR_SIZE, total_bytes)
    if not bulk:
        return objects, 0, map_str

    for i in range(MAX_OBJECTS):
        off = i * DATUM_SIZE
        raw = bulk[off:off + DATUM_SIZE]
        if len(raw) < DATUM_SIZE:
            break
        salt = struct.unpack_from("<H", raw, 0)[0]
        if salt == 0:
            continue

        flags    = raw[2]
        typ      = raw[3]
        cluster  = struct.unpack_from("<h", raw, 4)[0]
        size     = struct.unpack_from("<H", raw, 6)[0]
        obj_addr = struct.unpack_from("<I", raw, 8)[0]

        hdr = {
            "index":   i,
            "salt":    salt,
            "flags":   flags,
            "type_id": typ,
            "type":    OBJECT_TYPES.get(typ, f"unk({typ})"),
            "cluster": cluster,
            "size":    size,
            "addr":    obj_addr,
            "active":  bool(flags & 0x01),
        }
        od = parse_object_data(mem, obj_addr)
        objects.append({**hdr, **od})

    return objects, active_count_raw, map_str
