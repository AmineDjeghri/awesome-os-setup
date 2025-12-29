from __future__ import annotations

import platform
from typing import Callable

from awesome_os.tasks.system.chezmoi_tasks import (
    configure_dotfiles,
    install_chezmoi,
    chezmoi_apply,
    chezmoi_diff,
    chezmoi_init,
    chezmoi_update,
    setup_zsh_p10k,
)
from awesome_os.tasks.system.nvidia_tasks import detect_cuda, detect_nvidia, setup_cuda
from awesome_os.tasks.managers.base import PackageManager
from awesome_os.tasks.managers.ubuntu_snap import UbuntuSnapManager
from awesome_os.tasks.managers.ubuntu_apt import UbuntuAptManager
from awesome_os.tasks.task import TaskResult

_PACKAGE_MANAGER_FACTORY_BY_DISTRO: dict[str, dict[str, Callable[[], PackageManager]]] = {
    "ubuntu": {"apt": UbuntuAptManager, "snap": UbuntuSnapManager},
}


def get_package_manager(*, distro: str, manager: str) -> PackageManager | None:
    """Return a unified package manager backend for the given environment.

    Args:
        distro: A normalized distro identifier (e.g. `"ubuntu"`).
        manager: The package manager identifier (e.g. `"apt"`).

    Returns:
        A `PackageManager` instance if supported, otherwise `None`.
    """
    factory = _PACKAGE_MANAGER_FACTORY_BY_DISTRO.get(distro, {}).get(manager)
    return factory() if factory else None


def get_system_action_sections(
    *, distro: str
) -> list[tuple[str, list[tuple[str, Callable[[], TaskResult]]]]]:
    factories = _PACKAGE_MANAGER_FACTORY_BY_DISTRO.get(distro, {})
    system = platform.system().lower()

    sections: list[tuple[str, list[tuple[str, Callable[[], TaskResult]]]]] = [
        (
            "dotfiles",
            [
                ("configure dotfiles", configure_dotfiles),
                ("setup zsh/p10k", setup_zsh_p10k),
                ("install chezmoi", install_chezmoi),
                ("chezmoi init", chezmoi_init),
                ("chezmoi diff", chezmoi_diff),
                ("chezmoi apply", chezmoi_apply),
                ("chezmoi update", chezmoi_update),
            ],
        )
    ]

    system_actions: list[tuple[str, Callable[[], TaskResult]]] = []
    if system in {"windows", "linux"}:
        system_actions.extend(
            [
                ("detect nvidia", detect_nvidia),
                ("detect cuda", detect_cuda),
                ("setup cuda (advanced)", setup_cuda),
            ]
        )
    if system_actions:
        sections.append(("system", system_actions))

    for manager_name, factory in factories.items():
        pm = factory()
        sections.append(
            (
                manager_name,
                [
                    ("update", pm.update),
                    ("upgrade", pm.upgrade),
                    ("cleanup", pm.cleanup),
                ],
            )
        )

    return sections
