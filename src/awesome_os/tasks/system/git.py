from __future__ import annotations

from pathlib import Path

from awesome_os.tasks.commands import run
from awesome_os.tasks.task import TaskResult


def _detect_repo_origin_url() -> str:
    res = run(["git", "config", "--get", "remote.origin.url"], check=False)
    url = (res.stdout or "").strip()
    return url


def _git_clone(*, url: str, dest: Path, depth_1: bool = True) -> TaskResult:
    argv = ["git", "clone"]
    if depth_1:
        argv.extend(["--depth=1"])
    argv.extend([url, str(dest)])
    res = run(argv, check=False)
    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(ok=True, summary=f"cloned: {dest.name}", details=details)
    return TaskResult(ok=False, summary=f"clone {dest.name}: failed", details=details)
