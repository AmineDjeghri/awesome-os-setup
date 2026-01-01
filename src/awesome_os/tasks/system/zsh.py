from __future__ import annotations

import json
import os
import platform
import re
import shutil
from importlib import resources
from pathlib import Path

from awesome_os.tasks.system.git import _git_clone
from awesome_os.tasks.commands import run
from awesome_os.tasks.task import TaskResult


def _read_packaged_text_config(filename: str) -> str:
    pkg = resources.files("awesome_os")
    return (pkg / "config" / filename).read_text(encoding="utf-8")


def apply_zshrc_force() -> TaskResult:
    dest = Path.home() / ".zshrc"
    try:
        content = _read_packaged_text_config(".zshrc")
        dest.write_text(content, encoding="utf-8")
    except Exception as e:  # noqa: BLE001
        return TaskResult(ok=False, summary="write ~/.zshrc: failed", details=str(e))
    return TaskResult(ok=True, summary="wrote ~/.zshrc")


def apply_p10k_force() -> TaskResult:
    dest = Path.home() / ".p10k.zsh"
    try:
        content = _read_packaged_text_config(".p10k.zsh")
        dest.write_text(content, encoding="utf-8")
    except Exception as e:  # noqa: BLE001
        return TaskResult(ok=False, summary="write ~/.p10k.zsh: failed", details=str(e))
    return TaskResult(ok=True, summary="wrote ~/.p10k.zsh")


def uninstall_oh_my_zsh_and_p10k() -> TaskResult:
    home = Path.home()
    candidates = [
        home / ".oh-my-zsh",
        home / ".p10k.zsh",
        home / ".zshrc",
        home / ".fzf.zsh",
        home / ".zsh_history",
    ]

    actions: list[str] = []
    try:
        for p in candidates:
            if not p.exists():
                actions.append(f"skip: {p} (not found)")
                continue

            if p.is_dir():
                shutil.rmtree(p)
                actions.append(f"removed dir: {p}")
            else:
                p.unlink()
                actions.append(f"removed file: {p}")
    except Exception as e:  # noqa: BLE001
        return TaskResult(ok=False, summary="uninstall zsh config: failed", details=str(e))

    return TaskResult(
        ok=True,
        summary="uninstalled: oh-my-zsh + p10k files",
        details="\n".join(actions).strip(),
    )


def uninstall_zsh_apt() -> TaskResult:
    system = platform.system().lower()
    if system != "linux":
        return TaskResult(ok=False, summary=f"Unsupported OS for uninstalling zsh: {system}")

    # First, attempt to switch the user's default shell back to bash.
    # This mirrors the shell script behavior and reduces the chance of locking the user out.
    res_shell = set_bash_as_default_shell()
    actions: list[str] = [res_shell.summary]
    if res_shell.details:
        actions.append(res_shell.details)

    apt_get = shutil.which("apt-get")
    if apt_get is None:
        return TaskResult(
            ok=False,
            summary="apt-get not found",
            details="This action currently supports Debian/Ubuntu-like systems.",
        )

    cmd = ["sudo", "-n", apt_get, "remove", "-y", "zsh"]
    res = run(cmd, check=False)
    details = (res.stdout + "\n" + res.stderr).strip()
    actions.append(f"ran: {' '.join(cmd)}")
    if details:
        actions.append(details)

    if res.returncode == 0:
        actions.append(
            "Please restart your terminal to complete the uninstallation. "
            "If there is an error to access WSL, run in PowerShell: wsl ~ -e bash"
        )
        return TaskResult(
            ok=True, summary="zsh uninstalled (apt)", details="\n".join(actions).strip()
        )

    if "a password is required" in details.lower() or "sudo:" in details.lower():
        actions.append(
            "sudo needs a password. Run manually in a terminal:\nsudo apt-get remove -y zsh"
        )
        return TaskResult(
            ok=False,
            summary="zsh uninstall requires sudo password",
            details="\n".join(actions).strip(),
        )

    return TaskResult(
        ok=False, summary="failed to uninstall zsh (apt)", details="\n".join(actions).strip()
    )


def _parse_plugins_from_zshrc(zshrc_text: str) -> list[str]:
    m = re.search(r"plugins=\((.*?)\n\s*\)", zshrc_text, flags=re.DOTALL)
    if not m:
        return []
    block = m.group(1)
    plugins: list[str] = []
    for line in block.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        plugins.extend(stripped.split())
    return plugins


def _parse_theme_from_zshrc(zshrc_text: str) -> str | None:
    m = re.search(r'^\s*ZSH_THEME\s*=\s*"([^"]*)"', zshrc_text, flags=re.MULTILINE)
    if not m:
        return None
    raw = (m.group(1) or "").strip()
    if not raw:
        return None
    return raw.split("/", 1)[0]


