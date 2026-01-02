# Initialize settings and configure logging
from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

from awesome_os.env_settings import Settings

from loguru import logger as loguru_logger


LOG_FILE_PATH: Path | None = None


def initialize():
    settings = Settings()
    loguru_logger.remove()

    # Console sink: keep it readable.
    loguru_logger.add(sys.stderr, level="TRACE" if settings.DEV_MODE else "INFO")

    # File sink: always capture verbose logs so we can debug installs after the fact.
    global LOG_FILE_PATH
    try:
        logs_dir = Path.cwd() / ".logs"
        logs_dir.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        LOG_FILE_PATH = logs_dir / f"awesome-os_{ts}.log"
        loguru_logger.add(
            str(LOG_FILE_PATH),
            level="TRACE" if settings.DEV_MODE else "DEBUG",
            enqueue=True,
            backtrace=True,
            diagnose=True,
        )
    except Exception as e:  # noqa: BLE001
        # If we can't write logs, don't prevent the app from starting.
        LOG_FILE_PATH = None
        loguru_logger.warning(f"Failed to initialize file logging: {e}")

    return settings, loguru_logger


settings, logger = initialize()


def hello():
    logger.info("Hello World")


# Get version from pyproject.toml
from importlib.metadata import version

__version__ = version("awesome-os-setup")
