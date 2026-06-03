"""Settings and logging configuration for awesome-os-setup."""

from __future__ import annotations

import sys
from typing import Optional

from loguru import logger as _loguru_logger
from pydantic import Field, AliasChoices
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseEnvironmentSettings(BaseSettings):
    """Base settings for environment configuration."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class ApplicationSettings(BaseEnvironmentSettings):
    """Configuration for awesome-os-setup.

    Values are read from environment variables and optionally
    overridden by a ``.env`` file.
    """

    # --- Runtime ---
    logging_level: str = Field(
        default="DEBUG",
        validation_alias=AliasChoices("LOGGING_LEVEL", "logging_level"),
        description="Log level (TRACE, DEBUG, INFO, WARNING, ERROR, CRITICAL)",
    )

    # Example of a model validator
    # @model_validator(mode="after")
    # def set_os_environ(self) -> Self:
    #     """Sync environment variables after settings load."""
    #     os.environ["DEV_MODE"] = str(self.DEV_MODE)
    #     return self


# Cached singleton
_cached_settings: Optional[ApplicationSettings] = None


def get_cached_settings() -> ApplicationSettings:
    """Return the cached settings.

    On the first call the settings are loaded from env / .env.
    Subsequent calls return the same instance.
    """
    global _cached_settings
    if _cached_settings is None:
        _cached_settings = ApplicationSettings()
    return _cached_settings


_logger_initialized: bool = False


def get_logger():
    """Return a loguru logger bound to the app namespace.

    Log level is controlled by LOGGING_LEVEL setting.
    """
    global _logger_initialized
    if not _logger_initialized:
        _cfg = get_cached_settings()
        level = _cfg.logging_level

        # Remove the default loguru sink (ID 0) to prevent a duplicate when we add our logger.
        try:
            _loguru_logger.remove(0)
        except ValueError:
            pass  # already removed

        _loguru_logger.add(
            sys.stderr,
            level=level,
            filter=lambda record: record["extra"].get("name") == "awesome-os",
        )

        _logger_initialized = True

    return _loguru_logger.bind(name="awesome-os")
