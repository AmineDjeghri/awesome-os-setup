import platform

import TermTk as ttk


def detect_os():
    system = platform.system().lower()
    if "darwin" in system:
        return "darwin"
    elif "linux" in system:
        return "ubuntu"  # Assuming Ubuntu for now
    return "unknown"


def menu(parent, root):  # # Create a frame for the menu
    def show_app_selection(root):
        app_win = ttk.TTkWindow(parent=root, title="Select Apps", size=(40, 15), border=True)
        app_layout = ttk.TTkVBoxLayout()
        app_win.setLayout(app_layout)

        app_list = ["App 1", "App 2", "App 3", "App 4"]
        checkboxes = []
        for app in app_list:
            checkbox = ttk.TTkCheckbox(text=app)
            app_layout.addWidget(checkbox)
            checkboxes.append(checkbox)

        close_btn = ttk.TTkButton(text="Close")
        close_btn.clicked.connect(lambda: app_win.close())
        app_layout.addWidget(close_btn)

        root.addWidget(app_win)  # Ensure the window is added to the root
        app_win.raiseWidget()  # Bring the window to the top

    menu_frame = ttk.TTkFrame(parent=parent, title="Menu")

    menu_layout = ttk.TTkVBoxLayout()
    menu_frame.setLayout(menu_layout)

    install_apps_btn = ttk.TTkButton(text="1 - Install Apps")
    install_apps_btn.clicked.connect(lambda: show_app_selection(root))
    menu_layout.addWidget(install_apps_btn)

    menu_layout.addWidget(ttk.TTkButton(text=""))  # Add space between buttons

    load_dotfiles_btn = ttk.TTkButton(text="2 - Load Dotfiles")
    menu_layout.addWidget(load_dotfiles_btn)


def main():
    root = ttk.TTk()
    win = ttk.TTkWindow(
        parent=root, title="Selection Menu", size=(80, 18), border=True, layout=ttk.TTkVBoxLayout()
    )

    title = """
┌────────────────────────────────────────────────────────────┐
│░█▀█░█░█░█▀▀░█▀▀░█▀█░█▄█░█▀▀░░░█▀█░█▀▀░░░█▀▀░█▀▀░▀█▀░█░█░█▀█│
│░█▀█░█▄█░█▀▀░▀▀█░█░█░█░█░█▀▀░░░█░█░▀▀█░░░▀▀█░█▀▀░░█░░█░█░█▀▀│
│░▀░▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░▀▀▀░▀▀▀░░░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░░│
└────────────────────────────────────────────────────────────┘
    """
    ttk.TTkLabel(parent=win, text=title, alignment=ttk.TTkK.CENTER_ALIGN)

    # sub-frame
    sub_frame = ttk.TTkFrame(parent=win, layout=ttk.TTkHBoxLayout())
    ttk.TTkLabel(
        parent=sub_frame,
        text=f"Detected OS: \n {detect_os().upper()} " f"\nplatform : \n{platform.platform()}",
        color=ttk.TTkColor.fg("#00ff00"),
        alignment=ttk.TTkK.CENTER_ALIGN,
    )

    menu(parent=sub_frame, root=root)

    root.mainloop()


if __name__ == "__main__":
    main()
