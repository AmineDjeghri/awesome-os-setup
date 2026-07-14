# CachyOS Hyprland Developer Workstation Setup

> Work in Progress
>
> This document tracks my migration from Windows to a native Linux development workstation.
> It will be updated as the setup is tested and refined.

---

# Goal

Replace my Windows workflow with a fully native Linux environment.

## Previous setup

- Windows 11
- WSL
- GlazeWM
- ShareX
- Raycast

## New setup

- CachyOS
- Hyprland (without KDE Plasma desktop)
- Noctalia
- Ghostty
- Vicinae
- KDE applications where useful
- Native Linux gaming
- Native Linux development

---

# Installation

## Secure Boot

Disabled.

Reason:

The CachyOS installer was blocked by Secure Boot.

---

## Bootloader

Selected:

- Limine

Filesystem:

- Btrfs
- LUKS disk encryption

---

# After First Boot

sudo pacman -Syu

Verify NVIDIA drivers.

```bash
nvidia-smi
```

If this shows the GPU information, the NVIDIA driver is working correctly.

---

# Install Applications



Install:

- Helium Browser
- zed
- Ghostty
- Remove Kitty later
- Remove Alacritty later

Copy personal configuration files for:

- Hyprland . https://github.com/AmineDjeghri/awesome-os-setup/blob/main/src/awesome_os/config/unix/hyprland.lua
- Noctalia

in Dolphin . show hidden files

