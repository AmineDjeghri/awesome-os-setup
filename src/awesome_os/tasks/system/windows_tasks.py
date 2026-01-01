from __future__ import annotations

import json
import os
from pathlib import Path
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


def wsl_install(value: str) -> TaskResult:
    parts = [p.strip() for p in (value or "").split("|") if p.strip()]
    distro = parts[0] if parts else ""
    options = parts[1:] if parts else []

    location: str | None = None
    flags: set[str] = set()
    for opt in options:
        if "=" in opt:
            k, v = [x.strip() for x in opt.split("=", 1)]
            if k.lower() == "location":
                location = v
        else:
            flags.add(opt.lower())

    argv: list[str] = ["wsl.exe", "--install"]
    if distro:
        argv += ["--distribution", distro]
    # Default behavior: don't auto-launch the distro after install.
    argv.append("--no-launch")
    if location:
        argv += ["--location", location]

    res = run(argv, check=False)
    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(ok=True, summary=f"wsl --install {distro}".strip(), details=details)
    return TaskResult(ok=False, summary=f"wsl --install {distro} failed".strip(), details=details)


def wsl_list_online() -> TaskResult:
    res = run(["wsl.exe", "--list", "--online"], check=False)
    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(ok=True, summary="wsl --list --online", details=details)
    return TaskResult(ok=False, summary="wsl --list --online failed", details=details)


def wsl_list_verbose() -> TaskResult:
    res = run(["wsl.exe", "--list", "--verbose"], check=False)
    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(ok=True, summary="wsl --list --verbose", details=details)
    return TaskResult(ok=False, summary="wsl --list --verbose failed", details=details)


def wsl_update() -> TaskResult:
    res = run(["wsl.exe", "--update"], check=False)
    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(ok=True, summary="wsl --update", details=details)
    return TaskResult(ok=False, summary="wsl --update failed", details=details)


def wsl_version() -> TaskResult:
    res = run(["wsl.exe", "--version"], check=False)
    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(ok=True, summary="wsl --version", details=details)
    return TaskResult(ok=False, summary="wsl --version failed", details=details)


def wsl_shutdown() -> TaskResult:
    res = run(["wsl.exe", "--shutdown"], check=False)
    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(ok=True, summary="wsl --shutdown", details=details)
    return TaskResult(ok=False, summary="wsl --shutdown failed", details=details)


def _parse_two_fields(value: str, *, sep: str = "|") -> tuple[str, str] | None:
    parts = [p.strip() for p in (value or "").split(sep, 1)]
    if len(parts) != 2:
        return None
    if not parts[0] or not parts[1]:
        return None
    return parts[0], parts[1]


def wsl_unregister(distribution: str) -> TaskResult:
    distribution = (distribution or "").strip()
    if not distribution:
        return TaskResult(ok=False, summary="wsl --unregister: missing distribution name")
    res = run(["wsl.exe", "--unregister", distribution], check=False)
    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(ok=True, summary=f"wsl --unregister {distribution}", details=details)
    return TaskResult(ok=False, summary=f"wsl --unregister {distribution} failed", details=details)


def wsl_export(value: str) -> TaskResult:
    parsed = _parse_two_fields(value)
    if parsed is None:
        return TaskResult(
            ok=False,
            summary="wsl --export: invalid input",
            details="Expected format: <DistributionName>|<FileName>, e.g. Ubuntu|C:\\Temp\\ubuntu.tar",
        )
    distro, filename = parsed
    res = run(["wsl.exe", "--export", distro, filename], check=False)
    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(ok=True, summary=f"wsl --export {distro}", details=details)
    return TaskResult(ok=False, summary=f"wsl --export {distro} failed", details=details)


def wsl_import(value: str) -> TaskResult:
    parts = [p.strip() for p in (value or "").split("|")]
    if len(parts) < 3 or not parts[0] or not parts[1] or not parts[2]:
        return TaskResult(
            ok=False,
            summary="wsl --import: invalid input",
            details=(
                "Expected format: <DistributionName>|<InstallLocation>|<FileName>, "
                "e.g. Ubuntu|D:\\WSL\\Ubuntu|C:\\Temp\\ubuntu.tar"
            ),
        )

    distro, install_location, filename = parts[0], parts[1], parts[2]
    argv = ["wsl.exe", "--import", distro, install_location, filename]
    if len(parts) >= 4 and parts[3]:
        argv += ["--version", parts[3]]
    res = run(argv, check=False)
    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(ok=True, summary=f"wsl --import {distro}", details=details)
    return TaskResult(ok=False, summary=f"wsl --import {distro} failed", details=details)


def wsl_move(value: str) -> TaskResult:
    parsed = _parse_two_fields(value)
    if parsed is None:
        return TaskResult(
            ok=False,
            summary="wsl --manage --move: invalid input",
            details="Expected format: <DistributionName>|<NewLocation>, e.g. Ubuntu|D:\\WSL\\Ubuntu",
        )
    distro, new_location = parsed

    manage_res = run(["wsl.exe", "--manage", distro, "--move", new_location], check=False)
    manage_details = (manage_res.stdout + "\n" + manage_res.stderr).strip()
    if manage_res.returncode == 0:
        return TaskResult(ok=True, summary=f"wsl --manage {distro} --move", details=manage_details)
    return TaskResult(
        ok=False, summary=f"wsl --manage {distro} --move failed", details=manage_details
    )


def update_windows_terminal_ubuntu_profile() -> TaskResult:
    # First, ensure WSL is available and an Ubuntu distro is installed.
    wsl_res = run(["wsl.exe", "--list", "--verbose"], check=False)
    details = (wsl_res.stdout + "\n" + wsl_res.stderr).strip()
    if wsl_res.returncode != 0:
        return TaskResult(
            ok=False,
            summary="WSL not available (wsl --list --verbose failed)",
            details=details,
        )

    text = details.lower()
    has_ubuntu = "ubuntu" in text
    if not has_ubuntu:
        return TaskResult(
            ok=False,
            summary="Ubuntu distro not found",
            details=wsl_res.stdout.strip(),
        )

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
        # Use a robust WSL command targeting the Ubuntu distro explicitly.
        p["commandline"] = "wsl.exe -d Ubuntu"
        updated = True
        break

    if not updated:
        # Create a new Ubuntu profile wired to the Ubuntu WSL distro.
        profiles.append(
            {
                "name": "Ubuntu",
                "source": "Windows.Terminal.Wsl",
                "startingDirectory": "~",
                "commandline": "wsl.exe -d Ubuntu",
            }
        )

    try:
        settings_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except Exception as e:  # noqa: BLE001
        return TaskResult(
            ok=False, summary="write Windows Terminal settings: failed", details=str(e)
        )

    return TaskResult(
        ok=True, summary="Windows Terminal: ensured Ubuntu profile for installed distro"
    )


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
