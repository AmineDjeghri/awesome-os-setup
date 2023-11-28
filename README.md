# Awesome-Windows11-WSL-Linux
![windows desktop terminal](resources/windows-desktop-terminal_1.png)
![WSL terminal](resources/wsl_terminal.jpg)

## Content of repository
- If you are a linux/WSL user, you can jump direclty to the dedicated section for Unix-based systems, tested on Ubuntu 22.04: [unix_workflow/0_linux_setup.md](unix_workflow/0_linux_setup.md).
- If you are a windows user, this repository encompasses
   - Valuable tips for enhancing your Windows user experience, with a focus on creating a productive environment incorporating WSL 2 (Linux).
   - WSL setup & Linux guides & automated scripts [unix_workflow/0_linux_setup.md](unix_workflow/0_linux_setup.md) to automate the installation of essential components like terminal utilities, Conda, GPU drivers, and more.
   - No need for dualboot anymore, and includes SSH, SFTP with UI (Pycharm/FileZilla).

## Why this repositoy
#### Why Windows mixed with Linux(WSL) ? Linux users, please read till the end and don't be mad 😅
**macOS:**
- (+) Excellent for coding and video editing. Supports Adobe & Office products.
- (-) Limited gaming capabilities compared to Windows & Linux.

**Linux:**
- (+) Ideal for coding and gaming, providing good performance in both areas.
- (-) Lacks support for Adobe & Office products and certain software.

**Windows with WSL:**
- (+) Seamless compatibility with diverse software, including Adobe & Office products.
- (+) Optimal choice for gaming enthusiasts.
- (+) Well-suited for coding with Windows Subsystem for Linux (WSL) and no need for dual boot.
- (-) UI is not smooth and responsive compared to macOS & Linux 

Within the domain of development, Unix-based systems such as Linux and MacOS frequently garner attention. Nevertheless, the integration of WSL allows smooth coding alongside the utilization of Adobe and Microsoft products that may lack support on Linux. This flexibility, coupled with the ability to handle resource-intensive games beyond MacOS capabilities, positions Windows-WSL as an enticing platform, ensuring a well-rounded computing experience for all users, regardless of their workplace constraints.

Based on your needs, you can choose your OS.

