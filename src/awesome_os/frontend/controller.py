"""TermTk-based interactive frontend.

This module wires together:
- package selection (from the packages catalog)
- system actions (from the tasks factory)
- a background worker thread (JobRunner) to keep the UI responsive
"""

from __future__ import annotations

import shutil
from pathlib import Path

import TermTk as ttk

from awesome_os import logger
from awesome_os.packages import PackageRef
from awesome_os.tasks.factory import SystemAction, get_package_manager

from awesome_os.frontend.dialogs import confirm, prompt_text
from awesome_os.frontend.runner import JobRunner


class AppController:
    """Controller for handling UI events and dispatching background work.

    The controller is responsible for:
    - updating UI state (busy/disabled controls)
    - writing logs to the UI
    - enqueuing long-running work to :class:`~awesome_os.frontend.runner.JobRunner`
    """

    def __init__(
        self,
        *,
        win: ttk.TTkWindow,
        log: ttk.TTkTextEdit,
        distro: str,
        checks: list[tuple[PackageRef, ttk.TTkCheckbox]],
        install_btn: ttk.TTkButton,
        action_buttons: list[ttk.TTkButton],
        runner: JobRunner,
        poll_timer: ttk.TTkTimer,
    ) -> None:
        self._win = win
        self._log = log
        self._distro = distro
        self._checks = checks
        self._install_btn = install_btn
        self._action_buttons = action_buttons
        self._runner = runner
        self._poll_timer = poll_timer
        self._is_busy = False

    def ui_log(self, message: str) -> None:
        """Log to both the UI log panel and the Python logger."""
        self._log.append(message + "\n")
        logger.debug(message)

    def set_busy(self, busy: bool) -> None:
        """Enable/disable actions depending on whether a job is running."""
        self._is_busy = busy
        for btn in self._action_buttons:
            btn.setEnabled(not busy)
        self._install_btn.setEnabled(not busy)

    def on_poll(self) -> None:
        """Drain worker-thread events and re-arm the polling timer."""
        # JobRunner posts UI events from a background thread; we pull them on the UI thread.
        self._runner.drain_events(on_log=self.ui_log, on_busy=self.set_busy)
        self._poll_timer.start(0.1)

    def shutdown(self) -> None:
        """Stop background work and timers."""
        self._runner.stop()
        self._poll_timer.quit()

    def install_selected_clicked(self) -> None:
        """Install all packages whose checkboxes are selected."""
        if self._is_busy:
            self.ui_log("Busy: another task is running")
            return

        selected = [p for (p, cb) in self._checks if cb.isChecked()]
        if not selected:
            self.ui_log("No packages selected")
            return

        def _job() -> None:
            for p in selected:
                pm = get_package_manager(distro=self._distro, manager=p.manager)
                if pm is None:
                    self._runner.ui_events.put(
                        (
                            "log",
                            f"No installer available for {p.manager} on {self._distro} (coming soon)",
                        )
                    )
                    continue

                if pm.is_installed(p.name):
                    self._runner.ui_events.put(("log", f"{p.name}: already installed"))
                    continue

                res = pm.install(p.name)
                self._runner.ui_events.put(("log", res.summary))
                if res.details:
                    self._runner.ui_events.put(("log", res.details))

        self._runner.enqueue("packages: install selected", _job)

    def action_clicked(self, action: SystemAction, section_name: str) -> None:
        """Handle a click on a system action button."""
        if self._is_busy:
            self.ui_log("Busy: another task is running")
            return

        name = f"{section_name}: {action.label}"

        if (
            action.confirm
            and action.backup_target is not None
            and action.backup_default is not None
        ):
            # Some actions mutate a config file; ask for confirmation and offer an optional backup.
            self._confirm_with_optional_backup(action, name)
            return

        if action.confirm:

            def _on_yes() -> None:
                self._enqueue_action(action, name)

            confirm(
                parent=self._win, title="Confirm", text=f"Proceed with: {name}?", on_yes=_on_yes
            )
            return

        self._enqueue_action(action, name)

    def _enqueue_action(self, action: SystemAction, name: str) -> None:
        """Enqueue a system action into the background runner."""

        def _run_action() -> None:
            res = action.run()
            self._runner.ui_events.put(("log", res.summary))
            if res.details:
                self._runner.ui_events.put(("log", res.details))

        self._runner.enqueue(name, _run_action)

    def _confirm_with_optional_backup(self, action: SystemAction, name: str) -> None:
        """Confirm an action, optionally copying a backup of a target file first."""

        def _after_confirm() -> None:
            default_backup = action.backup_default
            prompt_text(
                parent=self._win,
                title="Backup (optional)",
                label="Backup path (leave empty to skip)",
                initial=str(default_backup) if default_backup else "",
                on_ok=_on_backup_path,
            )

        def _on_backup_path(path_text: str) -> None:
            backup_path = Path(path_text).expanduser() if path_text.strip() else None

            def _run_action_with_backup() -> None:
                try:
                    target = action.backup_target
                    if backup_path is not None and target is not None and target.exists():
                        # Ensure parent dirs exist before writing backup.
                        backup_path.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(target, backup_path)
                        self._runner.ui_events.put(("log", f"backup created: {backup_path}"))
                except Exception as e:  # noqa: BLE001
                    self._runner.ui_events.put(("log", f"backup: failed ({e})"))

                res = action.run()
                self._runner.ui_events.put(("log", res.summary))
                if res.details:
                    self._runner.ui_events.put(("log", res.details))

            self._runner.enqueue(name, _run_action_with_backup)

        confirm(
            parent=self._win,
            title="Confirm",
            text=f"Overwrite file? Proceed with: {name}?",
            on_yes=_after_confirm,
        )


def _build_package_checkboxes(
    *,
    parent: ttk.TTkFrame,
    packages: list[PackageRef],
) -> list[tuple[PackageRef, ttk.TTkCheckbox]]:
    """Render a categorized list of packages into the left pane."""
    checks: list[tuple[PackageRef, ttk.TTkCheckbox]] = []

    by_cat: dict[str, list[PackageRef]] = {}
    for p in packages:
        by_cat.setdefault(p.category, []).append(p)

    for cat in sorted(by_cat.keys()):
        ttk.TTkLabel(parent=parent, text=f"[{cat}]", color=ttk.TTkColor.fg("#ffaa00"), maxHeight=1)
        for p in sorted(by_cat[cat], key=lambda x: x.name):
            cb = ttk.TTkCheckbox(text=f"{p.name} ({p.manager})")
            parent.layout().addWidget(cb)  # type: ignore[call-arg]
            checks.append((p, cb))

    return checks
