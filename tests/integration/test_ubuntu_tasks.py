"""Integration tests for Ubuntu task functions.

These tests run on a real Ubuntu 24.04 system (GitHub Actions runner or local).

Run with: make test-integration
"""

from __future__ import annotations

import platform

import pytest

# Skip the entire module if not running on Linux
pytestmark = pytest.mark.skipif(
    platform.system().lower() != "linux",
    reason="Integration tests require a Linux system",
)


class TestAptManager:
    """Integration tests for UbuntuAptManager on a real Ubuntu system."""

    def test_is_installed_known_package(self):
        """Dpkg should report 'bash' as installed on any Ubuntu runner."""
        from awesome_os.tasks.managers.ubuntu_apt import UbuntuAptManager

        assert UbuntuAptManager().is_installed("bash") is True

    def test_is_installed_nonexistent_package(self):
        """Dpkg should report a clearly fake package as not installed."""
        from awesome_os.tasks.managers.ubuntu_apt import UbuntuAptManager

        assert UbuntuAptManager().is_installed("this-package-does-not-exist-xyz") is False

    def test_update_succeeds(self):
        """Apt update should succeed on the GitHub Actions runner (passwordless sudo)."""
        from awesome_os.tasks.managers.ubuntu_apt import UbuntuAptManager

        result = UbuntuAptManager().update()
        assert result.ok is True, f"apt update failed: {result.summary}\n{result.details}"

    def test_upgrade_succeeds(self):
        """Apt upgrade should succeed on the GitHub Actions runner."""
        from awesome_os.tasks.managers.ubuntu_apt import UbuntuAptManager

        result = UbuntuAptManager().upgrade()
        assert result.ok is True, f"apt upgrade failed: {result.summary}\n{result.details}"

    def test_cleanup_succeeds(self):
        """Apt cleanup (autoremove) should succeed on the GitHub Actions runner."""
        from awesome_os.tasks.managers.ubuntu_apt import UbuntuAptManager

        result = UbuntuAptManager().cleanup()
        assert result.ok is True, f"apt cleanup failed: {result.summary}\n{result.details}"

    def test_install_and_check_curl(self):
        """Installing curl via apt should succeed and be detectable via is_installed()."""
        from awesome_os.tasks.managers.ubuntu_apt import UbuntuAptManager

        mgr = UbuntuAptManager()
        result = mgr.install("curl")
        assert result.ok is True, f"apt install curl failed: {result.summary}\n{result.details}"
        assert mgr.is_installed("curl") is True


class TestDetectOS:
    """Integration tests for OS detection helpers."""

    def test_detect_os_returns_linux_ubuntu(self):
        """detect_os() should return family='linux', distro='ubuntu' on the Ubuntu runner."""
        from awesome_os.detect_os import detect_os

        info = detect_os()
        assert info.family == "linux"
        assert info.distro == "ubuntu"

    def test_is_wsl_false_on_native_runner(self):
        """GitHub Actions native Ubuntu runners are not WSL."""
        from awesome_os.detect_os import _is_wsl

        assert _is_wsl() is False


class TestNvidiaTasks:
    """Integration tests for NVIDIA/CUDA tasks on Ubuntu (no GPU on CI runner)."""

    def test_setup_nvidia_ubuntu_returns_task_result(self):
        """setup_nvidia_ubuntu() must return a TaskResult without crashing on a GPU-less runner."""
        from awesome_os.tasks.system.nvidia_tasks import setup_nvidia_ubuntu
        from awesome_os.tasks.task import TaskResult

        result = setup_nvidia_ubuntu()
        assert isinstance(result, TaskResult)
        assert isinstance(result.ok, bool)

    def test_setup_cuda_returns_task_result(self):
        """setup_cuda() must return a TaskResult without crashing."""
        from awesome_os.tasks.system.nvidia_tasks import setup_cuda
        from awesome_os.tasks.task import TaskResult

        result = setup_cuda()
        assert isinstance(result, TaskResult)
        assert isinstance(result.ok, bool)


class TestPackagesConfig:
    """Integration tests for packages.yaml loading on Ubuntu."""

    def _ubuntu_packages(self):
        from awesome_os.detect_os import PackageCatalog, iter_packages
        from importlib import resources
        import yaml

        pkg = resources.files("awesome_os")
        data = yaml.safe_load((pkg / "config" / "packages.yaml").read_text(encoding="utf-8")) or {}
        catalog = PackageCatalog(data=data)
        return list(iter_packages(catalog.for_distro("ubuntu")))

    def test_ubuntu_packages_load(self):
        """iter_packages() should yield at least one Ubuntu package without error."""
        assert len(self._ubuntu_packages()) > 0

    def test_ubuntu_apt_packages_present(self):
        """At least one apt package should be defined for Ubuntu."""
        apt_packages = [p for p in self._ubuntu_packages() if p.manager == "apt"]
        assert len(apt_packages) > 0

    def test_build_packages_for_os(self):
        """build_packages_for_os() should detect Ubuntu and return a non-empty package list."""
        from awesome_os.detect_os import build_packages_for_os

        system, distro, info, packages = build_packages_for_os()
        assert system == "linux"
        assert distro == "ubuntu"
        assert len(packages) > 0
