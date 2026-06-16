"""Halo 2 Xbox Object Monitor — memory reader."""
import sys
import ctypes
import ctypes.wintypes as wintypes
from constants import (
    PROCESS_VM_READ, PROCESS_VM_WRITE, PROCESS_VM_OPERATION,
    PROCESS_QUERY_INFORMATION, TH32CS_SNAPPROCESS, PROCESSENTRY32,
)

kernel32 = ctypes.windll.kernel32 if sys.platform == "win32" else None


class MemoryReader:
    """Wraps ReadProcessMemory / WriteProcessMemory for a given process handle."""

    def __init__(self, pid):
        self.pid = pid
        self.handle = None
        self._open()

    def _open(self):
        if kernel32 is None:
            raise RuntimeError("Windows only")
        h = kernel32.OpenProcess(
            PROCESS_VM_READ | PROCESS_VM_WRITE | PROCESS_VM_OPERATION
            | PROCESS_QUERY_INFORMATION, False, self.pid
        )
        if not h:
            err = kernel32.GetLastError()
            raise RuntimeError(
                f"OpenProcess failed (pid={self.pid}, err={err}). "
                "Run as Administrator.")
        self.handle = h

    def read(self, address: int, size: int) -> bytes | None:
        buf  = (ctypes.c_char * size)()
        read = ctypes.c_size_t(0)
        ok = kernel32.ReadProcessMemory(
            self.handle, ctypes.c_void_p(address), buf, size, ctypes.byref(read))
        if not ok or read.value != size:
            return None
        return bytes(buf)

    def read_u8(self, addr):
        b = self.read(addr, 1); return b[0] if b else None

    def read_i16(self, addr):
        import struct
        b = self.read(addr, 2); return struct.unpack_from("<h", b)[0] if b else None

    def read_u16(self, addr):
        import struct
        b = self.read(addr, 2); return struct.unpack_from("<H", b)[0] if b else None

    def read_u32(self, addr):
        import struct
        b = self.read(addr, 4); return struct.unpack_from("<I", b)[0] if b else None

    def read_f32(self, addr):
        import struct
        b = self.read(addr, 4)
        if not b: return None
        v = struct.unpack_from("<f", b)[0]
        return None if (v != v) else v

    def read_string(self, addr: int, max_len: int = 256) -> str | None:
        """Read a null-terminated ASCII string from memory."""
        b = self.read(addr, max_len)
        if not b: return None
        end = b.find(b'\x00')
        raw = b[:end] if end >= 0 else b
        return raw.decode("ascii", errors="replace")

    def write_bytes(self, address: int, data: bytes) -> bool:
        """Write bytes to process memory. Returns True on success."""
        buf     = (ctypes.c_char * len(data))(*data)
        written = ctypes.c_size_t(0)
        ok = kernel32.WriteProcessMemory(
            self.handle, ctypes.c_void_p(address),
            buf, len(data), ctypes.byref(written))
        return bool(ok) and written.value == len(data)

    def close(self):
        if self.handle:
            kernel32.CloseHandle(self.handle)
            self.handle = None


def list_processes() -> list[tuple[int, str]]:
    """Return list of (pid, name) for all running processes."""
    if kernel32 is None:
        return []
    snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
    if snapshot == wintypes.HANDLE(-1).value:
        return []
    entry = PROCESSENTRY32()
    entry.dwSize = ctypes.sizeof(PROCESSENTRY32)
    procs = []
    if kernel32.Process32First(snapshot, ctypes.byref(entry)):
        while True:
            procs.append((entry.th32ProcessID,
                          entry.szExeFile.decode("utf-8", errors="replace")))
            if not kernel32.Process32Next(snapshot, ctypes.byref(entry)):
                break
    kernel32.CloseHandle(snapshot)
    return procs


def find_halo2_pid() -> tuple[int | None, str | None]:
    """Try to auto-detect a Halo 2 / Xenia process."""
    keywords = ["halo2", "xenia", "xqemu", "h2"]
    for pid, name in list_processes():
        if any(k in name.lower() for k in keywords):
            return pid, name
    return None, None
