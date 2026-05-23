"""Unit tests for settings.py — get_cached_settings() and get_logger()."""

from __future__ import annotations

import pytest


def _reset_settings_module():
    """Reset the module-level singletons so each test starts clean."""
    import awesome_os.settings as s

    s._cached_settings = None
    s._logger_initialized = False


@pytest.fixture(autouse=True)
def reset_singletons():
    _reset_settings_module()
    yield
    _reset_settings_module()


class TestGetCachedSettings:
    """Tests for the get_cached_settings() singleton factory."""

    def test_is_singleton(self):
        """Repeated calls must return the exact same instance."""
        from awesome_os.settings import get_cached_settings

        s1 = get_cached_settings()
        s2 = get_cached_settings()
        assert s1 is s2

    def test_dev_mode_defaults_to_false(self):
        """DEV_MODE should be False when not set in the environment."""
        from awesome_os.settings import get_cached_settings

        settings = get_cached_settings()
        assert settings.DEV_MODE is False

    def test_dev_mode_from_env(self, monkeypatch):
        """DEV_MODE should be True when the env var is set."""
        monkeypatch.setenv("DEV_MODE", "true")
        from awesome_os.settings import get_cached_settings

        settings = get_cached_settings()
        assert settings.DEV_MODE is True


class TestGetLogger:
    """Tests for the get_logger() singleton factory."""

    def test_is_singleton(self):
        """Repeated calls must return the exact same logger instance."""
        from awesome_os.settings import get_logger

        l1 = get_logger()
        l2 = get_logger()
        assert l1 is l2
