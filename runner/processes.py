"""OS resource controls. These controls do not constitute a sandbox."""
import os
import signal
import sys


def limit_worker():
    if sys.platform != "win32":
        import resource
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
        resource.setrlimit(resource.RLIMIT_CPU, (32, 33))
        resource.setrlimit(resource.RLIMIT_FSIZE, (16 * 1024 * 1024,) * 2)
        if sys.platform == "linux":
            resource.setrlimit(resource.RLIMIT_AS, (512 * 1024 * 1024,) * 2)


class ProcessGuard:
    def __init__(self, process):
        self.process = process
        self.handle = None
        if sys.platform == "win32":
            import ctypes
            from ctypes import wintypes

            class Basic(ctypes.Structure):
                _fields_ = [("PerProcessUserTimeLimit", ctypes.c_int64), ("PerJobUserTimeLimit", ctypes.c_int64),
                            ("LimitFlags", wintypes.DWORD), ("MinimumWorkingSetSize", ctypes.c_size_t),
                            ("MaximumWorkingSetSize", ctypes.c_size_t), ("ActiveProcessLimit", wintypes.DWORD),
                            ("Affinity", ctypes.c_size_t), ("PriorityClass", wintypes.DWORD),
                            ("SchedulingClass", wintypes.DWORD)]

            class IO(ctypes.Structure):
                _fields_ = [(name, ctypes.c_uint64) for name in
                            ("ReadOperationCount", "WriteOperationCount", "OtherOperationCount",
                             "ReadTransferCount", "WriteTransferCount", "OtherTransferCount")]

            class Extended(ctypes.Structure):
                _fields_ = [("BasicLimitInformation", Basic), ("IoInfo", IO),
                            ("ProcessMemoryLimit", ctypes.c_size_t), ("JobMemoryLimit", ctypes.c_size_t),
                            ("PeakProcessMemoryUsed", ctypes.c_size_t), ("PeakJobMemoryUsed", ctypes.c_size_t)]

            kernel = ctypes.WinDLL("kernel32", use_last_error=True)
            kernel.CreateJobObjectW.argtypes = [ctypes.c_void_p, wintypes.LPCWSTR]
            kernel.CreateJobObjectW.restype = wintypes.HANDLE
            kernel.SetInformationJobObject.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD]
            kernel.AssignProcessToJobObject.argtypes = [wintypes.HANDLE, wintypes.HANDLE]
            kernel.CloseHandle.argtypes = [wintypes.HANDLE]
            handle = kernel.CreateJobObjectW(None, None)
            limits = Extended()
            limits.BasicLimitInformation.LimitFlags = 0x2000 | 0x100 | 0x8
            limits.BasicLimitInformation.ActiveProcessLimit = 1
            limits.ProcessMemoryLimit = 512 * 1024 * 1024
            if not handle or not kernel.SetInformationJobObject(handle, 9, ctypes.byref(limits), ctypes.sizeof(limits)):
                if handle:
                    kernel.CloseHandle(handle)
                raise OSError("Impossible de configurer les limites du processus Windows.")
            if not kernel.AssignProcessToJobObject(handle, int(process._handle)):
                kernel.CloseHandle(handle)
                raise OSError("Impossible d'isoler le processus dans un Job Object Windows.")
            self.handle, self.kernel = handle, kernel

    def stop(self):
        if self.handle:
            self.kernel.CloseHandle(self.handle)
            self.handle = None
        elif os.name != "nt":
            try:
                os.killpg(self.process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        elif self.process.poll() is None:
            self.process.kill()


def worker_command():
    from pathlib import Path
    if getattr(sys, "frozen", False):
        name = "MrPythonWorker.exe" if os.name == "nt" else "MrPythonWorker"
        return [str(Path(sys.executable).with_name(name)), "--worker"]
    # Windows venv python.exe is a redirector which may launch another process.
    # Start the actual interpreter before imposing the one-process Job limit.
    # The headless engine only depends on the standard library and vendored code.
    executable = Path(getattr(sys, "_base_executable", sys.executable) if os.name == "nt" else sys.executable)
    if executable.name.lower() == "pythonw.exe":
        executable = executable.with_name("python.exe")
    return [str(executable), "-I", str(Path(__file__).resolve().parent.parent / "run.py"), "--worker"]
