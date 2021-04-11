# BetterWindowsUX
Some windows tips to improve your User experience when using windows
- A guide to help you set up a windows environement to maximum your productivity 
- Spend some hours setting this up (a full guide to configure many things including, linux commands in windows no need for dualboot anymore, SSH, SFTP with interface to reach a maximum level of productivity)

### 1- Windows config
#### 1.1- Get a free windows 10 and others softwares if you are a student with Azure
 - [Free Windows 10 Education/Entreprise](https://github.com/AmineDjeghri/BetterWindowsUX/blob/master/Free-windows-key.md)
 - [Free Microsoft Office 365 Web only depends on your university](https://www.microsoft.com/en-us/education/products/office)
#### 1.2 Save your key to you microsoft account
 - Connect windows with your outlook account to save and link the key to your account 
 - Activate localization on windows
 - Activate bitlocker to encrypt your data (Exists only on windows pro, education and entreprise edition)
 - When placing an external monitor that runs 144hz, make sure to activate the `144Hz` in display settings 
 
### 2- Software 
-  <ins>Anaconda</ins> (for python and jupyter, you can always install python without anaconda, but i prefer to install python via anaconda in windows even if i use only pip with it): install it and CHECK add path to environnement variables, make sure to delete every avaible python version on your system 
- <ins>Sublime Text</ins>: install it before installing git bash (to make git bash uses sublime as an editor and not vim)
Go to Control Panel > System and Security > System > Advanced system settings and add C:\Program Files\Sublime Text 3 to the PATH environment variable.

Check that the PATH variable does not already contain the path to subl.exe so to avoid adding it twice.
- <ins>Git-Bash</ins>: You can use linux commands in windows ! Download gitbash to have the same commands as in linux, you can even personalize your terminal
( to check if linux commands work: run 'python --version' in gitbash to see if anaconda added python to the path, you can now use it like linux, 'pip install ' ect.. will work  )
git bash works in every directory, right lick in any directory and you can have a bash with that path 
- <ins>Jupyter autocomplete</ins>install Hinterland extension (for autocomlete) in jupyter https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231
- <ins>PyCharm or VScode</ins>: I prefer PyCharm but here are the config for both, BECAREFUL when creating a project to use the anaconda python and not another one (that's why you need to make sure to have only the anaconda python installed)
- pycharm : add gitbash to pycharm. file->settings->tools->terminal 
 in shell path add C:\Users\Amine DJEGHRI\AppData\Local\Programs\Git\bin\sh.exe (sh.exe to have the console directly integrated in pycharm console)

Defining a server as default:
A deployment server is considered default if its settings apply by default during automatic upload of changed files. To define a deployment server as the default one, follow these steps:

Choose the desired server on the Deployment page. You can open this page it two possible ways: either Settings/Preferences | Build, Execution, Deployment | Deployment, or Tools | Deployment | You will see your servers, right click on the one you want to set it as default, and click 'use as default' 

Enabling automatic upload:
As soon as the default server is set, you can make upload to this server automatic. This can be done in the following two ways:

Open the deployment Options (Settings/Preferences | Deployment | Options or Tools | Deployment | Options from the main menu), and in the Upload changed files automatically to the default server field choose Always, or On explicit save action. The difference between these two choices is explained in the field description.

In the main menu, select Tools | Deployment | Automatic upload. Note that automatic upload in this case is performed in the Always mode.

- VSCode: enable sync profile, and add gitbash as the default terminal of vscode to replace the powershell 
- Becareful when installing vscode, it can install another python interpreter for you and you will have 2 python on your pc, make sure to delete the vscode one.

#### Advanced Software

- <ins>Browser</ins>: Brave
- <ins>Browser extensions</ins> : uBlock Origin, pocket, Free Download Manager, Google translate, Google Dictionnary, Stream video downloader, colorZilla
- <ins>Privacy extensions</ins> : if you care about your data and privacy (even if you use windows lol) you can limit websites to collect your data:  ClearURLs, Cookie Auto Delete, HTTPS Everywhere, Decentralayes
- <ins>Agenda</ins> : Google agenda, -> create an app shortcut with brave, it will act like an app in windows
- <ins>Antivirus</ins> : Kaspersky Cloud free
- <ins>Mail</ins>: add your mail accounts to Windows Mail
- <ins>Others</ins>: CCleaner, Speccy,
- <ins>Adobe</ins> : Photoshop, illustrator, premiere pro, XD
- <ins>VPN</ins> : ProtonVPN
- <ins>PowerToys</ins> : https://github.com/microsoft/PowerToys
- <ins>Google Sync Drive</ins> :  download it on windows and put the files and folder that you want to be automatically saved on your drive, you won't need to everytime open google drive in your browser and manually put your files there
- <ins>Free Cloud GPU </ins> Google Colab you can either put your git repositories inside google drive to use them in colab, or directly import git repo inside colab without google drive 
- <ins>Microsoft Office 2016</ins>  buy it or ...., install it, than convert the activation.txt to .bat, run it as an administrator and make sure internet is on, 
even it it fails the first time, let it continue to run, it will find a KMS server after.

- wget: doesn't work, you should use your browser to download it or use an alternative library
- <ins>Online Storage</ins> : Google Drive (15gb), Mega Drive (50GB) ...ect. Use these Drives to store non personanal Data ! It's better to have an NAS or an external HDD to store your personal data.
- TaskbarX [link] (https://chrisandriessen.nl/taskbarx), also hide windows taskbar (right click on the taskbar -> taskbar settings-> hide in desktop mode)
- Fences [link] (https://store.steampowered.com/app/607380/Fences/?l=french) doesn't need steam to autostartup 

### SSH (needs to be updated and fileZilla)
 - https://github.com/AmineDjeghri/BetterWindowsUX/blob/master/SSH-PPTI-SU.md
### 3- Pytorch 
- use gitbash to install packages with pip install
- pytorch windows 10 with nvidia GPU that supports cuda:
install the right cuda for pytorch, example cuda 11: 
https://developer.nvidia.com/cuda-11.0-update1-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal
pytorch install with gitbash :

`pip install torch===1.7.1+cu110 torchvision===0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html`
- pytorch without gpu: 

`pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html`
- there is a requirements.txt that contains the principal data science libraries (without pytorch as you have installed it from the previous line, just do `pip install -r https://raw.githubusercontent.com/AmineDjeghri/BetterWindowsUX/master/requirements.txt`
- Check if you succeeded to install pytorch : create a project in PyCharm, select PREVIOUSLY configured interpreter for using the existing one (if you choose NEW environement  yu will have a clean environement with no packages installed and need to install pytoch in this environement with gitbash terminal in PyCharm Project) and copy this code in main.py and run it (You should see the name of your gpu in the console if you have one and successfully installed pytorch with cuda, if you don't have a gpu you will see 'cpu' in the console) :

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
- PyCharm envs: You can clean out old PyCharm interpreters that are no longer associated with a project see the image [here](https://github.com/AmineDjeghri/BetterWindowsUX/blob/master/pycharm_interpreters.PNG) .
- This gives you a listing where you can get rid of old virtualenvs that PyCharm thinks are still around 


### Windows design and UX: 
- You can convert a website to an application , for exemple: Google Agenda  in Brave/Chrome, go to plus d'outils -> creer un racourcie , and check window mode, it will run like an app in your windows desktop
( I took the example of mattermost because there is no free Google Agenda app in windows )
- Remove unnecessary programs, unnecessary icons from the start menu and add others like google maps, meteo calendar
- App shortcut : some apps don't provide a desktop shortcut, even if you try to find where they are you can't (like Netflix), they only give you the choice to add them to the start menu or the taskbar . But there is a solution :
             - if an app doesn't want to be added to the desktop like netflix, you can drag it from the start menu to the desktop
             - if it's not on the start up menu, search for it then add it to start menu then drag it to desktop
- Hide the Windows taskbar (right click on the taskbar -> taskbar settings). You can and make it centered and transparent with [TaskbarX]([https://chrisandriessen.nl/taskbarx)
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
