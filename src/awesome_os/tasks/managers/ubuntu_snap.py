from __future__ import annotations

from awesome_os import logger
from awesome_os.tasks.commands import run
from awesome_os.tasks.managers.base import InstallResult
from awesome_os.tasks.task import TaskResult


class UbuntuSnapManager:
    name = "snap"

    def is_installed(self, package: str) -> bool:
        res = run(["snap", "list", package], check=False)
        return res.returncode == 0

    def install(self, package: str) -> InstallResult:
        logger.info(f"Installing {package} via {self.name}...")
        argv = ["sudo", "snap", "install", package]
        if package == "chezmoi":
            argv.append("--classic")
        res = run(argv, check=False)
        if res.returncode == 0:
            return InstallResult(ok=True, summary=f"Installed {package}")
        details = (res.stdout + "\n" + res.stderr).strip()
        return InstallResult(ok=False, summary=f"Failed to install {package}", details=details)

    def update(self) -> TaskResult:
        res = run(["sudo", "snap", "refresh"], check=False)
        if res.returncode == 0:
            return TaskResult(ok=True, summary="snap refresh: done")
        details = (res.stdout + "\n" + res.stderr).strip()
        return TaskResult(ok=False, summary="snap refresh: failed", details=details)

    def upgrade(self) -> TaskResult:
        return self.update()

    def cleanup(self) -> TaskResult:
        return TaskResult(ok=True, summary="snap cleanup: no-op")
