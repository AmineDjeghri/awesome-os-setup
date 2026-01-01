from __future__ import annotations

import json
import os
from pathlib import Path
import tempfile
from urllib.request import urlopen

from awesome_os.tasks.commands import run
from awesome_os.tasks.task import TaskResult


def _windows_terminal_settings_path() -> Path:
    localappdata = os.environ.get("LOCALAPPDATA")
    if not localappdata:
        return Path("")
    return (
        Path(localappdata)
        / "Packages"
        / "Microsoft.WindowsTerminal_8wekyb3d8bbwe"
        / "LocalState"
        / "settings.json"
    )


def install_wsl_ubuntu() -> TaskResult:
    res = run(["wsl.exe", "--install", "-d", "Ubuntu", "--no-launch"], check=False)
    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(
            ok=True,
            summary="WSL install started (Ubuntu)",
            details=(
                details
                or "If Ubuntu doesn't start automatically, open a new terminal and run: ubuntu"
            ),
        )
    return TaskResult(ok=False, summary="WSL install failed", details=details)


def install_or_move_wsl_ubuntu(target_dir: str) -> TaskResult:
    """Install Ubuntu WSL, optionally relocating it to a user-selected folder.

    Notes:
        - `wsl.exe --install` does not support a custom install directory.
        - Relocation is done via: export -> unregister -> import.
        - If `target_dir` is empty/whitespace, we use the default WSL install.
    """
    target_dir = (target_dir or "").strip()
    if not target_dir:
        return install_wsl_ubuntu()

    # We only support moving an existing registered distro. Installing directly
    # into a custom location is not supported by WSL.
    list_res = run(["wsl.exe", "-l", "-q"], check=False)
    installed = any(line.strip() == "Ubuntu" for line in list_res.stdout.splitlines())
    if not installed:
        return TaskResult(
            ok=False,
            summary="Ubuntu WSL is not installed yet",
            details=(
                "Install Ubuntu first (default WSL location) using the 'install WSL (Ubuntu)' action, "
                "then re-run this action to move it to a custom folder."
            ),
        )

    if not os.path.isabs(target_dir):
        return TaskResult(
            ok=False,
            summary="Invalid target directory",
            details="Please provide an absolute Windows path, e.g. D:\\WSL\\Ubuntu",
        )

    try:
        Path(target_dir).mkdir(parents=True, exist_ok=True)
    except Exception as e:  # noqa: BLE001
        return TaskResult(ok=False, summary="Create target directory failed", details=str(e))

    export_path = Path(tempfile.gettempdir()) / "awesome_os_ubuntu_wsl_export.tar"

    export_res = run(["wsl.exe", "--export", "Ubuntu", str(export_path)], check=False)
    export_details = (export_res.stdout + "\n" + export_res.stderr).strip()
    if export_res.returncode != 0:
        return TaskResult(
            ok=False,
            summary="WSL export failed (Ubuntu)",
            details=export_details,
        )

    unreg_res = run(["wsl.exe", "--unregister", "Ubuntu"], check=False)
    unreg_details = (unreg_res.stdout + "\n" + unreg_res.stderr).strip()
    if unreg_res.returncode != 0:
        return TaskResult(
            ok=False,
            summary="WSL unregister failed (Ubuntu)",
            details=unreg_details,
        )

    import_res = run(
        ["wsl.exe", "--import", "Ubuntu", target_dir, str(export_path), "--version", "2"],
        check=False,
    )
    import_details = (import_res.stdout + "\n" + import_res.stderr).strip()
    try:
        export_path.unlink(missing_ok=True)
    except Exception:
        pass

    if import_res.returncode != 0:
        return TaskResult(
            ok=False,
            summary="WSL import failed (Ubuntu)",
            details=import_details,
        )

    return TaskResult(
        ok=True,
        summary="Ubuntu WSL moved successfully",
        details=(
            f"Imported Ubuntu into: {target_dir}\n"
            "Next steps:\n"
            "- Start it: ubuntu\n"
            "- If needed: wsl.exe -d Ubuntu"
        ),
    )


