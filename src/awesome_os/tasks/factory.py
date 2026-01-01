from __future__ import annotations

import os
from pathlib import Path
from typing import Callable

from pydantic import BaseModel, ConfigDict

from awesome_os.tasks.system.help import show_commands
from awesome_os.tasks.system.zsh import (
    apply_p10k_force,
    apply_zshrc_force,
    set_bash_as_default_shell,
    set_zsh_as_default_shell,
    sync_zsh_plugins_and_theme,
    uninstall_oh_my_zsh_and_p10k,
    uninstall_zsh_apt,
)
from awesome_os.detect_os import _is_wsl
from awesome_os.tasks.system.nvidia_tasks import (
    detect_cuda,
    detect_nvidia,
    setup_cuda,
    setup_nvidia_ubuntu,
    setup_nvidia_windows,
    setup_nvidia_wsl_instructions,
)
from awesome_os.tasks.managers.base import PackageManager
from awesome_os.tasks.managers.ubuntu_snap import UbuntuSnapManager
from awesome_os.tasks.managers.ubuntu_apt import UbuntuAptManager
from awesome_os.tasks.managers.windows_winget import WindowsWingetManager
from awesome_os.tasks.task import TaskResult
from awesome_os.tasks.system.windows_tasks import (
    apply_windows_terminal_ui_defaults,
    download_glazewm_config,
    install_or_move_wsl_ubuntu,
    install_wsl_ubuntu,
    update_windows_terminal_ubuntu_profile,
)

_PACKAGE_MANAGER_FACTORY_BY_DISTRO: dict[str, dict[str, Callable[[], PackageManager]]] = {
    "ubuntu": {"apt": UbuntuAptManager, "snap": UbuntuSnapManager},
    "windows": {"winget": WindowsWingetManager},
}


