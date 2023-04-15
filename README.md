# BetterWindows11
![windows desktop terminal](https://github.com/AmineDjeghri/BetterWindows/blob/master/windows-desktop-terminal_1.png)
![WSL terminal](https://github.com/AmineDjeghri/BetterWindows/blob/master/resources/wsl_terminal.jpg)

!! Updated for windows 11 !!

Some tips to improve your User experience when using windows. Including the installation of WSL 2.0 and more
- A guide to help you set up a windows environement to maximize your productivity 
- Spend some hours setting this up (a full guide to configure many things including, linux commands in windows no need for dualboot anymore, SSH, SFTP with interface to reach a maximum level of productivity)

## Summary 
1. [Windows Installation](https://github.com/AmineDjeghri/BetterWindows11#1--windows-configuration)
2. [Utility Softwares : Browsers, extensions, daily and usefull programs](https://github.com/AmineDjeghri/BetterWindows11#2-utility-softwares)
3. [Dev Workflow](https://github.com/AmineDjeghri/BetterWindows11#3--dev-workflow)

   3.1 [Dev Software: All the softwares I recommand for developpement and coding](https://github.com/AmineDjeghri/BetterWindows11#31-dev-software)

   3.2 [WSL vs Windows](https://github.com/AmineDjeghri/BetterWindows11#32-linux-wsl-inside-windows-or-just-use-windows-)
4. [UI/UX Custommization](https://github.com/AmineDjeghri/BetterWindows11#4--ux-custommization)


## 1- Windows configuration
- First thing to do is to connect your windows to your microsoft account : Windows-> account -> connect
### 1.1 Save your key to you microsoft account (important)
 - Connect windows with your Microsoft-Outlook) account to save and link the key to your account 
 - Activate localization on windows (if you want to localize your device)
 - Activate bitlocker to encrypt your data (Exists only on windows pro, education and entreprise edition)
 - When placing an external monitor that runs 144hz, make sure to activate the `144Hz` in display settings
 - If you're using OneDrive, becareful when you sync your Desktop and windows specific folders, you can face some problems. My advice is to avoid syncing windows default folders (like Desktop, Documents). Juse use OneDrive as a cloud store.
 - (Optionnal) sleep mode with or without screen lock [here](https://consumer.huawei.com/en/support/content/en-us15592807/#:~:text=Click%20the%20Windows%20icon%20and,Screen%20and%20Sleep%20to%20Never)
 - (Desktop) if you have a 3200mhz RAM and it runs bellow this frequency, activate XMP profile in the BIOS
 

### 1.1 New PC ? transfer your windows key
- On your old PC, check if the key is not an OEM by running  `Slmgr /dli`
- Get your licence key (if you fogot the serial number use a software like : 
- deactivate it windows terminal or cmd using administrator mode with `slmgr /cpky`
- activate it on the new computer using `slmgr /ipk xxxxx-xxxxx-xxxxx-xxxxx-xxxxx`

## 2-Utility Softwares
- <ins>Browser</ins>: Brave or Firefox or Edge, Don't forget to change your sync settings to import your passwords, bookmarks...ect.
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
- <ins>Adobe Suite</ins> : Photoshop or free alternative [Photopea](https://www.photopea.com/), illustrator / adobe premiere pro
- <ins>PDF editing</ins> (3 free tasks per hour) : https://www.sejda.com/ (do not download the desktop app)
- <ins>Windows Terminal </ins> windows terminal works in every directory, right lick in any directory and you can have a bash with that path 
- <ins> Teracopy </ins>
- <ins> Notion </ins>
- <ins> AnyDesk</ins>
### Screen recorder :
- ShareX : screen capturing and GIF recording
- Integrated Screen recording of windows :  press `windows key + G` 
- Screen Recording/ Streaming : OBS or Streamlabs

### Browser websites & extensions
- <ins>Netflix, Prime</ins>: windows store and browser. Browser is better in terms of stability, lists, content and vpn use. On the other hand, Netfliw from the store app and Netfliw on Edge browser  can handle 7.1 and 4k streaming. To add windows apps downloaded from windows store in the taskbar or the desktop :Press Windows key + R then enter shell:appsfolder then drag and drop . 
- Configure some websites on your desktop and taskbar as shorcuts (Netflix, Google calendar, Gmail...ect)
- <ins> Gmail and Google Calendar</ins> : you can configure dark mode ("Thèmes" , , choose "dark/sombre") and priority notifications (all new emails), signature.
- <inst> receive notifications from gmail browser : [Link](https://chrome.google.com/webstore/detail/checker-plus-for-gmail/oeopbcgkkoapgobdbedcemjljbihmemj)
- <inst> receive notifications from google calendar : [Link](https://chrome.google.com/webstore/detail/checker-plus-for-google-c/hkhggnncdpfibdhinjiegagmopldibha)


## 3- Dev workflow
### 3.1 Dev software

#### <ins>Sublime Text</ins> (Free, no need to but the pro lisence): 
- Extremely lightweight (low resource usage), but still keeps around some of the more advanced features you would expect out of a top text editor.
- Install it before installing git bash (a software that adds linux and git commands to windows). 
- (recommanded) CheatSheet
- (optionnal) Run from CLI: go to  `System Properties -> Advanced System Settings -> Advanced -> Environment Variables -> System variable -> path` and add `C:\Program Files\Sublime Text` to the PATH environment variable to make it accessible from the terminal. Close the windows terminal and open a new one and run this command `subl`, it should open Sublime Text.
#### <ins>Git-Bash</ins>:
- You can use linux commands in window like SSH and Git ! Download gitbash to have these commands added to windows Terminal. Open a new Windows terminal after the installation and run this command `git --version` you should see the following message `git version 2.39.1.windows.1`. that means the git command works !
#### <ins>Windows Terminal</ins> 
- Always use windows terminal/powershell instead of linux
- You can update to powershell 7 : Install it from Microsoft store. Close and then re-open your terminal window, Put powershell 7 as default.
#### <ins>PyCharm or VScode</ins>: 
- I prefer to use PyCharm (Education version which is free) but here are the config for both, BECAREFUL when creating a project, you should use the anaconda python or wsl anaconda and not another one like virtualenv)
- Sync pycharm settings : https://www.jetbrains.com/help/pycharm/sharing-your-ide-settings.html#IDE_settings_sync

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
- wget on windows terminal : add it to your temrinal: https://www.programmersought.com/article/90723524682/
- [jupyter autocmplete](https://github.com/krassowski/jupyterlab-lsp#installation) 
#### WSL2 tools : 
   - ncdu : check the disk space usage from wsl 
   - Reclaim disk space : `wsl --shutdown` then `cd 'C:\Users\Amine Djeghri\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\LocalState'` then `optimize-vhd -Path .\ext4.vhdx -Mode full`
   ( it requires these https://askubuntu.com/a/1380274 + https://github.com/microsoft/WSL/issues/4699 +  install this https://superuser.com/a/1307442/769637 install the Hyper-V Platform | Hyper-V Services part, too + restart)

### 3.2 Linux (WSL) inside windows or just use Windows ?
### 3.2.1.Conding using Linux(WSL) inside Windows (BEST CHOICE) - Skip this if you don't want to use WSL

![WSL terminal](https://github.com/AmineDjeghri/BetterWindows/blob/master/resources/wsl_terminal.jpg)

The most amazing thing about windows latest version is WSL (WSL2.0 exactly). You can run Linux in Windows. 
It is fantastic. Virtualisation overhead is not noticeable, full integration between guest and host os's, you can run binaries compiled for MS Windows from linux. Full development toolchain is available as WSLessentialy is linux VM in second incarnation. It supports snapshots and is portable. This made windows useful.
- You can install packages directly in Ubuntu 
- You can easily navigate and communicate between ubuntu and windows as Ubuntu acts like a disk drive.
- You can install conda environement in ubuntu, use GPU, use pycharm on windows to connect to WSL conda env and more.


#### install WSL:
 - Install WSL ``` wsl --install ``` 
 - Restart you computer
 - When installing WSL, it comes with Ubuntu (you don't need to install it from the Windows Store because there are many distribution)
 - In windows search bar, search for `ubuntu` and click on it. It will launch the terminal and install it. If it's not there, make sure you have correctly installed WSL by searching wsl in your windows search bar.
 - Run directly Ubuntu from windows search bar (or launch windows terminal and choose ubuntu or launch windows terminal and run the command `ubuntu`)
 - To make sure Ubuntu is properly installed : run in powershell `ubuntu run`. Make sure also to have the orange ubuntu square in windows search bar.
 - add systemd to wsl.conf : `sudo vim /etc/wsl.conf`:
 ```
[boot]
systemd=true
 ```
  restart the terminal and run `systemctl list-unit-files --type=service` to see some process running
  
#### install miniconda in WSL: 
 - run `wget https://repo.anaconda.com/miniconda/Miniconda3-py39_23.1.0-1-Linux-x86_64.sh`
 - run `chmod +x Miniconda3-py39_23.1.0-1-Linux-x86_64.sh`
 - run `bash Miniconda3-py39_23.1.0-1-Linux-x86_64.sh` (becarefull, when installing at then end, it will tell you if you want to to conda init, write yes instead of no)
 - if you wrote No, run `conda init`
 - close and reopen ubuntu terminal, you should see `(base)` at the left of the any command.
 - run `conda env list` to check the installed environements and their path.
 
#### configure WSL terminal : 
 - To open Ubuntu terminal from current location : go to windows terminal ->  parameters -> profiles -> ubuntu -> command line (under name) and change it to `ubuntu run`
 - (pycharm) Use WSL/ubuntu as the default terminal in pycharm: `settings -> tools -> terminal`  and put in shell path: `ubuntu run`
 - (pycharm) Add WSL conda interpreter in Pycharm (add interpreter -> WSL -> conda) and select the global conda : `/home/amine/miniconda3/bin/conda`. Then click on load environments and it will automatically detect all the conda envs.
 - You can use `wslpath` command to convert a windows path to wsl path : `wslpath  'C:\Users\AmineDjeghri\Desktop\git\myproject'`
 - Copy your ssh key from windows to linux and use on the ssh file of linux : `chmod 600 ~/.ssh/id_rsa` and `chmod 600 ~/.ssh/id_rsa.pub`

#### Install cuda in WSL : 
* We will install cuda 11.7 for pytorch 2.0.0      
* Install CUDA [driver](https://www.nvidia.com/download/index.aspx) on windows
* On windows,  `nvidia-smi`. If you have cuda toolkit installed on windows, run `nvcc --version`. You will see two different CUDA versions shown by nvcc and NVIDIA-smi which is normal if you have cuda toolkit on windows [source](https://stackoverflow.com/a/53504578)

* On linux, run `nvidia-smi`, you will see the same thing as on windows. If you run `nvcc --version`, you will get an error because cuda toolkit is not installed yet on WSL.   

Now, we will install cuda on WSL, the following commands must all be runned inside WSL :
* Run `sudo apt-key del 7fa2af80`
* The CUDA driver installed on Windows host will be stubbed inside the WSL 2 as libcuda.so, therefore users must not install any NVIDIA GPU Linux driver within WSL 2
* You can only install a cuda toolkit that is compatible with WSL inside wsl
* install the cuda toolkit compatible with WSL [here](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local) ny following these instructions. we are installing cuda 11.7 because of pytorch compatibility. 

   
```
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.7.0/local_installers/cuda-repo-wsl-ubuntu-11-7-local_11.7.0-1_amd64.deb
sudo dpkg -i cuda-repo-wsl-ubuntu-11-7-local_11.7.0-1_amd64.deb
sudo cp /var/cuda-repo-wsl-ubuntu-11-7-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda

   
or
wget https://developer.download.nvidia.com/compute/cuda/11.7.0/local_installers/cuda_11.7.0_515.43.04_linux.run
sudo sh cuda_11.7.0_515.43.04_linux.run   
```
* Restart the terminal and run `nvcc --version` to test cuda installation inside wsl. If nvcc is not recognized, it may be possible that the path is not inside .bashrc. First, verify that there is `/usr/local/cuda-11.7` inside WSL .Then, open `.bashrc` and add this at the end if it's not there.
```
export CUDA_HOME=/usr/local/cuda-11.7
export PATH=${CUDA_HOME}/bin:${PATH}
export LD_LIBRARY_PATH=${CUDA_HOME}/lib64:$LD_LIBRARY_PATH   
```   
* Restart the terminal and run again the command `nvcc --version`, you should see `Cuda compilation tools, release 11.7, V11.7.64`  
* You may also need to install cudnn from [here](https://developer.nvidia.com/rdp/cudnn-archive). You need to sign in, download the right version of cdnn for cuda 11.x. directly in wsl using windows explorer and then extract it with windows explorer then run it using `sudo apt install ./cudnn-local-repo-ubuntu2204-8.8.1.3_1.0-1_amd64.deb`
   
(Optional) Tutorials and sources :   
* [Download cuda 11.7](https://developer.nvidia.com/cuda-11-7-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local)      
* [Cuda-wsl Nvidia guide](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl-2](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl-2))
* [Cuda-wsl Ubuntu guide](https://ubuntu.com/tutorials/enabling-gpu-acceleration-on-ubuntu-on-wsl2-with-the-nvidia-cuda-platform#3-install-nvidia-cuda-on-ubuntu)

 
### 3.2.1.Coding using Windows (2nd choice) (Skip this if you are using WSL)
- [Install conda](https://github.com/AmineDjeghri/BetterWindows11/blob/master/install_conda_windows.md)
- [Install Pytorch/Cuda](https://github.com/AmineDjeghri/BetterWindows11/blob/master/install_conda_windows.md)

# 4- UX Custommization
## 4.1 customize WLS (ubuntu) terminal
![WSL terminal](https://github.com/AmineDjeghri/BetterWindows/blob/master/resources/wsl_terminal.jpg)
### Install and set up zsh as default

If necessary, follow these steps to install Zsh:

1. install Zsh:

   - With the package manager of your choice, _e.g._ `sudo apt install zsh`

2. Verify installation by running `zsh --version`. Expected result: `zsh 5.8.1` or more recent.

3. Make it your default shell: `chsh -s $(which zsh)`

4. Log out and log back in again to use your new default shell. And enter the number 1 to create an empty `.zshrc` file .

5. Test that it worked with `echo $SHELL`. Expected result: `/bin/zsh` or similar.

6. Test with `$SHELL --version`. Expected result: 'zsh 5.8' or similar

source : https://github.com/ohmyzsh/wiki/edit/main/Installing-ZSH.md



#### What is Oh my ZSH ?
- Oh My Zsh is an open source, community-driven framework for managing your zsh configuration.
-  with wget `sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"`
- Advanced Tab Autocompletion in Zsh : Another powerful Zsh feature is its tab completion system. It tries to suggest available commands according to the command-line context.
  - type `systemctl`, put a space and then hit TAB to get a list of available systemctl commands with their descriptions. Hit TAB again to start navigating through the list:
  - Type `cd` and put a space and then hit `TAB` twice  to get a list of files and use the arrows or `TAB`  again to navigate in the list between directories
  - Type `system` and without any space press `TAB` to get a list of auto suggestions. You may hit `TAB `again to start navigating through the available programs. Use TAB or ARROW keys to navigate through the list


#### Zsh Plugins : autosuggestions and syntaxh highlighting
A Zsh plugin is a set of useful aliases and functions designed to make you more productive.
run the following commands on your teminal 
- `git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`
- `git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting`

Open your .zshrc file at ~/.zshrc (you can do that through windows explorer and sublime text as you did before) and search for `plugins=(git)`.
If you don't find it, then create it and complete it with the missing plugins as shown in the example bellow : 
```
plugins=(git
        dirhistory
        history
        colored-man-pages
        jsontools
        zsh-autosuggestions
        zsh-syntax-highlighting
)
```

- Auto update oh my zsh : uncomment this: `zstyle ':omz:update' mode auto`
- History Timestamps, navigate with arrows when selecting files
- add the following alias to the end of .zshrc file to easily open sublime Text from windows:
`alias sublime="subl.exe"`. Try it with : `sublime .zshrc`
- uncomment `alias zshconfig="mate ~/.zshrc"`   
- You can visit this :[website](https://www.linkedin.com/pulse/how-install-start-using-oh-my-zsh-boost-your-mantas-levinas/?trk=pulse-article_more-articles_related-content-card) to understand more about the installed plugins. you can skip directly to `7. Enable Zsh Plugins` section and start reading. You will see that you have installed most of the commands there.


#### zsh themes : Powerlevel10k 
- Powerlevel10k is a theme for Zsh. It emphasizes speed, flexibility and out-of-the-box experience.
- `git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k`
- Open .zshrc and set `ZSH_THEME="powerlevel10k/powerlevel10k"`.
- install this font on windows [MesloLGS NF Regular.ttf](https://github.com/romkatv/dotfiles-public/blob/master/.local/share/fonts/NerdFonts/MesloLGS%20NF%20Regular.ttf)
- open windows terminal and go to settings -> profiles (bottom left) -> Ubuntu terminal(orange logo) -> additional parameters-> apparence -> change the font to MesloLGS. 
- (optional) add a new color scheme with this background #383B40. Select the new color scheme on your terminal an put a transparency of 85% [example]([here](https://pureinfotech.com/change-color-scheme-windows-terminal/))
- reload ubuntu terminal with `exec zsh` and configure your theme.

#### update .zshrc (conda and other tools)
- If you have conda / cuda installed : copy the content from .bashrc to .zshrc ( `vim .zshrc` or use windows explorer / sublime text to navigate to it : `\\wsl.localhost\Ubuntu\home\amine `.
- close all the terminals and run again ubuntu terminal.
- you should see the `(base)` noun before the command.

## 4.2 customize Windows terminal
- TO update


## 4.3 Costumize your windows UI:
![windows desktop](https://github.com/AmineDjeghri/BetterWindows/blob/master/windows-desktop.png)
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

## Pycharm : 
You can learn more about pycharm [here]()