def update_windows_terminal_ubuntu_profile() -> TaskResult:
    settings_path = _windows_terminal_settings_path()
    if not settings_path.exists():
        return TaskResult(
            ok=False,
            summary="Windows Terminal settings.json not found",
            details=str(settings_path),
        )

    try:
        data = json.loads(settings_path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return TaskResult(
            ok=False, summary="read Windows Terminal settings: failed", details=str(e)
        )

    profiles = (data.get("profiles") or {}).get("list")
    if not isinstance(profiles, list):
        return TaskResult(ok=False, summary="Windows Terminal settings: profiles.list missing")

    updated = False
    for p in profiles:
        if not isinstance(p, dict):
            continue
        if p.get("name") != "Ubuntu":
            continue
        p["startingDirectory"] = "~"
        p["commandline"] = "ubuntu run"
        updated = True
        break

    if not updated:
        return TaskResult(ok=False, summary="Ubuntu profile not found in Windows Terminal settings")

    try:
        settings_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except Exception as e:  # noqa: BLE001
        return TaskResult(
            ok=False, summary="write Windows Terminal settings: failed", details=str(e)
        )

    return TaskResult(ok=True, summary="Windows Terminal: updated Ubuntu profile")


def apply_windows_terminal_ui_defaults() -> TaskResult:
    settings_path = _windows_terminal_settings_path()
    if not settings_path.exists():
        return TaskResult(
            ok=False,
            summary="Windows Terminal settings.json not found",
            details=str(settings_path),
        )

    try:
        data = json.loads(settings_path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return TaskResult(
            ok=False, summary="read Windows Terminal settings: failed", details=str(e)
        )

    profiles = data.get("profiles")
    if not isinstance(profiles, dict):
        profiles = {}
        data["profiles"] = profiles

    defaults = profiles.get("defaults")
    if not isinstance(defaults, dict):
        defaults = {}
        profiles["defaults"] = defaults

    schemes = data.get("schemes")
    if not isinstance(schemes, list):
        schemes = []
        data["schemes"] = schemes

    night_owl = {
        "name": "Night Owl",
        "cursorColor": "#80a4c2",
        "selectionBackground": "#1d3b53",
        "background": "#011627",
        "foreground": "#D6DEEB",
        "black": "#011627",
        "blue": "#82AAFF",
        "cyan": "#21C7A8",
        "green": "#22DA6E",
        "purple": "#C792EA",
        "red": "#EF5350",
        "white": "#FFFFFF",
        "yellow": "#c5e478",
        "brightBlack": "#575656",
        "brightBlue": "#82AAFF",
        "brightCyan": "#7FDBCA",
        "brightGreen": "#22DA6E",
        "brightPurple": "#C792EA",
        "brightRed": "#EF5350",
        "brightWhite": "#FFFFFF",
        "brightYellow": "#FFEB95",
    }

    if not any(isinstance(s, dict) and s.get("name") == "Night Owl" for s in schemes):
        schemes.append(night_owl)

    defaults["colorScheme"] = "Night Owl"
    defaults["font"] = {"face": "JetBrainsMono Nerd Font", "size": 12.0}
    defaults["opacity"] = 90
    defaults["elevate"] = True
    defaults["selectionBackground"] = "#FFFF00"

    try:
        settings_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except Exception as e:  # noqa: BLE001
        return TaskResult(
            ok=False, summary="write Windows Terminal settings: failed", details=str(e)
        )

    return TaskResult(ok=True, summary="Windows Terminal UI defaults applied")


def download_glazewm_config() -> TaskResult:
    userprofile = os.environ.get("USERPROFILE")
    if not userprofile:
        return TaskResult(ok=False, summary="USERPROFILE not set")

    dest_dir = Path(userprofile) / ".glzr" / "glazewm"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "config.yaml"

    url = "https://raw.githubusercontent.com/AmineDjeghri/awesome-os-setup/main/docs/windows_workflow/win_dotfiles/.glzr/glazewm/config.yaml"

    try:
        with urlopen(url) as resp:  # noqa: S310
            content = resp.read()
        dest.write_bytes(content)
    except Exception as e:  # noqa: BLE001
        return TaskResult(ok=False, summary="download GlazeWM config: failed", details=str(e))

    return TaskResult(ok=True, summary="GlazeWM config installed", details=str(dest))
