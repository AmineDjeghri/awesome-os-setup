from __future__ import annotations

import subprocess
from typing import Iterable, Sequence

from pydantic import BaseModel, ConfigDict


class CommandResult(BaseModel):
    model_config = ConfigDict(frozen=True)

    argv: list[str]
    returncode: int
    stdout: str
    stderr: str


def run(
    argv: Sequence[str],
    *,
    check: bool = False,
    capture_output: bool = True,
    text: bool = True,
) -> CommandResult:
    completed = subprocess.run(
        list(argv),
        check=False,
        capture_output=capture_output,
        text=text,
    )
    if check and completed.returncode != 0:
        raise subprocess.CalledProcessError(
            completed.returncode, list(argv), output=completed.stdout, stderr=completed.stderr
        )
    return CommandResult(
        argv=list(argv),
        returncode=completed.returncode,
        stdout=completed.stdout or "",
        stderr=completed.stderr or "",
    )


def join_argv(argv: Iterable[str]) -> str:
    return " ".join(str(a) for a in argv)