## Table of Contents
1. [Content of repository](#--content-of-repository)
2. [Why this repository](#--why-this-repository)
3. [Windows Configuration](#1--windows-configuration)
4. [Utility Softwares](#2-utility-softwares)
5. [Dev Workflow](#3--dev-workflow)
   - [Dev Software](#31-dev-software)
   - [Coding using WSL/Linux](#32-coding-using-linuxwsl-inside-windows)
   - [Linux/WSL Setup, Miniconda, CUDA & More](#33-linuxwsl-setup-miniconda-cuda--more)
   - [WSL2 Tips & Tricks](#34-wsl2-tips--tricks-)
6. [UI/UX Customization](#4--ux-custommization)
7. [Awesome Piracy](#awesome-piracy)


## 1- Windows configuration

- First thing to do is to connect your windows to your microsoft account : Windows-> account -> connect
### 1.1 Save your key to you microsoft account (important) & update some parameters
 - Connect windows with your Microsoft/Outlook account to save and link the key to your account
 - Activate localization on windows (if you want to localize your device)
 - Activate bitlocker to encrypt your data (Exists only on windows pro, education and entreprise edition)
 - When placing an external monitor that runs 144hz, make sure to activate the `144Hz` in display settings
 - If you're using OneDrive, becareful when you sync your Desktop and windows specific folders, you can face some problems. My advice is to avoid syncing windows default folders (like Desktop, Documents). Unsyc everything (Desktop, Documents...) Just use OneDrive as a cloud store like Google Drive. If you don't use it, you can uninstall it.
 - (Optionnal) sleep mode with or without screen lock [here](https://consumer.huawei.com/en/support/content/en-us15592807/#:~:text=Click%20the%20Windows%20icon%20and,Screen%20and%20Sleep%20to%20Never)
 - (Desktop) if you have a 3200mhz RAM and it runs bellow this frequency, activate XMP profile in the BIOS
 - (Audio devices) if you have bluetooth and audio devices, you can sort them in audio settings -> use as default for both audio & communications
 - (Audio) Deactivate lowering communication sounds in advanced audio settings.

### 1.2 Want to move to a new computer ? transfer your windows key
When you reset your computer it will usual either recognize the device and apply the key, if not you can connect to the Microsoft account where you saved your key,
If you didn't save the key in your account, you need to do this before resetting your old computer
- On your old PC, check if the key is not an OEM by running  `Slmgr /dli`
- Get your licence key (if you fogot the serial number use a software like :
- Deactivate it in windows terminal by using administrator mode with `slmgr /cpky`
- Activate it on the new computer using `slmgr /ipk xxxxx-xxxxx-xxxxx-xxxxx-xxxxx`

## 2-Utility Software
- <ins>Browser</ins>: Brave or Edge or Firefox, Don't forget to change your sync settings to import your passwords, bookmarks...ect.
- <ins>Privacy extensions</ins> : if you care about your data and privacy (even if you use windows lol) you can limit websites to collect your data:  ClearURLs, Fast Forward, Cookie Auto Delete, HTTPS Everywhere, Decentralayes, Ugly Email (Privacy badge , but tends to block facebook api login in some websites)
- <ins>Browser extensions</ins> : uBlock Origin, Checker Plus for Gmail, Free Download Manager, Google translate, Google Dictionnary, colorZilla, Reddit enhacement Suite, Pocket, Enhacer for Youtube, Augmented Steam, Read Aloud,  pocket.
- <ins>ChatGPT extensions</ins>; Suite ChatGPT, ChatGPT sidebar,
- <ins>Agenda & Mail</ins> : Google agenda, Gmail, -> create an app shortcut with brave, it will act like an app in windows, and activate the notifications. Make BRave the default apps in windows for mailto and agenda then go to brave://settings/handlers and add gmailand agenda .
- <ins> Desktop notifications from gmail </ins>: [Link](https://chrome.google.com/webstore/detail/checker-plus-for-gmail/oeopbcgkkoapgobdbedcemjljbihmemj)
- <ins> Desktop notifications from Google calendar</ins> : [Link](https://chrome.google.com/webstore/detail/checker-plus-for-google-c/hkhggnncdpfibdhinjiegagmopldibha)
- <ins>Antivirus</ins> : Windows defender or Kaspersky Cloud free
- <ins>Powershell 7</ins> : Install Powershell 7  [link](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?WT.mc_id=THOMASMAURER-blog-thmaure&view=powershell-7.3&viewFallbackFrom=powershell-7). Change the default terminal in Windows Terminal, and activate the "run always as administrator in the default profile"
- <ins>Customization</ins>: PowerToys from microsoft store (very cool and useful features)
- <ins>Others</ins>: CCleaner, HWInfo (portable)
- <ins>Adobe</ins> : Photoshop, illustrator, premiere pro, XD
- <ins>Free photoshop alt </ins> :  [link](https://www.photopea.com/)
- <ins>VPN</ins> : ProtonVPN or NordVPN
- <ins>Torrent client</ins>: qBitTorrent
- <ins>Download Manager</ins>: [NeatDownloadManager](https://www.neatdownloadmanager.com/index.php/en/) + extension specially for videos + subtitles
- <ins>Google Drive</ins> :  download it on windows and put the files and folder that you want to be automatically saved on your drive, you won't need to everytime open google drive in your browser and manually put your files there
- <ins>Online Storage</ins> : Google Drive (15gb), Mega Drive (50GB) ...ect. Use these Drives to store non personanal Data ! It's better to have an NAS or an external HDD to store your personal data.
- <ins>Microsoft Office 2021</ins> Buy it or buy a retail key for 1$.

- <ins>PDF editing</ins> Adobe acrobat(paied) or Sejda(free)(3 free tasks per hour) : https://www.sejda.com/ (do not download the desktop app)
- <ins>Windows Terminal </ins> Windows terminal works in every directory, right lick in any directory and you can have a bash with that path
- <ins> Teracopy </ins>
- <ins> Notion </ins>
- <ins> AnyDesk</ins> (portable + enable password)
- <ins> Audio </ins> : ear trumpet
- <ins> Nvidia Driver </ins> : Geforce Experience (no need for cuda if you code using WSL)

### Screen recorder :
- ShareX : screen capturing and GIF recording (portable), use CTRL + print screen key
- Integrated Screen recording of windows :  press `windows key + G`
- Screen Recording/ Streaming : OBS or Streamlabs

### Browser websites
- <ins>Netflix, Prime</ins>: Windows store and browser. Browser is better in terms of stability, lists, content and vpn use. On the other hand, Netfliw from the store app and Netfliw on Edge browser  can handle 7.1 and 4k streaming. To add windows apps downloaded from windows store in the taskbar or the desktop :Press Windows key + R then enter shell:appsfolder then drag and drop .
- Configure some websites on your desktop and taskbar as shortcuts (Netflix, Google calendar, Gmail...ect)
- <ins> Gmail and Google Calendar</ins> : you can configure dark mode ("Thèmes" , , choose "dark/sombre") and priority notifications (all new emails), signature.

## 3- Dev workflow
### 3.1 Dev software
#### <ins>PyCharm or VScode or NeoVim</ins>:
- I prefer to use PyCharm (Pro version is free for students)
- BECAREFUL when creating a project, you should use the anaconda env (windows/WSL) and not installing a new python interpreter or using virtualenv
- Sync pycharm settings : https://www.jetbrains.com/help/pycharm/sharing-your-ide-settings.html#IDE_settings_sync
- [pycharm settings, tips & tricks](https://github.com/AmineDjeghri/Awesome-Windows11-WSL/blob/master/Pycharm_WSL_Anaconda.md)

#### <ins>Docker Desktop</ins> specially with WSL : you can start, stop, delete containers easily,  edit file right inside the app without the need of a terminal.
#### <ins>Sublime Text</ins> (Free):
- Extremely lightweight (low resource usage), but still keeps around some of the more advanced features you would expect out of a top text editor.
- Install it before installing git bash (a software that adds linux and git commands to windows).
- (recommanded) CheatSheet
- (optionnal) Run from CLI: go to  `System Properties -> Advanced System Settings -> Advanced -> Environment Variables -> System variable -> path` and add `C:\Program Files\Sublime Text` to the PATH environment variable to make it accessible from the terminal. Close the windows terminal and open a new one and run this command `subl`, it should open Sublime Text.
#### <ins>Windows Terminal</ins>
- Always use Windows terminal/powershell instead of linux
- You can update to powershell 7 : Install it from Microsoft store. Close and then re-open your terminal window, Put powershell 7 as default.

#### other tools
- <ins>ssh key</ins> : (requires gitbash) you can generate an ssh key with `ssh-keygen -t rsa` (when prompted, enter an empty password if you want, key name can stay the same)
Open file your_home_directory/.ssh/id_rsa.pub (example `C:\Users\AmineDjeghri\.ssh` with your favorite text editor to see the key.
- <ins>Pycharm Jupyter Notebook</ins> : Use the one provided in Pycharm. It provides better autocomplete.
- <ins>Free Cloud GPU </ins> Google Colab/Kaggle you can either put your git repositories inside google drive to use them in colab, or   git clone inside colab.
- <ins>Filezilla</ins> : for SFTP (work with private key: add it in edit/connection/sftp or use pageant)
- Git emojis: https://gitmoji.dev/
- Latex Handwriting recognition: https://detexify.kirelabs.org/classify.html
- Turn math equations and snipping to latex code: https://mathpix.com/
- Overleaf: https://www.overleaf.com/
- wget on Windows terminal : add it to your terminal: https://www.programmersought.com/article/90723524682/
- [jupyter autocmplete](https://github.com/krassowski/jupyterlab-lsp#installation)


### 3.2 Coding using Linux(WSL) inside Windows
Lot of libraries and codes are made for Linux. Hence, using WSL is the best choice. Do not code in both OS, use for example pycharm or vscode on windows with a conda environement installed on WSL. The best thing is to combine the power of Windows with WSL.

The most amazing thing about windows latest version is WSL (WSL2.0 exactly). You can run Linux in Windows.
It is fantastic. Virtualization overhead is not noticeable, full integration between guest and host os's, you can run binaries compiled for MS Windows from linux. Full development toolchain is available as WSLessentialy is linux VM in second incarnation. It supports snapshots and is portable. This made windows useful.
- You can install packages directly in Ubuntu
- You can easily navigate and communicate between ubuntu and windows as Ubuntu acts like a disk drive.
- You can install conda environment in ubuntu, use GPU, use pycharm on windows to connect to WSL conda env and more.


#### Install WSL:
 - Install WSL ``` wsl --install ```
 - Restart you computer
 - When installing WSL, it comes with Ubuntu (you can always install other distibutions from the microsoft store)
 - You have different options to run Ubuntu :
      - From windows search bar (and select ubuntu or WSL for the default distro)
      - Running `ubuntu`  inside Windows terminal
      - Running `wsl` inside Windows terminal to run the default distro
      - Running Windows terminal and choosing ubuntu in the terminal tab section.
      - If it's not there, make sure you have correctly installed WSL by searching wsl in your windows search bar & running it.
- If you have Nvidia GPU & the nvidia driver is installed on Windows, you can run `nvidia-smi` in Linux. No need to install the nvidia Driver again in Linux.
 - Add systemd to wsl.conf if it's not there: run `sudo vim /etc/wsl.conf` then paste the following code:
 ```
[boot]
systemd=true
 ```
 - Restart the terminal and run `systemctl list-unit-files --type=service` in WSL to see some processes running.
 - If you have an ssh key in windows, copy it to linux `home/.ssh` folder and use on the ssh file of linux : `chmod 600 ~/.ssh/id_rsa` and `chmod 600 ~/.ssh/id_rsa.pub`. If you don't have an SSH key, generate a new SSH key using : `ssh-keygen -t rsa` inside linux.

### 3.3 Linux/WSL Setup, Miniconda, CUDA & More:
- [Linux Setup Guide](unix_workflow/0_linux_setup.md) : contains an automated script & a tutorial to install the main elements I use in Linux/WSL.
- [Cuda & Pytorch installation inside conda](unix_workflow/1_cuda_pytorch_install.md)
- [Pycharm settings, tips & tricks](unix_workflow/2_pycharm_wsl_conda.md)
- [Python package example](unix_workflow/package_example)

### 3.4 WSL2 Tips & Tricks :
- Find WSL path : `\\wsl$\Ubuntu\home` or `\\wsl$\Ubuntu`  then ping it in Windows Explorer's sidebar.
- You can use `wslpath` command to convert a windows path to wsl path : `wslpath  'C:\Users\AmineDjeghri\Desktop\git\myproject'`
- Copy your ssh key from windows to linux and use on the ssh file of linux : `chmod 600 ~/.ssh/id_rsa` and `chmod 600 ~/.ssh/id_rsa.pub`
- Update packages:  `sudo apt update` then `sudo apt upgrade`
- Disk usage: `df -h` look on the right column 'Mounted on'
- wsl disk usage : `df -h /mnt/wslg/distro`
- Unzip: `sudo apt install unzip`
- Reclaim disk space :
   - it requires docker Dashboard for WSL2, and activating 2 hyper V params in Control Panel.
   -  Install this https://superuser.com/a/1307442/769637 install the Hyper-V Platform | Hyper-V Services part, too + restart)
   - in Administrator Mode : `wsl --shutdown` then `cd 'C:\Users\Amine Djeghri\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\LocalState'` then `optimize-vhd -Path .\ext4.vhdx -Mode full`
   - for more information check this : these https://askubuntu.com/a/1380274 + https://github.com/microsoft/WSL/issues/4699 +
- To change the default distro or fix the `wsl` command to start your distro from powershell not working you can do:
```sh
wsl --list
wsl --setdefault <name_of_your_distro>
```
#### configure WSL terminal :
 - You can enter ubuntu with different ways: clicking on Shortcut (Orange), or running 'wsl' in windows terminal, or running 'ubuntu' in windows terminal, or selecting the right profile in the tab in windows terminal.
 - To open Ubuntu terminal from current location : go to windows terminal ->  parameters -> profiles -> ubuntu -> command line (under name) and change it to `ubuntu run`.
 - Now, go to desktop and right click to open a windows terminal, run 'wsl', you should see that ubuntu started from the current location.
 - (pycharm) Use WSL/ubuntu as the default terminal in pycharm: `settings -> tools -> terminal`  and put in shell path: `ubuntu run`
 - (pycharm) Add WSL conda interpreter in Pycharm (add interpreter -> WSL -> conda) and select the global conda : `/home/amine/miniconda3/bin/conda`. Then click on load environments and it will automatically detect all the conda envs.

#### backup and restore
You can export wsl image after finishing all the steps to save it in case you move to a new computer :
   - wsl --terminate ubuntu
   - wsl --shutdown
   - wsl --export Ubuntu E:\ubuntu.tar
   - [source 1](https://www.xda-developers.com/how-back-up-restore-wsl/)

#### uninstall WSL:
Uninstall all distributions & WSL from the control panel & open Windows Features, then turn on (check) Windows Subsystem for Linux. Restart your computer.

# 4- UX Customization
## 4.1 customize Linux/WSL terminal
Follow this tutorial [customize linuxwsl terminal](unix_workflow/0_linux_setup.md) which includes an automated script to install the main elements I use in Linux/WSL.

## 4.2 customize Windows terminal
- # TODO

## 4.3 Customize your windows UI:
![windows desktop](resources/windows-desktop.png)
- Show Files extensions : If you don’t see file name extensions when you view files in File Explorer: In the search box on the taskbar, type file explorer, and in the search results, select File Explorer. In File Explorer under View, in the Show/hide group, select the File name extensions check box.
- Install rainmeter
- Install https://github.com/mpurses/Sonder/releases
- Download this wallpaper https://raw.githubusercontent.com/mpurses/Sonder/master/Skins/Sonder/Wallpapers/Trees-22.jpg
- O&O ShutUp 10 : privacy control windows
- DS4Windows : make playstation controllers work on PC : https://github.com/Ryochan7/DS4Windows/releases
- Bing wallpaper: https://www.microsoft.com/en-us/bing/bing-wallpaper?SilentAuth=1&wa=wsignin1.0
- Pin some folders and drivers, Recycle Bin in the file explorer. Fast browsing: right click on the file explorer in the taskbar to show the shortcut to the pinned folders.
- Add more Desktop icons (PC, Downloads...): Personalization->themes->desktop icon settings
- WinAero Tweaker : customize the appearance and behavior of the operating system in a flexible way (context menu)
- TaskbarX [link] (https://chrisandriessen.nl/taskbarx), also hide windows taskbar (right click on the taskbar -> taskbar settings-> hide in desktop mode)
- Fences [link] (https://store.steampowered.com/app/607380/Fences/?l=french) doesn't need steam to autostartup
- Hide the Windows taskbar (right click on the taskbar -> taskbar settings). You can and make it centered and transparent with [TaskbarX]([https://chrisandriessen.nl/taskbarx)


#### other customizations:
- You can convert a website to an application , for exemple: Google Agenda/ Netflix in Edge/Brave/Chrome, go to At the top right: More -> More Tools ->  Create shortcut.  , and check window mode, it will run like an app in your windows desktop
( I took the example of mattermost because there is no free Google Agenda app in windows )
- Remove unnecessary programs, unnecessary icons from the start menu and add others like google maps, meteo calendar
- App shortcut : some apps don't provide a desktop shortcut, even if you try to find where they are you can't (like Netflix), they only give you the choice to add them to the start menu or the taskbar . But there is a solution :
             - if an app doesn't want to be added to the desktop like netflix, you can drag it from the start menu to the desktop
             - if it's not on the start up menu, search for it then add it to start menu then drag it to desktop
- Use windows touchpad gestures, it really improves the experience and saves time, for exemple create a desktop and open a windows inside it, then you can create another desktop and put another window in it, after this you can fast switch between the two desktops using your four fingers and swap from the left to right
- Use Quiet Hours and add only the applications that you want them to send you a notification, (Brave will still send you notifications to get BAT but it will never appear ;) )
 - <ins>Deactivate startup programs</ins>:task manager -> startup -> deactivate software that you don't want it to run at startup ( do the same in ccleaner)
 - <ins>Windows partition</ins>: use the windows partition integrated software to create , delete or format partitions
 - You can change your power management options (when windows will be put on sleep, what happens when you close your laptop ..ect), performance vs normal usage.
 - If you consider buying a computer with a GPU for Deep Learning, choose a computer with an NVIDIA GPU that supports CUDA (preferably > RTX 2000 series).

### Wifi & Router 5ghz:
- Deactivate WPS
- Make your wifi invisible
Choose 5ghz over 2.4ghz: if your device is connected to a wifi and it keeps switching between 5ghz and 2.4ghz do the following:
- If it's your wifi: split your WiFi into 2 access points, one for 5Ghz and the other for 2.4Ghz. After that make your PC connect to the 5Ghz one only
- If it's not your wifi (hotel/work wifi) and you have an ethernet port, you can always plug a router( example HONOR ROUTER 3 WIFI 6) and have your own private network. You can split the wifi into 2 access points like i mentionnned it in the section above.

## Awesome Piracy :
https://github.com/Igglybuff/awesome-piracy


## Star History (do not forget to star the repo 😁 )
[![Star History Chart](https://api.star-history.com/svg?repos=aminedjeghri/awesomewindows11&type=Date)](https://star-history.com/#aminedjeghri/awesomewindows11&Date)
