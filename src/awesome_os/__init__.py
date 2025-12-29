# Initialize settings and configure logging
import sys

from awesome_os.env_settings import Settings

from loguru import logger as loguru_logger


def initialize():
    settings = Settings()
    loguru_logger.remove()

    if settings.DEV_MODE:
        loguru_logger.add(sys.stderr, level="TRACE")
    else:
        loguru_logger.add(sys.stderr, level="INFO")

    return settings, loguru_logger


settings, logger = initialize()


def hello():
    logger.info("Hello World")


# Get version from pyproject.toml
from importlib.metadata import version

__version__ = version("awesome-os-setup")
