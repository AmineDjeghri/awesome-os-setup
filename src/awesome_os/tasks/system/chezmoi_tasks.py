from __future__ import annotations

import os
import platform
import shutil
from pathlib import Path

from awesome_os.tasks.commands import run
from awesome_os.tasks.managers.ubuntu_apt import UbuntuAptManager
from awesome_os.tasks.managers.ubuntu_snap import UbuntuSnapManager
from awesome_os.tasks.task import TaskResult


def _run_chezmoi(argv: list[str]) -> TaskResult:
    if shutil.which("chezmoi") is None:
        return TaskResult(ok=False, summary="chezmoi not found on PATH")

    try:
        res = run(["chezmoi", *argv], check=False)
    except Exception as e:  # noqa: BLE001
        return TaskResult(ok=False, summary=f"chezmoi {' '.join(argv)}: failed", details=str(e))

    details = (res.stdout + "\n" + res.stderr).strip()
    if res.returncode == 0:
        return TaskResult(ok=True, summary=f"chezmoi {' '.join(argv)}: ok", details=details)
    return TaskResult(ok=False, summary=f"chezmoi {' '.join(argv)}: failed", details=details)


def _chezmoi_is_initialized() -> bool:
    if shutil.which("chezmoi") is None:
        return False
    res = run(["chezmoi", "source-path"], check=False)
    return res.returncode == 0 and bool((res.stdout or "").strip())


def _detect_repo_origin_url() -> str:
    res = run(["git", "config", "--get", "remote.origin.url"], check=False)
    url = (res.stdout or "").strip()
    return url


def chezmoi_init() -> TaskResult:
    if _chezmoi_is_initialized():
        return TaskResult(ok=True, summary="chezmoi already initialized")

    if shutil.which("git") is None:
        return TaskResult(ok=False, summary="git not found on PATH (required for chezmoi init)")

    url = _detect_repo_origin_url()
    if not url:
        return TaskResult(
            ok=False,
            summary="Could not detect git remote origin URL",
            details="Run manually: chezmoi init <your-dotfiles-repo>",
        )

    return _run_chezmoi(["init", url])


def chezmoi_diff() -> TaskResult:
    return _run_chezmoi(["diff"])


def chezmoi_apply() -> TaskResult:
    return _run_chezmoi(["apply"])


def chezmoi_update() -> TaskResult:
    return _run_chezmoi(["update"])


def install_chezmoi() -> TaskResult:
    if shutil.which("chezmoi") is not None:
        return TaskResult(ok=True, summary="chezmoi already installed")

    system = platform.system().lower()
    if system == "linux":
        if shutil.which("snap") is None:
            return TaskResult(ok=False, summary="snap not found; cannot install chezmoi")
        pm = UbuntuSnapManager()
        res = pm.install("chezmoi")
        return TaskResult(ok=res.ok, summary=res.summary, details=res.details)

    if system == "darwin":
        if shutil.which("brew") is None:
            return TaskResult(ok=False, summary="brew not found; cannot install chezmoi")
        res = run(["brew", "install", "chezmoi"], check=False)
        details = (res.stdout + "\n" + res.stderr).strip()
        if res.returncode == 0:
            return TaskResult(ok=True, summary="installed chezmoi (brew)", details=details)
        return TaskResult(ok=False, summary="install chezmoi (brew): failed", details=details)

    return TaskResult(ok=False, summary=f"Unsupported OS for chezmoi install: {system}")


def setup_zsh_p10k() -> TaskResult:
    system = platform.system().lower()

    if system == "linux":
        pm = UbuntuAptManager()
        actions: list[str] = []
        for pkg in ("zsh", "git", "curl"):
            if pm.is_installed(pkg):
                actions.append(f"already installed: {pkg}")
                continue
            r = pm.install(pkg)
            actions.append(r.summary)
            if not r.ok:
                return TaskResult(
                    ok=False,
                    summary="setup zsh/p10k prerequisites: failed",
                    details="\n".join(actions),
                )
    elif system == "darwin":
        if shutil.which("brew") is None:
            return TaskResult(ok=False, summary="brew not found; cannot install zsh/git/curl")
        res = run(["brew", "install", "zsh", "git", "curl"], check=False, capture_output=False)
        if res.returncode != 0:
            return TaskResult(ok=False, summary="brew install zsh/git/curl: failed")
    else:
        return TaskResult(ok=False, summary=f"Unsupported OS for Zsh setup: {system}")

    if shutil.which("git") is None:
        return TaskResult(
            ok=False, summary="git not found on PATH (required to install zsh plugins)"
        )

    home = Path.home()
    omz_dir = home / ".oh-my-zsh"
    zsh_custom = Path(os.environ.get("ZSH_CUSTOM", str(omz_dir / "custom")))

    actions: list[str] = []

    if not omz_dir.exists():
        res = run(
            ["git", "clone", "--depth=1", "https://github.com/ohmyzsh/ohmyzsh.git", str(omz_dir)],
            check=False,
        )
        if res.returncode != 0:
            details = (res.stdout + "\n" + res.stderr).strip()
            return TaskResult(ok=False, summary="clone oh-my-zsh: failed", details=details)
        actions.append("installed oh-my-zsh")
    else:
        actions.append("oh-my-zsh already installed")

    (zsh_custom / "themes").mkdir(parents=True, exist_ok=True)
    (zsh_custom / "plugins").mkdir(parents=True, exist_ok=True)

    repos: list[tuple[str, Path]] = [
        (
            "https://github.com/romkatv/powerlevel10k.git",
            zsh_custom / "themes" / "powerlevel10k",
        ),
        (
            "https://github.com/marlonrichert/zsh-autocomplete.git",
            zsh_custom / "plugins" / "zsh-autocomplete",
        ),
        (
            "https://github.com/zsh-users/zsh-autosuggestions.git",
            zsh_custom / "plugins" / "zsh-autosuggestions",
        ),
        (
            "https://github.com/zsh-users/zsh-syntax-highlighting.git",
            zsh_custom / "plugins" / "zsh-syntax-highlighting",
        ),
        (
            "https://github.com/unixorn/fzf-zsh-plugin.git",
            zsh_custom / "plugins" / "fzf-zsh-plugin",
        ),
    ]

    for url, dest in repos:
        if dest.exists():
            actions.append(f"exists: {dest.name}")
            continue
        res = run(["git", "clone", "--depth=1", url, str(dest)], check=False)
        if res.returncode != 0:
            details = (res.stdout + "\n" + res.stderr).strip()
            return TaskResult(ok=False, summary=f"clone {dest.name}: failed", details=details)
        actions.append(f"installed: {dest.name}")

    return TaskResult(ok=True, summary="zsh/p10k setup: ok", details="\n".join(actions))


def configure_dotfiles() -> TaskResult:
    steps: list[tuple[str, callable[[], TaskResult]]] = [
        ("install chezmoi", install_chezmoi),
        ("setup zsh/p10k", setup_zsh_p10k),
        ("chezmoi init", chezmoi_init),
        ("chezmoi apply", chezmoi_apply),
    ]

    details_lines: list[str] = []
    for name, fn in steps:
        res = fn()
        details_lines.append(f"{name}: {res.summary}")
        if res.details:
            details_lines.append(res.details)
        if not res.ok:
            return TaskResult(
                ok=False,
                summary="dotfiles config: failed",
                details="\n".join(details_lines).strip(),
            )

    return TaskResult(
        ok=True, summary="dotfiles config: ok", details="\n".join(details_lines).strip()
    )
