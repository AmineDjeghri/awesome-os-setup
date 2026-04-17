# Linux setup

If you are using a headless server (ubuntu-server for example), prefer to use a client with a GUI and connect to the server via SSH so you can copy-paste the commands and use Awesome-OS with a mouse.

## Installation Process

The Awesome OS Setup provides a **Terminal UI (TUI) application** that guides you through the installation process. Once you run the one-liner installer, you'll see an interactive interface with the following steps:

Use [README.md](../../README.md#linux--wsl2--macos) as it automatically handles the OS setup with the interactive TUI application.

Before installing packages, it's recommended to update your system:
```sh
apt update    # Refresh package lists
apt upgrade   # Upgrade installed packages
apt cleanup   # Remove unused packages
```

### 1. Package Selection
The app displays all available packages from [packages.yaml](../../src/awesome_os/config/packages.yaml) organized by category:
- **Core tools**: `git`, `curl`, `zsh`
- **Terminal tools**: `bat`, `btop`, `fzf`, `lsd`, `neofetch`
- **Apps**: Code editor, messaging apps, media players, etc.

You can multi-select packages using the interactive interface.

### 2. Terminal Setup (Zsh + Oh My Zsh + Powerlevel10k)
The app provides buttons to automate the terminal configuration:

- **Install JetBrainsMono Nerd Font**: Required for proper theme rendering
- **Apply ~/.zshrc**: Configures shell aliases and environment variables
- **Apply ~/.p10k.zsh**: Applies Powerlevel10k theme configuration
- **Sync zsh plugins/theme**: Installs Oh My Zsh plugins and themes
- **Set zsh as default shell**: Makes Zsh your default login shell

**Python Management**: The zshrc configuration replaces both `python3` and `python` with the alias `uv run python`, ensuring you always use the `uv` package manager for Python execution instead of the system Python.

**.env Detection**: The configuration automatically detects and loads `.env` files from your project directories, making environment variables available in your shell session without manual setup.

See the [zshrc configuration file](../../src/awesome_os/config/unix/.zshrc) for the default configuration used by this project.

If you need to revert changes:
- Uninstall Oh My Zsh and Powerlevel10k files
- Uninstall Zsh package
- Reset Bash as default shell

Additional system configuration options (only if you have NVIDIA GPU):
- **Detect NVIDIA**: Check if NVIDIA GPU is available
- **Setup NVIDIA (WSL)**: Configure NVIDIA drivers for WSL2
- **Detect CUDA**: Check CUDA installation
- **Setup CUDA (Advanced)**: Configure CUDA for GPU computing
