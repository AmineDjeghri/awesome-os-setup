"""Public entry point for launching the terminal UI."""

from __future__ import annotations

from pathlib import Path

import TermTk as ttk
from TermTk import TTkString

from awesome_os import logger
from awesome_os.frontend.controller import _build_package_checkboxes, AppController
from awesome_os.frontend.runner import JobRunner
from awesome_os.detect_os import build_packages_for_os
from awesome_os.tasks.factory import get_system_action_sections, SystemAction


def run_app() -> None:
    """Entry point for launching the terminal UI."""
    system, distro, info, packages = build_packages_for_os()
    info = f" info:{info}" if info else ""
    root = ttk.TTk()
    win = ttk.TTkWindow(
        parent=root,
        title="Awesome OS Setup",
        size=(150, 50),
        border=True,
        layout=ttk.TTkVBoxLayout(),
    )

    # header
    header = ttk.TTkFrame(parent=win, layout=ttk.TTkHBoxLayout())
    ttk.TTkLabel(
        parent=header,
        text=f"OS: {system} | Distro: {distro} | {info}",
        color=ttk.TTkColor.fg("#00ff00"),
        maxHeight=2,
    )

    # body
    body = ttk.TTkFrame(parent=win, layout=ttk.TTkHBoxLayout())

    # left
    left = ttk.TTkFrame(
        parent=body, title=TTkString("Packages"), layout=ttk.TTkVBoxLayout(), maxHeight=20
    )
    checks = _build_package_checkboxes(parent=left, packages=packages)

    # right
    right = ttk.TTkFrame(parent=body, title=TTkString("Log"), layout=ttk.TTkVBoxLayout())
    log = ttk.TTkTextEdit(parent=right, readOnly=True)
    right.layout().addWidget(log)  # type: ignore[call-arg]

    # footer
    footer = ttk.TTkFrame(parent=win, layout=ttk.TTkVBoxLayout())

    # Display install button
    install_row = ttk.TTkFrame(parent=footer, layout=ttk.TTkHBoxLayout())
    install_btn = ttk.TTkButton(parent=install_row, text=TTkString("Install selected"))

    action_buttons: list[ttk.TTkButton] = []

    runner = JobRunner()
    runner.start()

    poll_timer = ttk.TTkTimer()

    controller = AppController(
        win=win,
        log=log,
        distro=distro,
        checks=checks,
        install_btn=install_btn,
        action_buttons=action_buttons,
        runner=runner,
        poll_timer=poll_timer,
    )

    install_btn.clicked.connect(controller.install_selected_clicked)

    if distro == "unknown":
        controller.ui_log("Unsupported OS")

    # Display actions buttons
    for section_name, actions in get_system_action_sections(
        system=system, distro=distro, info=info
    ):
        row = ttk.TTkFrame(parent=footer, layout=ttk.TTkHBoxLayout())
        ttk.TTkLabel(parent=row, text=f"{section_name}:", maxWidth=14)
        for action in actions:
            btn = ttk.TTkButton(parent=row, text=TTkString(action.label))
            action_buttons.append(btn)

            def _on_action_clicked(
                *_args: object, _action: SystemAction = action, _section_name: str = section_name
            ) -> None:
                controller.action_clicked(_action, _section_name)

            btn.clicked.connect(_on_action_clicked)

    poll_timer.timeout.connect(controller.on_poll)
    poll_timer.start(0.1)

    try:
        root.mainloop()
    finally:
        controller.shutdown()


def main():
    if not Path.cwd().name == "awesome-os-setup":
        logger.warning(
            "You are launching the UI from a directory that does not look like the repo root. "
            "For the intended workflow, run it from the repo root (or use install.sh / make)."
        )
    run_app()


if __name__ == "__main__":
    main()
