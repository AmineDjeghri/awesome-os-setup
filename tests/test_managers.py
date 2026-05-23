"""Unit tests for package manager backends."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDarwinBrewManager:
    """Tests for the macOS Homebrew package manager backend."""

    def test_install_brew_not_found(self):
        """install() should return ok=False when brew is not on PATH."""
        from awesome_os.tasks.managers.darwin_brew import DarwinBrewManager

        with patch("shutil.which", return_value=None):
            mgr = DarwinBrewManager()
            result = mgr.install("wget")
        assert result.ok is False
        assert "brew not found" in result.summary

    def test_install_success(self):
        """install() should return ok=True when brew exits with returncode 0."""
        from awesome_os.tasks.managers.darwin_brew import DarwinBrewManager

        mock_result = MagicMock(returncode=0, stdout="", stderr="")
        with (
            patch("shutil.which", return_value="/opt/homebrew/bin/brew"),
            patch("awesome_os.tasks.managers.darwin_brew.run", return_value=mock_result),
        ):
            mgr = DarwinBrewManager()
            result = mgr.install("wget")
        assert result.ok is True

    def test_install_failure(self):
        """install() should return ok=False when brew exits with a non-zero code."""
        from awesome_os.tasks.managers.darwin_brew import DarwinBrewManager

        mock_result = MagicMock(returncode=1, stdout="err", stderr="not found")
        with (
            patch("shutil.which", return_value="/opt/homebrew/bin/brew"),
            patch("awesome_os.tasks.managers.darwin_brew.run", return_value=mock_result),
        ):
            mgr = DarwinBrewManager()
            result = mgr.install("wget")
        assert result.ok is False

    def test_is_installed(self):
        """is_installed() should reflect the returncode of the brew list command."""
        from awesome_os.tasks.managers.darwin_brew import DarwinBrewManager

        with (
            patch("shutil.which", return_value="/opt/homebrew/bin/brew"),
            patch(
                "awesome_os.tasks.managers.darwin_brew.run", return_value=MagicMock(returncode=0)
            ),
        ):
            assert DarwinBrewManager().is_installed("wget") is True
        with (
            patch("shutil.which", return_value="/opt/homebrew/bin/brew"),
            patch(
                "awesome_os.tasks.managers.darwin_brew.run", return_value=MagicMock(returncode=1)
            ),
        ):
            assert DarwinBrewManager().is_installed("wget") is False


class TestUbuntuAptManager:
    """Tests for the Ubuntu apt-get package manager backend."""

    def test_install_no_sudo(self):
        """install() should fail immediately when sudo is not available."""
        from awesome_os.tasks.managers.ubuntu_apt import UbuntuAptManager

        with patch(
            "awesome_os.tasks.managers.ubuntu_apt.sudo_non_interactive_ok", return_value=False
        ):
            mgr = UbuntuAptManager()
            result = mgr.install("curl")
        assert result.ok is False
        assert "sudo" in result.summary.lower()

    def test_install_success(self):
        """install() should return ok=True when apt-get exits with returncode 0."""
        from awesome_os.tasks.managers.ubuntu_apt import UbuntuAptManager

        mock_result = MagicMock(returncode=0, stdout="", stderr="")
        with (
            patch(
                "awesome_os.tasks.managers.ubuntu_apt.sudo_non_interactive_ok", return_value=True
            ),
            patch("awesome_os.tasks.managers.ubuntu_apt.run", return_value=mock_result),
        ):
            mgr = UbuntuAptManager()
            result = mgr.install("curl")
        assert result.ok is True

    def test_is_installed(self):
        """is_installed() should return True when dpkg shows 'install ok installed' status."""
        from awesome_os.tasks.managers.ubuntu_apt import UbuntuAptManager

        mock_result = MagicMock(returncode=0, stdout="Status: install ok installed\n")
        with patch("awesome_os.tasks.managers.ubuntu_apt.run", return_value=mock_result):
            assert UbuntuAptManager().is_installed("curl") is True


class TestWebInstallManager:
    """Tests for the web-based (browser-open) install backend."""

    def test_is_installed_always_false(self):
        """is_installed() always returns False — web installs cannot be verified."""
        from awesome_os.tasks.managers.webinstall import WebInstallManager

        assert WebInstallManager().is_installed("https://example.com") is False

    def test_install_opens_browser(self):
        """install() should open the URL in the default browser and return ok=True."""
        from awesome_os.tasks.managers.webinstall import WebInstallManager

        with patch("webbrowser.open") as mock_open:
            result = WebInstallManager().install("https://example.com/download")
        assert result.ok is True
        mock_open.assert_called_once_with("https://example.com/download")
