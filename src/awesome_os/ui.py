from __future__ import annotations

from importlib import resources

import TermTk as ttk

from awesome_os import logger

from awesome_os.installers.factory import get_installer
from awesome_os.os_detect import detect_os
from awesome_os.packages import PackageRef, iter_packages, load_catalog_from_text


def _add_log_line(text_edit: ttk.TTkTextEdit, line: str) -> None:
    text_edit.append(line + "\n")


def _read_packages_yaml() -> str:
    pkg = resources.files("awesome_os")
    return (pkg / "config" / "packages.yaml").read_text(encoding="utf-8")


def _build_packages_for_os() -> tuple[str, list[PackageRef]]:
    os_info = detect_os()
    distro = os_info.distro
    catalog = load_catalog_from_text(_read_packages_yaml())
    distro_block = catalog.for_distro(distro)
    packages = list(iter_packages(distro_block))
    return distro, packages


def run_app() -> None:
    distro, packages = _build_packages_for_os()

    root = ttk.TTk()
    win = ttk.TTkWindow(
        parent=root,
        title="Awesome OS Setup",
        size=(100, 30),
        border=True,
        layout=ttk.TTkVBoxLayout(),
    )

    header = ttk.TTkFrame(parent=win, layout=ttk.TTkHBoxLayout())
    ttk.TTkLabel(
        parent=header,
        text=f"Detected distro: {distro}",
        color=ttk.TTkColor.fg("#00ff00"),
        maxHeight=2,
    )

    body = ttk.TTkFrame(parent=win, layout=ttk.TTkHBoxLayout())

    left = ttk.TTkFrame(parent=body, title="Packages", layout=ttk.TTkVBoxLayout())
    right = ttk.TTkFrame(parent=body, title="Log", layout=ttk.TTkVBoxLayout())

    log = ttk.TTkTextEdit(parent=right, readOnly=True)
    right.layout().addWidget(log)  # type: ignore[call-arg]

    def ui_log(message: str) -> None:
        _add_log_line(log, message)
        logger.debug(message)

    if distro == "arch":
        ui_log("Arch support: coming soon")
    if distro == "unknown":
        ui_log("Unsupported OS")

    checks: list[tuple[PackageRef, ttk.TTkCheckbox]] = []

    by_cat: dict[str, list[PackageRef]] = {}
    for p in packages:
        by_cat.setdefault(p.category, []).append(p)

    for cat in sorted(by_cat.keys()):
        ttk.TTkLabel(parent=left, text=f"[{cat}]", color=ttk.TTkColor.fg("#ffaa00"))
        for p in sorted(by_cat[cat], key=lambda x: x.name):
            cb = ttk.TTkCheckbox(text=f"{p.name} ({p.manager})")
            left.layout().addWidget(cb)  # type: ignore[call-arg]
            checks.append((p, cb))

    def do_install_selected() -> None:
        selected = [p for (p, cb) in checks if cb.isChecked()]
        if not selected:
            ui_log("No packages selected")
            return

        for p in selected:
            installer = get_installer(distro=distro, manager=p.manager)
            if installer is None:
                ui_log(f"No installer available for {p.manager} on {distro} (coming soon)")
                continue

            if installer.is_installed(p.name):
                ui_log(f"{p.name}: already installed")
                continue

            res = installer.install(p.name)
            ui_log(res.summary)
            if res.details:
                ui_log(res.details)

    buttons = ttk.TTkFrame(parent=left, layout=ttk.TTkHBoxLayout())
    install_btn = ttk.TTkButton(parent=buttons, text="Install selected")
    install_btn.clicked.connect(do_install_selected)

    try:
        root.mainloop()
    finally:
        pass