def sync_zsh_plugins_and_theme() -> TaskResult:
    if shutil.which("git") is None:
        return TaskResult(ok=False, summary="git not found on PATH (required to sync zsh plugins)")

    try:
        user_zshrc = Path.home() / ".zshrc"
        if user_zshrc.exists():
            zshrc_text = user_zshrc.read_text(encoding="utf-8")
        else:
            zshrc_text = _read_packaged_text_config(".zshrc")
    except Exception as e:  # noqa: BLE001
        return TaskResult(ok=False, summary="read config .zshrc: failed", details=str(e))

    try:
        pkg = resources.files("awesome_os")
        raw = (pkg / "config" / "zshrc_external_plugins.json").read_text(encoding="utf-8")
        registry = json.loads(raw)
    except Exception as e:  # noqa: BLE001
        return TaskResult(
            ok=False, summary="read zshrc_external_plugins.json: failed", details=str(e)
        )

    plugins = _parse_plugins_from_zshrc(zshrc_text)
    theme = _parse_theme_from_zshrc(zshrc_text)

    home = Path.home()
    omz_dir = home / ".oh-my-zsh"
    zsh_custom = Path(os.environ.get("ZSH_CUSTOM", str(omz_dir / "custom")))

    actions: list[str] = []

    omz_url = str(registry.get("oh_my_zsh") or "").strip()
    if not omz_url:
        omz_url = "https://github.com/ohmyzsh/ohmyzsh.git"

    if not omz_dir.exists():
        res = _git_clone(url=omz_url, dest=omz_dir)
        actions.append(res.summary)
        if res.details:
            actions.append(res.details)
        if not res.ok:
            return TaskResult(
                ok=False,
                summary="sync zsh plugins/theme: failed",
                details="\n".join(actions).strip(),
            )
    else:
        actions.append("exists: oh-my-zsh")

    (zsh_custom / "themes").mkdir(parents=True, exist_ok=True)
    (zsh_custom / "plugins").mkdir(parents=True, exist_ok=True)

    plugin_urls = registry.get("plugins") if isinstance(registry.get("plugins"), dict) else {}
    theme_urls = registry.get("themes") if isinstance(registry.get("themes"), dict) else {}

    for name in plugins:
        url = (plugin_urls.get(name) if isinstance(plugin_urls, dict) else None) or ""
        url = str(url).strip()
        if not url:
            actions.append(f"skipped: {name} (no url mapping or internal plugin)")
            continue
        dest = zsh_custom / "plugins" / name
        if dest.exists():
            actions.append(f"exists: {name}")
            continue
        res = _git_clone(url=url, dest=dest)
        actions.append(res.summary)
        if res.details:
            actions.append(res.details)
        if not res.ok:
            return TaskResult(
                ok=False,
                summary="sync zsh plugins/theme: failed",
                details="\n".join(actions).strip(),
            )

    if theme:
        url = (theme_urls.get(theme) if isinstance(theme_urls, dict) else None) or ""
        url = str(url).strip()
        if not url:
            actions.append(f"skipped theme: {theme} (no url mapping)")
        else:
            dest = zsh_custom / "themes" / theme
            if dest.exists():
                actions.append(f"exists theme: {theme}")
            else:
                res = _git_clone(url=url, dest=dest)
                actions.append(res.summary)
                if res.details:
                    actions.append(res.details)
                if not res.ok:
                    return TaskResult(
                        ok=False,
                        summary="sync zsh plugins/theme: failed",
                        details="\n".join(actions).strip(),
                    )

    return TaskResult(
        ok=True, summary="sync zsh plugins/theme: ok", details="\n".join(actions).strip()
    )


def set_zsh_as_default_shell() -> TaskResult:
    system = platform.system().lower()
    if system not in {"linux", "darwin"}:
        return TaskResult(ok=False, summary=f"Unsupported OS for setting default shell: {system}")

    zsh_path = shutil.which("zsh")
    if zsh_path is None:
        return TaskResult(ok=False, summary="zsh not found on PATH")

    current_shell = os.environ.get("SHELL", "").strip()
    if current_shell and Path(current_shell).resolve() == Path(zsh_path).resolve():
        return TaskResult(ok=True, summary="zsh is already the default shell")

    chsh_path = shutil.which("chsh")
    if chsh_path is None:
        return TaskResult(
            ok=False,
            summary="chsh not found on PATH",
            details=f"Run manually: chsh -s {zsh_path}",
        )

    res = run([chsh_path, "-s", zsh_path], check=False)
    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(
            ok=True,
            summary="default shell set to zsh",
            details=(
                details
                or "Log out and back in (or restart your terminal) for changes to take effect."
            ),
        )

    hint = f"Run manually: chsh -s {zsh_path}"
    if details:
        hint = hint + "\n" + details
    return TaskResult(ok=False, summary="failed to set default shell to zsh", details=hint)


def set_bash_as_default_shell() -> TaskResult:
    system = platform.system().lower()
    if system not in {"linux", "darwin"}:
        return TaskResult(ok=False, summary=f"Unsupported OS for setting default shell: {system}")

    bash_path = shutil.which("bash")
    if bash_path is None:
        return TaskResult(ok=False, summary="bash not found on PATH")

    current_shell = os.environ.get("SHELL", "").strip()
    if current_shell and Path(current_shell).resolve() == Path(bash_path).resolve():
        return TaskResult(ok=True, summary="bash is already the default shell")

    chsh_path = shutil.which("chsh")
    if chsh_path is None:
        return TaskResult(
            ok=False,
            summary="chsh not found on PATH",
            details=f"Run manually: chsh -s {bash_path}",
        )

    res = run([chsh_path, "-s", bash_path], check=False)
    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(
            ok=True,
            summary="default shell set to bash",
            details=(
                details
                or "Log out and back in (or restart your terminal) for changes to take effect."
            ),
        )

    hint = f"Run manually: chsh -s {bash_path}"
    if details:
        hint = hint + "\n" + details
    return TaskResult(ok=False, summary="failed to set default shell to bash", details=hint)
