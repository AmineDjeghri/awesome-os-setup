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
from awesome_os.commands import run

from awesome_os.installers.base import InstallResult


class UbuntuAptInstaller:
    """Installer implementation for Ubuntu using `apt-get`."""

    name = "apt"

    def is_installed(self, package: str) -> bool:
        """Return whether the given package is already installed.

        Args:
            package: The apt package name.

        Returns:
            True if `dpkg -s` reports the package is installed.
        """
        res = run(["bash", "-lc", f"dpkg -s {package} >/dev/null 2>&1"], check=False)
        return res.returncode == 0

    def install(self, package: str) -> InstallResult:
        """Install a package using `apt-get`.

        Args:
            package: The apt package name.

        Returns:
            An `InstallResult` with `ok=True` on success. On failure, `details`
            contains a best-effort concatenation of stdout/stderr.
        """
        logger.info(f"Installing {package} via apt...")
        res = run(
            ["bash", "-lc", f"sudo apt-get update -y && sudo apt-get install -y {package}"],
            check=False,
        )
        if res.returncode == 0:
            return InstallResult(ok=True, summary=f"Installed {package}")
        details = (res.stdout + "\n" + res.stderr).strip()
        return InstallResult(ok=False, summary=f"Failed to install {package}", details=details)
