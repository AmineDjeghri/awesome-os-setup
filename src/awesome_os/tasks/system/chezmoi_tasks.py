from __future__ import annotations

import shutil
from pathlib import Path

from awesome_os.tasks.commands import run
from awesome_os.tasks.system.git import _detect_repo_origin_url
from awesome_os.tasks.task import TaskResult


def _ensure_chezmoi_initialized() -> TaskResult | None:
    if shutil.which("chezmoi") is None:
        return TaskResult(ok=False, summary="chezmoi not found on PATH")

    init_probe = run(["chezmoi", "source-path"], check=False)
    source_path = (init_probe.stdout or "").strip()
    if init_probe.returncode != 0 or not source_path or not Path(source_path).exists():
        return TaskResult(
            ok=False,
            summary="chezmoi not initialized",
            details="Run: dotfiles: chezmoi init",
        )
    return None


def chezmoi_init() -> TaskResult:
    if shutil.which("chezmoi") is None:
        return TaskResult(ok=False, summary="chezmoi not found on PATH")

    init_probe = run(["chezmoi", "source-path"], check=False)
    source_path = (init_probe.stdout or "").strip()
    if init_probe.returncode == 0 and source_path and Path(source_path).exists():
        return TaskResult(ok=True, summary="chezmoi already initialized")

    if shutil.which("git") is None:
        return TaskResult(ok=False, summary="git not found on PATH (required for chezmoi init)")

    url = _detect_repo_origin_url()
    if not url:
        return TaskResult(
            ok=False,
            summary="Could not detect git remote origin URL",
            details="Run manually: chezmoi init <your-dotfiles-repo>",
        )

    argv = ["chezmoi", "init", url]
    try:
        res = run(argv, check=False)
    except Exception as e:  # noqa: BLE001
        return TaskResult(ok=False, summary="chezmoi init: failed", details=str(e))

    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(ok=True, summary="chezmoi init: ok", details=details)
    return TaskResult(ok=False, summary="chezmoi init: failed", details=details)


def chezmoi_apply() -> TaskResult:
    guard = _ensure_chezmoi_initialized()
    if guard is not None:
        return guard

    argv = ["chezmoi", "apply"]
    try:
        res = run(argv, check=False)
    except Exception as e:  # noqa: BLE001
        return TaskResult(ok=False, summary="chezmoi apply: failed", details=str(e))

    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(ok=True, summary="chezmoi apply: ok", details=details)
    return TaskResult(ok=False, summary="chezmoi apply: failed", details=details)


def chezmoi_update() -> TaskResult:
    guard = _ensure_chezmoi_initialized()
    if guard is not None:
        return guard

    argv = ["chezmoi", "update"]
    try:
        res = run(argv, check=False)
    except Exception as e:  # noqa: BLE001
        return TaskResult(ok=False, summary="chezmoi update: failed", details=str(e))

    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(ok=True, summary="chezmoi update: ok", details=details)
    return TaskResult(ok=False, summary="chezmoi update: failed", details=details)
