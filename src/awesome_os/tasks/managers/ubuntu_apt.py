"""Ubuntu `apt` installer backend.

This installer wraps `apt-get` to provide a simple, uniform interface for the
setup application.

Notes:
    - Commands are executed via `awesome_os.commands.run`.
    - Logging goes through `awesome_os.logger`.
    - `install()` currently runs `apt-get update` before installing each
      package. This is safe but can be slow; batching may be added later.
"""

from __future__ import annotations

from awesome_os import logger
from awesome_os.tasks.commands import run

from awesome_os.tasks.managers.base import InstallResult
from awesome_os.tasks.task import TaskResult


class UbuntuAptManager:
    """Ubuntu `apt-get` package manager backend.

    This backend provides both package installation and system maintenance
    operations.
    """

    name = "apt"

    def is_installed(self, package: str) -> bool:
        """Return whether the given package is already installed."""
        res = run(["dpkg", "-s", package], check=False)
        return res.returncode == 0

    def install(self, package: str) -> InstallResult:
        """Install a package using `apt-get`."""
        logger.info(f"Installing {package} via {self.name}...")
        update_res = run(["sudo", "apt-get", "update", "-y"], check=False)
        install_res = run(["sudo", "apt-get", "install", "-y", package], check=False)
        if update_res.returncode == 0 and install_res.returncode == 0:
            return InstallResult(ok=True, summary=f"Installed {package}")

        details = (
            (update_res.stdout + "\n" + update_res.stderr).strip()
            + "\n"
            + (install_res.stdout + "\n" + install_res.stderr).strip()
        ).strip()
        return InstallResult(ok=False, summary=f"Failed to install {package}", details=details)

    def update(self) -> TaskResult:
        res = run(["sudo", "apt-get", "update", "-y"], check=False)
        if res.returncode == 0:
            return TaskResult(ok=True, summary="apt update: done")
        details = (res.stdout + "\n" + res.stderr).strip()
        return TaskResult(ok=False, summary="apt update: failed", details=details)

    def upgrade(self) -> TaskResult:
        res = run(["sudo", "apt-get", "upgrade", "-y"], check=False)
        if res.returncode == 0:
            return TaskResult(ok=True, summary="apt upgrade: done")
        details = (res.stdout + "\n" + res.stderr).strip()
        return TaskResult(ok=False, summary="apt upgrade: failed", details=details)

    def cleanup(self) -> TaskResult:
        res = run(["sudo", "apt-get", "autoremove", "-y"], check=False)
        if res.returncode == 0:
            return TaskResult(ok=True, summary="apt cleanup (autoremove): done")
        details = (res.stdout + "\n" + res.stderr).strip()
        return TaskResult(ok=False, summary="apt cleanup (autoremove): failed", details=details)
