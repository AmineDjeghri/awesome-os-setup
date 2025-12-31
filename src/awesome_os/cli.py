from __future__ import annotations

from pathlib import Path

from awesome_os import logger
from awesome_os.frontend.main import run_app


def main() -> None:
    if not Path.cwd().name == "awesome-os-setup":
        logger.warning(
            "You are launching the UI from a directory that does not look like the repo root. "
            "For the intended workflow, run it from the repo root (or use install.sh / make)."
        )
    run_app()
