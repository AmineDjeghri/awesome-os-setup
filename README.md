# BetterWindows11
![windows desktop terminal](https://github.com/AmineDjeghri/BetterWindows/blob/master/windows-desktop-terminal_1.png)

!! Updated for windows 11 !!

Some tips to improve your User experience when using windows
- A guide to help you set up a windows environement to maximum your productivity 
- Spend some hours setting this up (a full guide to configure many things including, linux commands in windows no need for dualboot anymore, SSH, SFTP with interface to reach a maximum level of productivity)

## Summary 
1. [Windows Installation](https://github.com/AmineDjeghri/BetterWindows11#1--windows-configuration)
2. [Utility Softwares : Browsers, extensions, daily and usefull programs](https://github.com/AmineDjeghri/BetterWindows11#2-utility-softwares)
3. [Dev Softwares : All the softwares I recommand for developpement and codin](https://github.com/AmineDjeghri/BetterWindows11#3--dev-softwares)
4. [Pytorch and Cuda](https://github.com/AmineDjeghri/BetterWindows11#4-python-pytorch-and-cuda-installation)
5. [UI/UX Custommization](https://github.com/AmineDjeghri/BetterWindows11#5--ux-custommization)


## 1- Windows configuration
- First thing to do is to connect your windows to your microsoft account : Windows-> account -> connect
### 1.1 Save your key to you microsoft account (important)
 - Connect windows with your Microsoft-Outlook) account to save and link the key to your account 
 - Activate localization on windows (if you want to localize your device)
 - Activate bitlocker to encrypt your data (Exists only on windows pro, education and entreprise edition)
 - When placing an external monitor that runs 144hz, make sure to activate the `144Hz` in display settings
 - (Skip if you are on laptop) if you have a 3200mhz RAM and it runs bellow this frequency, activate XMP profile in the BIOS

### 1.1 New PC ? transfer your windows key
- On your old PC, check if the key is not an OEM by running  `Slmgr /dli`
- Get your licence key (if you fogot the serial number use a software like : 
- deactivate it windows terminal or cmd using administrator mode with `slmgr /cpky`
- activate it on the new computer using `slmgr /ipk xxxxx-xxxxx-xxxxx-xxxxx-xxxxx`

## 2-Utility Softwares
- <ins>Browser</ins>: Brave, Don't forget to change your sync settings to import your passwords...ect.
- <ins>Privacy extensions</ins> : if you care about your data and privacy (even if you use windows lol) you can limit websites to collect your data:  ClearURLs, Fast Forward, Cookie Auto Delete, HTTPS Everywhere, Decentralayes, Ugly Email (Privacy badge , but tends to block facebook api login in some websites)
- <ins>Browser extensions</ins> : uBlock Origin, Checker Plus for Gmail, Free Download Manager, Google translate, Google Dictionnary, colorZilla, Reddit enhacement Suite, Pocket, Enhacer for Youtube, Augmented Steam, Read Aloud,  pocket.
- <ins>Agenda & Mail</ins> : Google agenda, Gmail, -> create an app shortcut with brave, it will act like an app in windows, and activate the notifications. Make BRave the default apps in windows for mailto and agenda then go to brave://settings/handlers and add gmailand agenda .
- <ins>Antivirus</ins> : Kaspersky Cloud free
- <ins>Others</ins>: CCleaner, HWInfo
- <ins>Adobe</ins> : Photoshop, illustrator, premiere pro, XD
- <ins>VPN</ins> : ProtonVPN or NordVPN
- <ins>Torrent client</ins>: qBitTorrent
- <ins>Google Drive</ins> :  download it on windows and put the files and folder that you want to be automatically saved on your drive, you won't need to everytime open google drive in your browser and manually put your files there
- <ins>Online Storage</ins> : Google Drive (15gb), Mega Drive (50GB) ...ect. Use these Drives to store non personanal Data ! It's better to have an NAS or an external HDD to store your personal data.
- <ins>Microsoft Office 2016</ins> Buy it or ... Better than the 365 version.
- <ins>Netflix, Prime</ins>: windows store and browser (browser is better in terms of stability and vpn use, windows store apps can handle 7.1 and 4k streaming). To add windwos apps downloaded from windows store in the taskbar or the desktop :Press Windows key + R then enter shell:appsfolder then drag and drop .
- <ins>Windows Terminal </ins> windows terminal works in every directory, right lick in any directory and you can have a bash with that path 
-  <ins> Teracopy </ins>
### 2.2 Amazing apps & websites:
- Free PDF editing (3 free tasks per hour) : https://www.sejda.com/
- Free Photoshop alternative : https://www.photopea.com/
- Notion 

## 3- Dev workflow
### 3.1 Dev software
#### <ins>Sublime Text</ins> (Free, no need to but the pro lisence): 
- Extremely lightweight (low resource usage), but still keeps around some of the more advanced features you would expect out of a top text editor.
- Install it before installing git bash (a software that adds linux and git commands to windows). 
- (recommanded) CheatSheet
- (optionnal) Run from CLI: go to  `System Properties -> Advanced System Settings -> Advanced -> Environment Variables -> System variable -> path` and add `C:\Program Files\Sublime Text` to the PATH environment variable to make it accessible from the terminal. Close the windows terminal and open a new one and run this command `subl`, it should open Sublime Text.
#### <ins>Git-Bash</ins>:
- You can use linux commands in window like SSH and Git ! Download gitbash to have these commands added to windows Terminal. Open a new Windows terminal after the installation and run this command `git --version` you should see the following message `git version 2.39.1.windows.1`. that means the git command works !
#### <ins>PyCharm or VScode</ins>: 
- I prefer to use PyCharm (Education version which is free) but here are the config for both, BECAREFUL when creating a project, you should use the anaconda python and not another one like virtualenv (that's why you need to make sure to have only the anaconda python installed)
- Sync pycharm settings : https://www.jetbrains.com/help/pycharm/sharing-your-ide-settings.html#IDE_settings_sync
#### other tools
- .ssh key : generate an ssh key with `ssh-keygen -t rsa` (when prompted, enter an empty password if you want, key name can stay the same)
Open file your_home_directory/.ssh/id_rsa.pub (example `C:\Users\AmineDjeghri\.ssh` with your favorite text editor to see the key.
- <ins>Pycharm Jupyter Notebook<ins> : Use the one provided in Pycharm. It provides better autocomplete.
- <ins>Free Cloud GPU </ins> Google Colab you can either put your git repositories inside google drive to use them in colab, or directly import git repo inside colab without google drive 
- powershell 7 : Install it from Microsoft store. Close all the terminals than you have than run again windows terminal. Put powershell as default.
- <ins>SFTP</ins> : Filezilla (work with private key: add it in edit/connection/sftp or use pageant)
- Git emojis: https://gitmoji.dev/ 
- Latex Handwriting recognition: https://detexify.kirelabs.org/classify.html
- Turn math equations and snipping to latex code: https://mathpix.com/
- Overleaf: https://www.overleaf.com/
- wget: add it to your temrinal: https://www.programmersought.com/article/90723524682/


### 3.2 Do you want to use Linux (WSL) inside windows or just use Windows ?
### 3.2.1.Conding using Linux(WSL) inside Windows (1st and best choice)

![WSL terminal](https://github.com/AmineDjeghri/BetterWindows/blob/master/resources/wsl_terminal.png)

The most amazing thing about windows latest version is WSL (WSL2.0 exactly). You can run Linux in Windows. 
It is fantastic. Virtualisation overhead is not noticeable, full integration between guest and host os's, you can run binaries compiled for MS Windows from linux. Full development toolchain is available as WSLessentialy is linux VM in second incarnation. It supports snapshots and is portable. This made windows useful.
- You can install packages directly in UBuntu 
- You can easily navigate and communicate between ubuntu and windows as Ubuntu acts like a disk drive.
- you can install conda environement in ubuntu, use GPU, install pycharm on windows, and use the conda installation in pycharm.
 Give it a try:
 - Install WSL ``` wsl --install ``` 
 - Restart you computer
 - Install Ubuntu from [MS Store](https://apps.microsoft.com/store/detail/ubuntu-on-windows/9NBLGGH4MSV6?hl=fr-fr&gl=fr)
 - Run directly Ubuntu from windows search bar (or windows terminal and choose ubuntu)
-  <ins>Miniconda or Anaconda</ins> (better than installing python alone)

### 3.2.1.Conding using Windows (2nd choice)
#### install conda :
- Download miniconda from [the official website](https://docs.conda.io/en/latest/miniconda.html)
: install it and CHECK add path to environnement variables, make sure to delete every available python version on your system before.
- After the installation of conda, restart your pc.
-Open a 'Anaconda Powershell Prompt'  from Start Menu (not a regular windows terminal). Now Try:
conda init powershell
- Run windows terminal (powershell) always use windows terminal instead of cmd or somethig else)
- you should see '(base)' before any command.
- run `conda env list` to verify if conda has been correctly installed. also run `python` to see if python has been added to the path 




## 4-Python, Pytorch and Cuda installation: 
#### 4.1.1 Pytorch with Nvidia GPU
- Important : Pytorch 1.10.1 works with CUDA 11.3 and visual studio 2019
- Download [VSCode Community 2019](https://docs.microsoft.com/en-us/visualstudio/releases/2019/release-notes).
- Install it and check `Desktop Development with C++` and `.NET` (size will be 11GB approxiamtly) 
- Download and install [CUDA 11.3](https://developer.nvidia.com/cuda-11.3.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local)
- Install [Pytorch 1.10.1](https://pytorch.org/get-started/locally/) by running this command `pip install torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio===0.10.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html`

#### 4.1.2 Pytorch without gpu: 
`pip install torch torchvision torchaudio`

- Check if you succeeded to install pytorch, run the following python code: 

```
import torch
# setting device on GPU if available, else CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)
print()

#Additional Info when using cuda
if device.type == 'cuda':
    print(torch.cuda.get_device_name(0))
    print('Memory Usage:')
    print('Allocated:', round(torch.cuda.memory_allocated(0)/1024**3,1), 'GB')
    print('Cached:   ', round(torch.cuda.memory_reserved(0)/1024**3,1), 'GB')
```

#### 4.2 Python packages:
- Always use `pip` command in Windows Terminal to install python packages 
- there is a requirements.txt that contains the principal data science libraries (without pytorch as you have installed it from the previous line, just do `pip install -r https://raw.githubusercontent.com/AmineDjeghri/BetterWindowsUX/master/requirements.txt`

# 5- UX Custommization
## WSL (Windows subsystem for Linux ) / Windows Terminal :

 
 #### Windows Terminal & WSL : 
 - Open Ubuntu terminal from current location : go to windows terminal ->  parameters -> profiles -> ubuntu -> command line (under name) and change it to `ubuntu run`
 - Use ubuntu as default terminal in pycharm: tools>terminal  and put in shell path: `ubuntu run`
 - You can use this command to convert a windows path to wsl path : `wslpath  'C:\Users\AmineDjeghri\Desktop\git\quarterback-tabular'`
 - copy your ssh key from windows to linux and use on the ssh file of linux : `chmod 600 your_ssh_file`

## customize linux terminal
### Install and set up zsh as default

If necessary, follow these steps to install Zsh:

1. install Zsh:

   - With the package manager of your choice, _e.g._ `sudo apt install zsh`

2. Verify installation by running `zsh --version`. Expected result: `zsh 5.0.8` or more recent.

3. Make it your default shell: `chsh -s $(which zsh)`

4. Log out and log back in again to use your new default shell. And enter the number 0 .

5. Test that it worked with `echo $SHELL`. Expected result: `/bin/zsh` or similar.

6. Test with `$SHELL --version`. Expected result: 'zsh 5.8' or similar

source : https://github.com/ohmyzsh/wiki/edit/main/Installing-ZSH.md

### install miniconda
- install miniconda on ubuntu 
- copy the export link to your .zshrc ( if you want to find it : `cd` then `ls -a` then `nano .zshrc` or use windows explorer to navigate to it : 
`\\wsl.localhost\Ubuntu\home\amine ` and open the file .zshrc with notepad or sublimText.

```
#### enable miniconda
export PATH="/home/amine/miniconda3/bin:$PATH")
```
- run : `conda init zsh`
- close all the terminals and run again ubuntu terminal.
- you should see the `(base)` noun before the command.


#### What is ZSH-Syntax-Highlighting?
The ZSH syntax highlighting feature—similar to one found in the fish shell—automatically highlights your commands as you type them, which can help you catch syntax errors and fix them before running the command.
- `sudo apt-get install git`
- `git clone https://github.com/zsh-users/zsh-syntax-highlighting.git`
- The next step is to add the syntax-highlighting extension to the .zshrc file. The value of the ZDOTDIR variable will determine this. Use the command shown below:
`echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc`
- source ./zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

#### What is Oh my ZSH ?
- Oh My Zsh is an open source, community-driven framework for managing your zsh configuration.
-  with wget `sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"`

#### some pluggins : autosuggestions and syntaxh highlighting

run the following commands on your teminal 
- `git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`
- `git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting`

Open your editor and add these lines in .zshrc file at ~/.zshrc (you can do that through windows explorer as you did before)
```
plugins=(git
zsh-autosuggestions
zsh-syntax-highlighting
)
```
- other plugings :[website](https://www.linkedin.com/pulse/how-install-start-using-oh-my-zsh-boost-your-mantas-levinas/?trk=pulse-article_more-articles_related-content-card)

#### Powerlevel10k 
- Powerlevel10k is a theme for Zsh. It emphasizes speed, flexibility and out-of-the-box experience.
- `git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k`
- Set ZSH_THEME="powerlevel10k/powerlevel10k" in ~/.zshrc.
- install this font on windows [MesloLGS NF Regular.ttf](https://github.com/romkatv/dotfiles-public/blob/master/.local/share/fonts/NerdFonts/MesloLGS%20NF%20Regular.ttf)
- restart ubuntu terminal and configure your theme.

### Costumize your windows:
- #### Rainmeter: 
![windows desktop](https://github.com/AmineDjeghri/BetterWindows/blob/master/windows-desktop.png)
- Install rainmeter
- Install https://github.com/mpurses/Sonder/releases
- Download this wallpaper https://raw.githubusercontent.com/mpurses/Sonder/master/Skins/Sonder/Wallpapers/Trees-22.jpg


- O&O ShutUp 10 : privacy control windows
- DS4Windows : make playstation controllers work on PC : https://github.com/Ryochan7/DS4Windows/releases
- Bing wallpaper: https://www.microsoft.com/en-us/bing/bing-wallpaper?SilentAuth=1&wa=wsignin1.0
- Pin some folders and drivers, Recycle Bin in the file explorer. Fast browsing: right click on the file explorer in the taskbar to show the shortcut to the pinned folders.
- Desktop icons: Personalization->themes->desktop icon settings
- WinAero Tweaker : customize the appearance and behavior of the operating system in a flexible way (context menu)
- TaskbarX [link] (https://chrisandriessen.nl/taskbarx), also hide windows taskbar (right click on the taskbar -> taskbar settings-> hide in desktop mode)
- Fences [link] (https://store.steampowered.com/app/607380/Fences/?l=french) doesn't need steam to autostartup 
- Hide the Windows taskbar (right click on the taskbar -> taskbar settings). You can and make it centered and transparent with [TaskbarX]([https://chrisandriessen.nl/taskbarx)

# NOT UPDATED YET
### Browser websites
- Configure some websites on your desktop and taskbar as shorcuts (Netflix, Google calendar, Gmail...ect)
- <ins>Gmail and Google Calendar</ins> : you can configure dark mode ("Thèmes" et cliquez sur "Tout afficher", choose "dark/sombre") and priority notifications (all new emails), signature.
- 

### SSH (needs to be updated and fileZilla)
 - https://github.com/AmineDjeghri/BetterWindowsUX/blob/master/SSH-PPTI-SU.md

- PyCharm envs: You can clean out old PyCharm interpreters that are no longer associated with a project see the image [here](https://github.com/AmineDjeghri/BetterWindowsUX/blob/master/pycharm_interpreters.PNG) .
- This gives you a listing where you can get rid of old virtualenvs that PyCharm thinks are still around 

### Windows design and UX: 
- You can convert a website to an application , for exemple: Google Agenda  in Brave/Chrome, go to plus d'outils -> creer un racourcie , and check window mode, it will run like an app in your windows desktop
( I took the example of mattermost because there is no free Google Agenda app in windows )
- Remove unnecessary programs, unnecessary icons from the start menu and add others like google maps, meteo calendar
- App shortcut : some apps don't provide a desktop shortcut, even if you try to find where they are you can't (like Netflix), they only give you the choice to add them to the start menu or the taskbar . But there is a solution :
             - if an app doesn't want to be added to the desktop like netflix, you can drag it from the start menu to the desktop
             - if it's not on the start up menu, search for it then add it to start menu then drag it to desktop
- Use windows touchpad gestures, it really improves the experience and saves time, for exemple create a desktop and open a windows inside it, then you can create another desktop and put another window in it, after this you can fast switch between the two desktops using your four fingers and swap from the left to right 
- Use Quiet Hours and add only the applications that you want them to send you a notification, (Brave will still send you notifications to get BAT but it will never appear ;) )
- 
### Screen recorder :
- You can use the integrated screen recorder of windows, press `windows key + G` 
- Use other free software like: OBS, Streamlabs

### Screenshot in windows 10: Windows provides two ways to take a screenshot
#### 1) Windows screenshot 
- Press the `Windows key + Shift + S`. The integrated windows screenshot software will open. You can drag to select parameters like: active windows, all screen, region ...ect.
- Press `PrtScn` This copies the entire screen to the clipboard. You can paste the screenshot into any program that displays images, like Paint or Microsoft Word.
- Press `Alt + PrtScn` . This copies the active window to the clipboard, which you can paste into another program. 

#### 2) Windows Snipping Tool
1. search for it in the search bar
2. In the "Mode" drop down, choose the kind of screenshot shape you want — you can choose anything from full screen to rectangular to a free-form shape

### Wifi :
if your pc keeps switching between 5ghz and 2.4ghz do the following:
- If it's your wifi: split your WiFi into 2 access points, one for 5Ghz and the other for 2.4Ghz. After that make your PC connect to the 5Ghz one only 
- If it's not your wifi but you have an ethernet port, you can always buy a router( example HONOR ROUTER 3 WIFI 6) and you will have your own private network and can split the wifi into 2 access points like i mentionnned it in the section above.
### More  
 - <ins>Deactivate startup programs</ins>:task manager -> startup -> deactivate software that you don't want it to run at startup ( do the same in ccleaner)
 - <ins>Windows partition</ins>: use the windows partition integrated software to create , delete or format partitions
 - You can change your power management options (when windows will be put on sleep, what happens when you close your laptop ..ect)
 - If you consider buying a laptop with a GPU for Deep Learning, go for an NVIDIA laptop with with a GPU that supports CUDA. You can always use the cloud solutions for GPU computing: Google Colab, 100$ Free Azure Credits...ect. Just DON'T buy a laptop with an AMD GPU for Deep Learning.

## Awesome Piracy : 
https://github.com/Igglybuff/awesome-piracy

### Pycharm remote deployment : 
Defining a server as default:
A deployment server is considered default if its settings apply by default during automatic upload of changed files. To define a deployment server as the default one, follow these steps:

Choose the desired server on the Deployment page. You can open this page it two possible ways: either Settings/Preferences | Build, Execution, Deployment | Deployment, or Tools | Deployment | You will see your servers, right click on the one you want to set it as default, and click 'use as default' 

Enabling automatic upload:
As soon as the default server is set, you can make upload to this server automatic. This can be done in the following two ways:

Open the deployment Options (Settings/Preferences | Deployment | Options or Tools | Deployment | Options from the main menu), and in the Upload changed files automatically to the default server field choose Always, or On explicit save action. The difference between these two choices is explained in the field description.
In the main menu, select Tools | Deployment | Automatic upload. Note that automatic upload in this case is performed in the Always mode.
