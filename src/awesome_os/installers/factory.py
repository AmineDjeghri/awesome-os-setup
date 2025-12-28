"""Installer selection.

This module centralizes the mapping from an OS/distro + package manager to a
concrete installer implementation.

The UI and task runner should use `get_installer()` to obtain an installer for
the current environment, then call:

- `installer.is_installed(package)` to skip already-installed packages.
- `installer.install(package)` to perform the install.
"""

from __future__ import annotations

from awesome_os.installers.base import Installer
from awesome_os.installers.ubuntu_apt import UbuntuAptInstaller


def get_installer(*, distro: str, manager: str) -> Installer | None:
    """Return an installer implementation for the given environment.

    Args:
        distro: A normalized distro identifier (e.g. `"ubuntu"`).
        manager: The package manager identifier (e.g. `"apt"`).

    Returns:
        An `Installer` instance if supported, otherwise `None`.
    """
    if distro == "ubuntu" and manager == "apt":
        return UbuntuAptInstaller()
    return None
