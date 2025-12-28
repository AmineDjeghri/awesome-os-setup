"""Installer interfaces and result models.

This module defines the minimal contract that all installers in
`awesome_os.installers` must follow.

Installers are thin backends around a system package manager (e.g. `apt`). They
are responsible for:

- Checking whether a package is already installed (`is_installed`).
- Installing a package (`install`).

They do not own any UI concerns. All logging should go through
`awesome_os.logger`.
"""

from __future__ import annotations

from typing import Protocol

from pydantic import BaseModel, ConfigDict


class InstallResult(BaseModel):
    """Represents the outcome of a single installation attempt.

    Attributes:
        ok: Whether the installation completed successfully.
        summary: Short, user-facing message describing the outcome.
        details: Optional diagnostic information (stdout/stderr, error context).
    """

    model_config = ConfigDict(frozen=True)

    ok: bool
    summary: str
    details: str = ""


class Installer(Protocol):
    """Protocol for a package installer backend.

    Concrete installers typically wrap one package manager (apt, brew, winget,
    etc.) and should be written to be as idempotent as possible.

    Attributes:
        name: A short identifier for the backend (e.g. `"apt"`).
    """

    name: str

    def is_installed(self, package: str) -> bool: ...

    def install(self, package: str) -> InstallResult: ...
