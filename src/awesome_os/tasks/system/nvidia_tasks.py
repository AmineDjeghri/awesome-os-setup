from __future__ import annotations

import platform
import shutil

from awesome_os.tasks.commands import run
from awesome_os.tasks.task import TaskResult


def _command_exists(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def detect_nvidia() -> TaskResult:
    """Detect NVIDIA driver availability via `nvidia-smi`.

    Works on Linux and Windows (including CUDA on Windows).
    """
    if not _command_exists("nvidia-smi"):
        system = platform.system().lower()
        return TaskResult(ok=False, summary=f"nvidia-smi not found on PATH ({system})")

    # Keep it simple: run a lightweight query.
    res = run(["nvidia-smi", "-L"], check=False)
    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(ok=True, summary="nvidia-smi: ok", details=details)
    return TaskResult(ok=False, summary="nvidia-smi: failed", details=details)


def detect_cuda() -> TaskResult:
    """High-level CUDA detection.

    Simple rule: CUDA is considered present if `nvcc` is available.
    """
    system = platform.system().lower()
    if not _command_exists("nvcc"):
        return TaskResult(ok=False, summary=f"CUDA not detected (nvcc missing) ({system})")

    res = run(["nvcc", "--version"], check=False)
    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(ok=True, summary="CUDA detected (nvcc available)", details=details)
    return TaskResult(ok=False, summary="CUDA not detected (nvcc failed)", details=details)


def setup_cuda() -> TaskResult:
    """Advanced: CUDA setup task (placeholder).

    Keeping it simple for now: report-only stub.
    """
    system = platform.system().lower()
    return TaskResult(
        ok=False,
        summary=f"CUDA setup (advanced) not implemented yet ({system})",
        details="Planned: provide guided installation steps for Windows/Linux, then validate with nvcc and nvidia-smi.",
    )
