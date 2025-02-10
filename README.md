# Awesome OS Setup

![Logo](docs/images/logo.png)

| Windows WSL Terminal                                          | Desktop with terminals                                             |
|---------------------------------------------------------------|--------------------------------------------------------------------|
| ![Windows WSL Terminal](docs/images/windows_wsl_terminal.png) | ![Desktop with terminals](docs/images/desktop_with_terminals.jpeg) |

<div style="text-align: center;">The image you are looking at is a screenshot of a WSL Ubuntu terminal in Windows 11. The top bar is an app called GlazeWM that is a tiling WM that lets you organize windows and adjust their layout on the fly by using keyboard-driven commands.
You can follow this repository to get a similar setup on Windows11, Linux or both.

![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white)
[![Linux](https://img.shields.io/badge/-Linux-grey?style=for-the-badge&logo=linux)](https://www.microsoft.com/en-in/windows)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Windows Terminal](https://img.shields.io/badge/Windows%20Terminal-%234D4D4D.svg?style=for-the-badge&logo=windows-terminal&logoColor=white)
</div>

**Table of contents**
<!-- TOC -->
* [Awesome OS Setup](#awesome-os-setup)
  * [1. Windows 11-WSL2](#1-windows-11-wsl2)
  * [2. Linux WSL2 (Ubuntu)](#2-linux-wsl2-ubuntu)
  * [3. TV setup](#3-tv-setup)
  * [4. Shortcuts_and_apps_setup](#4-shortcuts_and_apps_setup)
  * [5. Awesome Websites & Browser extensions](#5-awesome-websites--browser-extensions)
  * [Contributing](#contributing)
<!-- TOC -->

#todo: add load yaml packages.yaml config (from path or url )

## 1. Windows 11-WSL2

Valuable applications & tips for enhancing your Windows user experience, with a focus on creating a productive
environment incorporating WSL 2 (Linux).

- **My Windows/WSL2 docs**: Read more about it
  here: [windows_workflow_README.](docs/windows_workflow/README_windows.md) / [Website](https://setup.aminedjeghri.com/readme-windows.html)

Get started with one command (run it in PowerShell as administrator):

```powershell
## Run it in powershell as ADMINISTRATOR
iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/AmineDjeghri/awesome-os-setup/main/docs/windows_workflow/setup_windows.ps1'))

```

## 2. Linux WSL2 (Ubuntu)

A set of configurations,
dotfiles and a script to automatically set up a powerful terminal & shell utilities(zsh,fzf, ctrl+f on terminal to
search files & folder...),
themes like Powerlvl10k, Conda, GPU drivers, and more on Linux/WSL2, again automatically.

- **My Linux/WSL2 docs**: Read more about it
  here: [README](docs/unix_workflow/README_unix.md) / [website](https://setup.aminedjeghri.com/readme-unix.html)

Get started with one command (linux):

```bash
sh -c "$(wget https://raw.githubusercontent.com/AmineDjeghri/awesome-os-setup/main/docs/unix_workflow/setup_linux.sh -O -)"
```

## 3. TV setup

- **My TV setup docs**: Read me about it
  here: [README](docs/tv_setup.md) / [website](https://setup.aminedjeghri.com/tv_setup.html)

## 4. Shortcuts_and_apps_setup

- **My Apps setup docs**: Read more about it here:
  [README](docs/apps_configuration_and_shorcuts) / [website](https://setup.aminedjeghri.com/shortcuts_and_apps_setup.html)

## 5. Awesome Websites & Browser extensions

Read more about it here:
[README](docs/awesome_websites_browser_extensions) / [website](https://setup.aminedjeghri.com/awesome-websites.html)

**For Windows users: Why you should use WSL2?**
WSL2 enables users to run Linux applications and use command-line tools natively on their Windows machines.
This integration allows users
to enjoy the familiarity of Windows while simultaneously harnessing the power and flexibility of Linux.
Also, a surprising number of Linux GUI apps can run on WSL. GUI applications are officially supported on WSL2 and
referred to as [WSLg](https://github.com/microsoft/wslg)(No installation required).

|              | macOS                                                                         | Linux                                                                      | Windows with WSL                                                                                                                                                                                                                          |
|--------------|-------------------------------------------------------------------------------|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Advantages   | (+) Excellent for coding and video editing. Supports Adobe & Office products. | (+) Ideal for coding and gaming, providing good performance in both areas. | - (+) Seamless compatibility with diverse software, including Adobe & Office products. </br> (+) Optimal choice for gaming enthusiasts </br> (+) Well-suited for coding with Windows Subsystem for Linux (WSL) and no need for dual boot. |
| Inconvenient | (-) Limited gaming capabilities compared to Windows & Linux.                  | (-) Lacks support for Adobe & Office products and certain software.        | (-) UI is not smooth and responsive compared to macOS & Linux                                                                                                                                                                             |

Within the domain of development, Unix-based systems such as Linux and macOS frequently garner attention. Nevertheless,
the integration of WSL allows smooth coding alongside the utilization of Adobe and Microsoft products that may lack
support on Linux. This flexibility, coupled with the ability to handle resource-intensive games beyond macOS
capabilities, positions Windows-WSL as an enticing platform, ensuring a well-rounded computing experience for all users,
regardless of their workplace constraints.

Based on your needs, you can choose your OS.

## Contributing



**Star History Chart**
[![Star History Chart](https://api.star-history.com/svg?repos=aminedjeghri/awesomewindows11&type=Date)](https://star-history.com/#aminedjeghri/awesomewindows11&Date)
