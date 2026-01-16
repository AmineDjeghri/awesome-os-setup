# macOS (Darwin) setup

This document describes how to get a productive macOS setup (terminal + apps + UX tweaks) consistent with the rest of this repo.

**Table of contents**
<!-- TOC -->
* [macOS (Darwin) setup](#macos-darwin-setup)
  * [1. Key goals](#1-key-goals)
  * [2. Prerequisites](#2-prerequisites)
  * [3. Package manager (Homebrew)](#3-package-manager-homebrew)
  * [4. Terminal setup (Zsh + Oh My Zsh + Powerlevel10k)](#4-terminal-setup-zsh--oh-my-zsh--powerlevel10k)
  * [5. Developer tools](#5-developer-tools)
  * [6. Recommended apps](#6-recommended-apps)
    * [6.1. Raycast](#61-raycast)
    * [6.2. AltTab](#62-alttab)
    * [6.3. AeroSpace + JankyBorders](#63-aerospace--jankyborders)
  * [7. UI/UX tweaks](#7-uiux-tweaks)
  * [8. Keyboard layout: macOS vs Windows](#8-keyboard-layout-macos-vs-windows)
  * [9. Notes](#9-notes)
<!-- TOC -->

## 1. Key goals

- Get a modern terminal stack (Zsh + Oh My Zsh + Powerlevel10k + useful CLI tools).
- Install core apps via Homebrew (and brew casks).

## 2. Prerequisites

- macOS 15+ recommended.
- Internet connection.
- Apple ID (optional but useful for the App Store).

All the following apps and commands are available in

## 3. Package manager (Homebrew)

Install Homebrew:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Ensure `brew` is available:

```sh
echo "export PATH=/opt/homebrew/bin:$PATH" >> ~/.zshrc
```

## 4. Terminal setup (Zsh + Oh My Zsh + Powerlevel10k)

Recommended order:

1. Install Oh My Zsh first (it modifies `~/.zshrc`).
2. Install FiraCode Nerd font from [here](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/FiraCode.zip).
3. Install the Powerlevel10k theme.
4. Install CLI tools (`bat`, `btop`, `fastfetch`, `lsd`, ...).

Notes:

- `bat` is the macOS equivalent of Ubuntu’s `batcat`.
- If you set aliases in `~/.zshrc`, keep them small and obvious.

Example:

```sh
echo 'alias cat="bat"' >> ~/.zshrc
```

## 5. Developer tools

- Install Xcode Command Line Tools:

```sh
xcode-select --install
```

- Prefer `uv` over Python's system at `/usr/bin/python3`.

```sh
echo 'alias python="uv run python"' >> ~/.zshrc
```

## 6. Recommended apps

This repo’s `packages.yaml` includes macOS `brew` packages and `cask` apps.

### 6.1. Raycast

- Use Raycast as a “PowerShell equivalent” launcher.
- Replace Spotlight:
  - Remove Spotlight shortcut in macOS keyboard settings.
  - Configure the same shortcut for Raycast.
- Finder is still useful for macOS-specific settings and edge cases.


### 6.2. AltTab

- Brings a Windows-like Alt-Tab experience.
- Useful if you remap keys to be more Windows-like.

### 6.3. AeroSpace + JankyBorders

- AeroSpace: tiling window manager.
  - Tutorial: https://www.youtube.com/watch?v=-FoWClVHG5g
  - Docs: https://nikitabobko.github.io/AeroSpace/
- JankyBorders: adds window borders (requires AeroSpace).

## 7. UI/UX tweaks

- Enable sudo with Touch ID:

```sh
sed -e 's/^#auth/auth/' /etc/pam.d/sudo_local.template | sudo tee /etc/pam.d/sudo_local
```
- Night Shift.
- Auto-hide the dock.
- Remove unused menu bar icons:
  - Hold `command` then drag the icon out of the menu bar (not all apps support it).
- Finder:
  - Show tab bar.
  - Show path bar.
  - Show hidden files: `command + shift + .`

## 8. Keyboard layout: macOS vs Windows
![SCR-20241117-sbna.png](SCR-20241117-sbna.png)
- **Command (⌘)** is the macOS equivalent of **Ctrl** for most shortcuts.
- **Option (⌥)** is similar to **Alt**.
- **Control (⌃)** is often used for secondary actions (e.g. Control+Click is right-click).
- **Delete** behaves like Backspace. Forward delete is `Fn + Delete`.

If you remap keys to make the layout feel closer to Windows, keep the mapping consistent and avoid mixing multiple remap tools.

## 9. Notes

- Some apps do not have import/export settings and require manual configuration (e.g. Ice, AltTab).
- Some apps might need manual installation (e.g. Badgeify).
