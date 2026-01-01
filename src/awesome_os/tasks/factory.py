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
    install_wsl_ubuntu,
    update_windows_terminal_ubuntu_profile,
    wsl_export,
    wsl_import,
    wsl_install,
    wsl_list_online,
    wsl_list_verbose,
    wsl_move,
    wsl_shutdown,
    wsl_unregister,
    wsl_update,
    wsl_version,
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
                "wsl",
                [
                    SystemAction(label="installed distros", run=wsl_list_verbose),
                    SystemAction(label="online distros", run=wsl_list_online),
                    SystemAction(
                        label="install distro",
                        run=lambda: TaskResult(
                            ok=True,
                            summary=(
                                "Provide input as: <DistributionName>|location=<Folder(optional)>\n"
                                "Examples:\n"
                                "- Ubuntu\n"
                                "- Ubuntu|location=D:\\WSL\\Ubuntu\n"
                                "Note: this action uses --no-launch by default."
                            ),
                        ),
                        run_with_prompt=wsl_install,
                        prompt_label=(
                            "Install input: <DistributionName>|location=<Folder(optional)>\n"
                            "Example: Ubuntu|location=D:\\WSL\\Ubuntu"
                        ),
                        prompt_initial="Ubuntu",
                        confirm=True,
                        confirm_message="This will run wsl --install (no-launch by default). Proceed?",
                    ),
                    SystemAction(label="version", run=wsl_version),
                    SystemAction(
                        label="update WSL",
                        run=wsl_update,
                        confirm=True,
                        confirm_message="This will update WSL components. Proceed?",
                    ),
                    SystemAction(
                        label="shutdown WSL",
                        run=wsl_shutdown,
                        confirm=True,
                        confirm_message="This will shut down all running WSL distros. Proceed?",
                    ),
                    SystemAction(
                        label="Export distro",
                        run=lambda: TaskResult(
                            ok=True,
                            summary="Provide input as: <DistributionName>|<FileName> . For example: "
                            "Ubuntu|C:\\Temp\\ubuntu.tar  . You can get the distro name with the button 'installed "
                            "distros'",
                        ),
                        run_with_prompt=wsl_export,
                        prompt_label="Export input: <DistributionName>|<FileName>  e.g. Ubuntu|C:\\Temp\\ubuntu.tar",
                        prompt_initial="Ubuntu|C:\\Temp\\ubuntu.tar",
                        confirm=True,
                        confirm_message="This will export the distro to a tar file. Proceed?",
                    ),
                    SystemAction(
                        label="Import distro",
                        run=lambda: TaskResult(
                            ok=True,
                            summary="Provide input as: <DistributionName>|<InstallLocation>|<FileName>",
                        ),
                        run_with_prompt=wsl_import,
                        prompt_label=(
                            "Import input: <DistributionName>|<InstallLocation>|<FileName>"
                            "e.g. Ubuntu|D:\\WSL\\Ubuntu|C:\\Temp\\ubuntu.tar"
                        ),
                        prompt_initial="Ubuntu|D:\\WSL\\Ubuntu|C:\\Temp\\ubuntu.tar",
                        confirm=True,
                        confirm_message="This will import a distro from a tar file. Proceed?",
                    ),
                    SystemAction(
                        label="Delete distro",
                        run=lambda: TaskResult(
                            ok=True,
                            summary="Provide the DistributionName to unregister",
                        ),
                        run_with_prompt=wsl_unregister,
                        prompt_label="DistributionName to unregister (DELETES the distro)",
                        prompt_initial="Ubuntu",
                        confirm=True,
                        confirm_message="This will unregister (DELETE) the distro. Proceed?",
                    ),
                    SystemAction(
                        label="Move distro to new location",
                        run=lambda: TaskResult(
                            ok=True,
                            summary="Provide input as: <DistributionName>|<NewLocation>",
                        ),
                        run_with_prompt=wsl_move,
                        prompt_label="Move input: <DistributionName>|<NewLocation>  e.g. Ubuntu|D:\\WSL\\Ubuntu",
                        prompt_initial="Ubuntu|D:\\WSL\\Ubuntu",
                        confirm=True,
                        confirm_message=("This will move the distro to a new location. Proceed?"),
                    ),
                ],
            )
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
