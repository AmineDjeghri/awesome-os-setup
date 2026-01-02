"""Arch Linux `yay` package manager backend.

This backend supports Arch and Arch-based distros by:
- bootstrapping `yay` if missing (requires non-interactive sudo)
- installing packages via `yay -S --needed --noconfirm`
"""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

from awesome_os import logger
from awesome_os.tasks.commands import join_argv, run
from awesome_os.tasks.managers.base import InstallResult
from awesome_os.tasks.task import TaskResult


def _sudo_non_interactive_ok() -> bool:
    """Return True if `sudo -n` is usable (no password prompt)."""
    res = run(["sudo", "-n", "true"], check=False)
    return res.returncode == 0


def _format_failed(argv: list[str], stdout: str, stderr: str) -> str:
    details = [f"$ {join_argv(argv)}"]
    if stdout.strip():
        details.append(stdout.strip())
    if stderr.strip():
        details.append(stderr.strip())
    return "\n".join(details).strip()


class ArchYayManager:
    """`yay` manager for Arch Linux and Arch-based distros."""

    name = "yay"

    def _yay(self) -> str | None:
        return shutil.which("yay")

    def _ensure_yay(self) -> TaskResult:
        yay = self._yay()
        if yay is not None:
            return TaskResult(ok=True, summary="yay: found")

        if not _sudo_non_interactive_ok():
            return TaskResult(
                ok=False,
                summary="yay: missing (sudo password required)",
                details=(
                    "This app runs non-interactively; it cannot prompt for your sudo password.\n"
                    "Install yay manually, then re-run:\n"
                    "  sudo pacman -Sy --needed base-devel git\n"
                    "  cd /tmp && git clone https://aur.archlinux.org/yay.git\n"
                    "  cd yay && makepkg -si\n"
                ),
            )

        # Ensure build tooling exists.
        res = run(
            ["sudo", "-n", "pacman", "-Sy", "--needed", "--noconfirm", "base-devel", "git"],
            check=False,
        )
        if res.returncode != 0:
            return TaskResult(
                ok=False,
                summary="yay: bootstrap failed (pacman deps)",
                details=_format_failed(res.argv, res.stdout, res.stderr),
            )

        # Build and install yay from AUR.
        with tempfile.TemporaryDirectory(prefix="awesome-os-yay-") as td:
            tdir = Path(td)
            clone = run(
                ["git", "clone", "https://aur.archlinux.org/yay.git", str(tdir / "yay")],
                check=False,
            )
            if clone.returncode != 0:
                return TaskResult(
                    ok=False,
                    summary="yay: bootstrap failed (git clone)",
                    details=_format_failed(clone.argv, clone.stdout, clone.stderr),
                )

            yay_dir = tdir / "yay"
            # Note: `makepkg -si` will install the built package via pacman (sudo).
            makepkg = run(
                ["bash", "-lc", f"cd {str(yay_dir)!r} && makepkg -si --noconfirm"],
                check=False,
                capture_output=True,
                text=True,
            )
            if makepkg.returncode != 0:
                return TaskResult(
                    ok=False,
                    summary="yay: bootstrap failed (makepkg)",
                    details=_format_failed(makepkg.argv, makepkg.stdout, makepkg.stderr),
                )

        yay = self._yay()
        if yay is None:
            return TaskResult(
                ok=False,
                summary="yay: bootstrap finished but yay not on PATH",
                details="`yay` was built/installed but is still not found on PATH. Restart your shell and try again.",
            )
        return TaskResult(ok=True, summary="yay: installed")

    def is_installed(self, package: str) -> bool:
        # Both repo and AUR packages end up in pacman's local DB.
        pacman = shutil.which("pacman")
        if pacman is None:
            return False
        res = run([pacman, "-Q", package], check=False)
        return res.returncode == 0

    def install(self, package: str) -> InstallResult:
        ensure = self._ensure_yay()
        if not ensure.ok:
            return InstallResult(ok=False, summary=f"{package}: install failed (yay missing)", details=ensure.details)

        yay = self._yay()
        if yay is None:
            return InstallResult(ok=False, summary="yay not found on PATH", details="Ensure `yay` is installed.")

        logger.info(f"Installing {package} via yay...")
        res = run([yay, "-S", "--needed", "--noconfirm", package], check=False)
        if res.returncode == 0:
            return InstallResult(ok=True, summary=f"{package}: installed (yay)")
        return InstallResult(
            ok=False,
            summary=f"{package}: install failed (yay)",
            details=_format_failed(res.argv, res.stdout, res.stderr),
        )

    def update(self) -> TaskResult:
        ensure = self._ensure_yay()
        if not ensure.ok:
            return TaskResult(ok=False, summary="yay update: failed", details=ensure.details)
        yay = self._yay()
        if yay is None:
            return TaskResult(ok=False, summary="yay update: failed", details="yay not found on PATH")
        res = run([yay, "-Sy", "--noconfirm"], check=False)
        if res.returncode == 0:
            return TaskResult(ok=True, summary="yay sync: done")
        return TaskResult(ok=False, summary="yay sync: failed", details=_format_failed(res.argv, res.stdout, res.stderr))

    def upgrade(self) -> TaskResult:
        ensure = self._ensure_yay()
        if not ensure.ok:
            return TaskResult(ok=False, summary="yay upgrade: failed", details=ensure.details)
        yay = self._yay()
        if yay is None:
            return TaskResult(ok=False, summary="yay upgrade: failed", details="yay not found on PATH")
        res = run([yay, "-Syu", "--noconfirm"], check=False)
        if res.returncode == 0:
            return TaskResult(ok=True, summary="yay -Syu: done")
        return TaskResult(ok=False, summary="yay -Syu: failed", details=_format_failed(res.argv, res.stdout, res.stderr))

    def cleanup(self) -> TaskResult:
        ensure = self._ensure_yay()
        if not ensure.ok:
            return TaskResult(ok=False, summary="yay cleanup: failed", details=ensure.details)
        yay = self._yay()
        if yay is None:
            return TaskResult(ok=False, summary="yay cleanup: failed", details="yay not found on PATH")
        # `-Sc` removes unused packages from cache. `--noconfirm` to avoid prompts.
        res = run([yay, "-Sc", "--noconfirm"], check=False)
        if res.returncode == 0:
            return TaskResult(ok=True, summary="yay cache cleanup: done")
        return TaskResult(ok=False, summary="yay cache cleanup: failed", details=_format_failed(res.argv, res.stdout, res.stderr))

