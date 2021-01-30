# BetterWindowsUX
Some windows tips to improve your UX experience when using windows


### 1- Windows config
#### 1.1- Get a free windows 10 and others softwares if you are a student with Azure
 - If you are a student, maybe you are eligible to have a free windows key and a lot of others microsoft softwares (it only depends on the partnership between your University and Microsoft)
- Follow this link https://azureforeducation.microsoft.com/devtools .To directly access Azure, login here and select Azure for Students: https://portal.azure.com/#blade/Microsoft_Azure_Education/EducationMenuBlade/overview
- If you successfully got a free student plan, got here to see all the avaible softwares including windows 10 Education: https://portal.azure.com/#blade/Microsoft_Azure_Education/EducationMenuBlade/software 
(also If you‘ve reached the end of your 12 months and are still a student, you‘ll be able to renew your Azure for Students offer. )
- Then activate the key in windows (if you had a version that is not education, it will ask your for an update) or download windows education and install it, do not login with your account when installing it because it will ask you your university email and it's better to save your key to your microsoft account. when the installation is finished, link your account in windows settings 

#### 1.2 Save your key to you microsoft account
 - Connect windows with your outlook account to save and link the key to your account 
 - Activate localization on windows
 - Activate bitlocker to encrypt your data (Exists only on windows pro, education and entreprise edition)
 - When placing an external monitor that runs 144hz, make sure to activate the `144Hz` in display settings 
 
### Software 
-  Anaconda (for python and jupyter): install it and check add path, make sure to delete every avaible python version on your system 
- Sublime Text: install it before installing git bash (to make git bash uses sublime as an editor and not vim)
Go to Control Panel > System and Security > System > Advanced system settings and add C:\Program Files\Sublime Text 3 to the PATH environment variable.

Check that the PATH variable does not already contain the path to subl.exe so to avoid adding it twice.
- Git-Bash: You can use linux commands in windows ! Download gitbash to have the same commands as in linux, you can even personalize your terminal
( to check if linux commands work: run 'python --version' in gitbash to see if anaconda added python to the path, you can now use it like linux, 'pip install ' ect.. will work  )
git bash works in every directory, right lick in any directory and you can have a bash with that path 
- install Hinterland extension (for autocomlete) in jupyter https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231
- VScode: enable sync profile, and add gitbash as the default terminal of vscode to replace the powershell 
- Google Sync Drive:  download it on windows and put your git repositories inside it, you can use vscode to run the codes in your pc and also google colab 
- Microsoft word 2016 buy it or ...., install it, than convert the activation.txt to .bat, run it as an administrator and make sure internet is on, 
even it it fails the first time, let it continue to run, it will find a KMS server after.
- SSH: https://github.com/AmineDjeghri/BetterWindowsUX/blob/master/SSH-PPTI-SU.md
- wget: doesn't work, you should use your browser to download it or use an alternative library
- Browser : Brave
- Browser extension: uBlock Origin, pocket, Free Download Manager, Google translate, Google Dictionnary, Stream video downloader, colorZilla
- Antivirus: Kaspersky Cloud free
- Mail: add your mail accounts to Windows Mail
- Others: CCleaner, Speccy,
- Adobe: Photoshop, illustrator, premiere pro, XD
- VPN: ProtonVPN

### Windows design and UX: 
- You can convert a website to an application , for exemple: Mattermost in chrome, go to plus d'outils -> creer un racourcie , and check window mode, it will run like an app in your windows desktop
( I took the example of mattermost because using their windows application causes WIFI disconnect issues, so ihave to use the website instead of the app)
- Remove unnecessary programs, unnecessary icons from the start menu and add others like google maps, meteo calendar
- App shortcut : some apps don't provide a desktop shortcut, even if you try to find where they are you can't (like Netflix), they only give you the choice to add them to the start menu or the taskbar . But there is a solution :
             - if an app doesn't want to be added to the desktop like netflix, you can drag it from the start menu to the desktop
             - if it's not on the start up menu, search for it then add it to start menu then drag it to desktop
- Hide the Windows taskbar (right click on the taskbar -> taskbar settings). You can and make it centered and transparent with [TaskbarX]([https://chrisandriessen.nl/taskbarx)
- Use windows touchpad gestures, it really improves the experience and saves time, for exemple create a desktop and open a windows inside it, then you can create another desktop and put another window in it, after this you can fast switch between the two desktops using your four fingers and swap from the left to right 

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

### More  
 - task manager -> startup -> deactivate software that you don't want it to run at startup ( do the same in ccleaner)
 - windows partition: use the windows partition integrated software to create , delete or format partitions
 - You can change your power management options (when windows will be put on sleep, what happens when you close your laptop ..ect)