class SystemAction(BaseModel):
    model_config = ConfigDict(frozen=True, arbitrary_types_allowed=True)

    label: str
    run: Callable[[], TaskResult]
    prompt_label: str | None = None
    prompt_initial: str = ""
    run_with_prompt: Callable[[str], TaskResult] | None = None
    confirm: bool = False
    confirm_message: str | None = None
    backup_target: Path | None = None


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
    *, system: str, distro: str, info: str | None
) -> list[tuple[str, list[SystemAction]]]:
    home = Path.home()
    sections: list[tuple[str, list[SystemAction]]] = []
    if system in {"darwin", "linux"}:
        # help
        sections.append(
            (
                "help",
                [
                    SystemAction(label="show commands", run=show_commands),
                ],
            )
        )
        # zsh
        sections.append(
            (
                "zsh",
                [
                    SystemAction(
                        label="apply ~/.zshrc",
                        run=apply_zshrc_force,
                        confirm=True,
                        confirm_message="This will overwrite ~/.zshrc if it exists. Proceed? (A backup will be created)",
                        backup_target=(home / ".zshrc"),
                    ),
                    SystemAction(
                        label="apply ~/.p10k.zsh",
                        run=apply_p10k_force,
                        confirm=True,
                        confirm_message="FiraCode Nerd Font is required for best results. \n"
                        "This will overwrite ~/.p10k.zsh if it exists. Proceed? (A backup will be created)",
                        backup_target=(home / ".p10k.zsh"),
                    ),
                    SystemAction(label="sync zsh plugins/theme", run=sync_zsh_plugins_and_theme),
                    SystemAction(
                        label="set zsh as default shell",
                        run=set_zsh_as_default_shell,
                        confirm=True,
                        confirm_message="Set your default shell to zsh?",
                    ),
                ],
            )
        )
        # zsh uninstall
        sections.append(
            (
                "zsh uninstall",
                [
                    SystemAction(
                        label="uninstall: oh-my-zsh + p10k files",
                        run=uninstall_oh_my_zsh_and_p10k,
                        confirm=True,
                        confirm_message="This will delete oh-my-zsh and related zsh config files. Proceed?",
                    ),
                    SystemAction(
                        label="uninstall zsh (apt)",
                        run=uninstall_zsh_apt,
                        confirm=True,
                        confirm_message="This will uninstall zsh via apt (sudo required). Proceed?",
                    ),
                    SystemAction(
                        label="set bash as default shell",
                        run=set_bash_as_default_shell,
                        confirm=True,
                        confirm_message="Set your default shell to bash?",
                    ),
                ],
            )
        )

        # chezmoi
        # sections.append(
        #         (
        #             "chezmoi",
        #             [
        #                 SystemAction(label="chezmoi init", run=chezmoi_init),
        #                 SystemAction(label="chezmoi apply", run=chezmoi_apply),
        #                 SystemAction(label="chezmoi update", run=chezmoi_update),
        #             ],
        #         )
        #     )

    # NVIDIA
    if system in {"windows", "linux"}:
        nvidia_actions: list[SystemAction] = [
            SystemAction(label="detect nvidia", run=detect_nvidia)
        ]

        if system == "windows":
            nvidia_actions.append(
                SystemAction(
                    label="setup nvidia (windows)",
                    run=setup_nvidia_windows,
                    confirm=True,
                    confirm_message="This will show NVIDIA setup guidance for Windows. Proceed?",
                )
            )
        elif system == "linux" and _is_wsl():
            nvidia_actions.append(
                SystemAction(
                    label="setup nvidia (wsl)",
                    run=setup_nvidia_wsl_instructions,
                    confirm=True,
                    confirm_message="This will show NVIDIA setup guidance for WSL (Windows host driver). Proceed?",
                )
            )
        elif distro == "ubuntu":
            nvidia_actions.append(
                SystemAction(
                    label="setup nvidia (ubuntu)",
                    run=setup_nvidia_ubuntu,
                    confirm=True,
                    confirm_message="This will attempt to install NVIDIA drivers on Ubuntu (reboot required). Proceed?",
                )
            )
        else:
            nvidia_actions.append(
                SystemAction(
                    label=f"setup nvidia ({distro})",
                    run=lambda: TaskResult(
                        ok=False, summary=f"NVIDIA setup not implemented for distro: {distro}"
                    ),
                    confirm=True,
                    confirm_message=f"NVIDIA setup is not implemented for distro '{distro}'. Proceed to show details?",
                )
            )

        sections.append(
            (
                "system",
                [
                    *nvidia_actions,
                    SystemAction(label="detect cuda", run=detect_cuda),
                    SystemAction(label="setup cuda (advanced)", run=setup_cuda),
                ],
            )
        )

    if system == "windows":
        settings_path = (
            Path(os.environ.get("LOCALAPPDATA", ""))
            / "Packages"
            / "Microsoft.WindowsTerminal_8wekyb3d8bbwe"
            / "LocalState"
            / "settings.json"
        )

        sections.append(
            (
                "windows",
                [
                    SystemAction(
                        label="install WSL (Ubuntu)",
                        run=install_wsl_ubuntu,
                        confirm=True,
                        confirm_message="This will run wsl.exe --install for Ubuntu. Proceed?",
                    ),
                    SystemAction(
                        label="install/move WSL (Ubuntu) to a folder",
                        run=lambda: TaskResult(
                            ok=True,
                            summary="Provide a target directory to move Ubuntu, or leave empty for default install.",
                        ),
                        run_with_prompt=install_or_move_wsl_ubuntu,
                        prompt_label="Target directory for Ubuntu WSL (leave empty for default). Example: D:\\WSL\\Ubuntu",
                        prompt_initial="",
                        confirm=True,
                        confirm_message=(
                            "If you provide a directory, this will export and UNREGISTER the current Ubuntu distro, "
                            "then import it into the new folder. Proceed?"
                        ),
                    ),
                    SystemAction(
                        label="update Windows Terminal Ubuntu profile",
                        run=update_windows_terminal_ubuntu_profile,
                        confirm=True,
                        confirm_message="This will update Windows Terminal settings.json (Ubuntu profile). Proceed?",
                        backup_target=settings_path,
                    ),
                    SystemAction(
                        label="apply Windows Terminal UI defaults",
                        run=apply_windows_terminal_ui_defaults,
                        confirm=True,
                        confirm_message="This will update Windows Terminal settings.json (theme/font/opacity). Proceed?",
                        backup_target=settings_path,
                    ),
                    SystemAction(
                        label="install GlazeWM config",
                        run=download_glazewm_config,
                        confirm=True,
                        confirm_message="This will download and overwrite GlazeWM config.yaml. Proceed?",
                    ),
                ],
            )
        )

    # Package managers (apt, snap, brew...)
    factories = _PACKAGE_MANAGER_FACTORY_BY_DISTRO.get(distro, {})
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