test shortcuts : alt+f for fullscreen for example .
you can also choose theme in noctualia settings -> themes and apply theme . (I don't advice for that), i like to keep my personal themes)

(don't delete qt6 and 5 themes , for now i didn't figure out how to delete noctalia theme without affecting other stuff)

---
Hyprland Plugins (hymission and hyprbars:

sudo pacman -S \
cpio \
cmake \
git \
meson \
gcc \
base-devel

sudo pacman -S nlohmann-json

hyprpm update

hyprpm add https://github.com/gfhdhytghd/hymission

hyprpm enable hymission

Test ALT TAB


hyprpm add https://github.com/hyprwm/hyprland-plugins
hyprpm enable hyprbars
Test drag and drop, and close, maximise windows

hyprpm reload

hyprpm list
You can now use alt-tab
---

sudo pacman -S grim slurp satty wl-clipboard




# KDE Theme Integration

## Problem

KDE applications inside Hyprland look inconsistent.

Examples:

- Dolphin

Reason:

Hyprland is only a window manager.

It does **not** configure Qt themes automatically like KDE Plasma does.

---

## Required Packages

```bash
sudo pacman -S \
breeze \
breeze-icons \
breeze-gtk \
kde-gtk-config \
kde-cli-tools \
qt6ct \

```

### Package explanations

### breeze

The default KDE Qt theme.

Provides:

- window styling
- widgets
- buttons
- menus

**Recommended:** Yes

---

### breeze-icons

Official KDE icon theme.

Without it many KDE apps display incorrect or missing icons.

**Recommended:** Yes

---

### breeze-gtk

Makes GTK applications (Firefox, Chromium, etc.) visually match KDE applications.

**Recommended:** Yes



---
Optional: 

### kde-gtk-config

Allows KDE to configure GTK themes.

Useful if using KDE settings.

**Recommended:** Optional

---

### kcolorpicker

Simple KDE color picker.

Only needed if you actually use it.

**Recommended:** Optional

### kde-cli-tools

Small KDE command-line utilities.

Examples:

- launching System Settings pages
- opening files
- desktop integration

Some KDE apps expect these utilities.

**Recommended:** Yes




### qt6ct

Qt Configuration Tool.

Lets you configure:

- Qt theme
- fonts
- icon theme
- appearance

Run:

```bash
qt6ct
```

**Recommended:** Yes



---

# Qt Configuration

Run:

```bash
qt6ct
```

Configure:

- Breeze theme
- Breeze icons
- Fonts
- Color scheme

This makes Qt applications consistent outside Plasma.

---

# Dolphin "Open With" Fix (My Hyprland configuration already creates this automatically.)

## Problem 
The "Open With" menu is empty.

Reason:

The XDG application menu is missing.

try this only if it is not available:

Install:

```bash
sudo pacman -S archlinux-xdg-menu
```

Create the menu symlink:

```bash
sudo ln -sf \
/etc/xdg/menus/arch-applications.menu \
/etc/xdg/menus/applications.menu
```

My Hyprland configuration already creates this automatically.

No need to repeat it.

---

# Desktop Integration Packages

```bash
sudo pacman -S \
xdg-utils \
xdg-user-dirs \
xdg-user-dirs-gtk \
xdg-desktop-portal \
xdg-desktop-portal-hyprland \
xdg-desktop-portal-kde \
polkit-kde-agent \
kio \
kio-extras \
dolphin
```

## Package explanations

### xdg-utils

Provides standard Linux desktop commands.

Examples:

- open URLs
- open files
- default applications

Very important.

**Required:** Yes

---

### xdg-user-dirs

Creates standard folders.

Examples:

- Documents
- Downloads
- Pictures
- Videos

**Required:** Yes

---

### xdg-user-dirs-gtk

Keeps GTK applications synchronized with user folders.

Optional but recommended.

---

### xdg-desktop-portal

Provides desktop APIs used by modern applications.

Needed for:

- Flatpak
- File picker
- Screensharing
- Sandboxed applications

**Required:** Yes

---

### xdg-desktop-portal-hyprland

Portal backend specifically for Hyprland.

Needed for:

- screen sharing
- screenshots
- Wayland integration

**Required:** Yes

---

### xdg-desktop-portal-kde

Provides KDE-native file picker and dialogs.

Useful if most applications are KDE-based.

Only one portal backend is active for each feature, but having this installed is generally harmless.

**Recommended:** Yes

---

### polkit-kde-agent

Authentication dialog.

Shows password prompts for:

- mounting drives
- installing software
- privileged operations

Without it, many GUI actions silently fail.

**Required:** Yes

---

### kio

KDE's file access framework.

Required by Dolphin.

Supports:

- network shares
- USB
- remote files
- virtual locations

**Required:** Yes

---

### kio-extras

Additional KIO plugins.

Adds support for:

- SMB
- FTP
- SFTP
- MTP (Android)
- many network protocols

Recommended if Dolphin is your main file manager.

---

### dolphin

KDE file manager.

Recommended.

---

# KDE System Settings

Install:

```bash
sudo pacman -S systemsettings
```

Although KDE Plasma is **not** installed, System Settings is extremely useful.

It provides graphical configuration for:

- Fonts
- Icons
- Colors
- Appearance
- Input devices
- Display settings

This replaces editing many configuration files manually.

Recommended.

---

# Utilities

Install:

```bash
sudo pacman -S wdisplays
```

GUI monitor configuration.

---

```bash
sudo pacman -S brightnessctl
```

Brightness control.

---

```bash
sudo pacman -S wlsunset
```

Night light (blue light filter).

---

# Hyprland Plugins

## Hyprspace / Hymission

Requires JSON library:

```bash
sudo pacman -S nlohmann-json
```

Build dependencies:

```bash
sudo pacman -S \
base-devel \
git \
gcc \
cmake \
meson \
cpio
```

### Why these packages?

- **base-devel** – Standard Arch build tools (make, pkgconf, etc.). Essential for compiling AUR packages.
- **git** – Clone source code repositories.
- **gcc** – C/C++ compiler.
- **cmake** – Build system used by many C++ projects.
- **meson** – Modern build system used by some Hyprland projects.
- **cpio** – Archive utility occasionally required during package builds.

In practice, installing **base-devel**, **git**, **cmake**, and **meson** is usually sufficient. `gcc` is included in `base-devel`, and `cpio` is only needed by some build scripts.

---

# Still To Do

- Install Gaming Packages from CachyOS Hello
- Configure Vicinae
- Finish Hyprland plugin setup
- Test desktop integration
- Verify theming consistency
- Remove unnecessary packages after testing



APPs to try: 
- Spectacle: https://apps.kde.org/spectacle/
- KDE connect
- 

sudo pacman -S \
ripgrep \
fd \
fzf \
jq \
tree \
btop \
fastfetch
