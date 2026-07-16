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

You can also check and click on the temps in the top bar (noctalia) to seee detailed things about your pc (cpu temp, gpu name, system information without going to the settings)
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

## Screnshot & annotation tools (CTRL + print) check my hyprland config
sudo pacman -S grim slurp satty wl-clipboard




# Theme Integration

- Dolphin
 If you use Noctalia you can change applications themes directly from noctalia .
Doplhin can be set again to other theems by goign to Dolphin -> Menu bar (3 bars) -> Configure -> Window Color Scheeme -> Breeze Dark.

## qt6ct
``qt6ct``




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

 `sudo pacman -S ddcutil`
`sudo modprobe i2c-dev`
 
Night light (blue light filter).


You can now control some stuff directly in noctalia 


sudo pacman -S breeze-gtk
sudo pacman -S kde-gtk-config
`sudo pacman -S qt5-wayland qt6-wayland`
`sudo pacman -S hyprpolkitagent`
---------------------------------------------------------------------------------------------------



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
