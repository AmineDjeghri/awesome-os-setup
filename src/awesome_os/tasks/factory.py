from __future__ import annotations

from pathlib import Path
import platform
from typing import Callable

from pydantic import BaseModel, ConfigDict

from awesome_os.tasks.system.chezmoi_tasks import (
    chezmoi_apply,
    chezmoi_diff,
    chezmoi_init,
    chezmoi_update,
)
from awesome_os.tasks.system.help import show_commands
from awesome_os.tasks.system.zsh import (
    apply_p10k,
    apply_p10k_force,
    apply_zshrc,
    apply_zshrc_force,
    set_bash_as_default_shell,
    set_zsh_as_default_shell,
    sync_zsh_plugins_and_theme,
    uninstall_oh_my_zsh_and_p10k,
    uninstall_zsh_apt,
)
from awesome_os.tasks.system.nvidia_tasks import detect_cuda, detect_nvidia, setup_cuda
from awesome_os.tasks.managers.base import PackageManager
from awesome_os.tasks.managers.ubuntu_snap import UbuntuSnapManager
from awesome_os.tasks.managers.ubuntu_apt import UbuntuAptManager
from awesome_os.tasks.task import TaskResult

_PACKAGE_MANAGER_FACTORY_BY_DISTRO: dict[str, dict[str, Callable[[], PackageManager]]] = {
    "ubuntu": {"apt": UbuntuAptManager, "snap": UbuntuSnapManager},
}


class SystemAction(BaseModel):
    model_config = ConfigDict(frozen=True, arbitrary_types_allowed=True)

    label: str
    run: Callable[[], TaskResult]
    confirm: bool = False
    backup_target: Path | None = None
    backup_default: Path | None = None


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


def get_system_action_sections(*, distro: str) -> list[tuple[str, list[SystemAction]]]:
    factories = _PACKAGE_MANAGER_FACTORY_BY_DISTRO.get(distro, {})
    system = platform.system().lower()

    home = Path.home()
    sections: list[tuple[str, list[SystemAction]]] = [
        (
            "help",
            [
                SystemAction(label="show commands", run=show_commands),
            ],
        ),
        (
            "zsh",
            [
                SystemAction(label="apply ~/.zshrc", run=apply_zshrc),
                SystemAction(
                    label="apply ~/.zshrc (force)",
                    run=apply_zshrc_force,
                    confirm=True,
                    backup_target=(home / ".zshrc"),
                    backup_default=(home / ".zshrc.bak"),
                ),
                SystemAction(label="apply ~/.p10k.zsh", run=apply_p10k),
                SystemAction(
                    label="apply ~/.p10k.zsh (force)",
                    run=apply_p10k_force,
                    confirm=True,
                    backup_target=(home / ".p10k.zsh"),
                    backup_default=(home / ".p10k.zsh.bak"),
                ),
                SystemAction(label="sync zsh plugins/theme", run=sync_zsh_plugins_and_theme),
                SystemAction(
                    label="set zsh as default shell", run=set_zsh_as_default_shell, confirm=True
                ),
            ],
        ),
        (
            "zsh uninstall",
            [
                SystemAction(
                    label="uninstall: oh-my-zsh + p10k files",
                    run=uninstall_oh_my_zsh_and_p10k,
                    confirm=True,
                ),
                SystemAction(
                    label="uninstall zsh (apt)",
                    run=uninstall_zsh_apt,
                    confirm=True,
                ),
                SystemAction(
                    label="set bash as default shell", run=set_bash_as_default_shell, confirm=True
                ),
            ],
        ),
        (
            "advanced",
            [
                SystemAction(label="chezmoi init", run=chezmoi_init),
                SystemAction(label="chezmoi diff", run=chezmoi_diff),
                SystemAction(label="chezmoi apply", run=chezmoi_apply),
                SystemAction(label="chezmoi update", run=chezmoi_update),
            ],
        ),
    ]

    if system in {"windows", "linux"}:
        sections.append(
            (
                "system",
                [
                    SystemAction(label="detect nvidia", run=detect_nvidia),
                    SystemAction(label="detect cuda", run=detect_cuda),
                    SystemAction(label="setup cuda (advanced)", run=setup_cuda),
                ],
            )
        )

    for manager_name, factory in factories.items():
        pm = factory()
        sections.append(
            (
                manager_name,
                [
                    SystemAction(label="update", run=pm.update),
                    SystemAction(label="upgrade", run=pm.upgrade),
                    SystemAction(label="cleanup", run=pm.cleanup),
                ],
            )
        )

    return sections
