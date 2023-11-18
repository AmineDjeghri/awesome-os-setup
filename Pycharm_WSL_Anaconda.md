# PyCharm: 
- I prefer to use PyCharm (Education/professional which is free for students) 
- BECAREFUL when creating a project with pycharm, you should use the anaconda python or wsl anaconda and not another one like virtualenv.
- Sync pycharm settings : https://www.jetbrains.com/help/pycharm/sharing-your-ide-settings.html#IDE_settings_sync
- PyCharm has keyboard shortcuts for most of its commands related to editing, navigation, refactoring, debugging, and other tasks. Memorizing these hotkeys can help you stay more productive by keeping your hands on the keyboard. [Link to Cheatsheet](https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf)
- The first thing you need to do is to create a project and test these shortcuts. Everytime you test one that you find usefull, write it in a paper next to you. Later you can look at the paper to remember.
- <ins>Pycharm Jupyter Notebook</ins> : Use the one provided in Pycharm. It provides better autocomplete.
- You can use ubuntu as default terminal in pycharm: tools>terminal  and put in shell path: `ubuntu run`
- Use ubuntu as default terminal in pycharm: tools>terminal  and put in shell path: `ubuntu run`
- Add WSL interpreter in Pycharm (add interpreter -> WSL)

## 1. My Pycharm config : 
- [Shortcuts](https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf)
- [myconfig] TODO
- Plugins I use:
  - TODO
  - TODO
- Tips & tricks:
  - TODO
 

## 2.Pycharm remote deployment :
WARNING : project folder needs to be on windows and not WSL to use the remote ssh. Do not host folders outside WSL if you are not using a remote interpreter, there are  [WSL perforamance issues](https://github.com/microsoft/WSL/issues/4197?notification_referrer_id=MDE4Ok5vdGlmaWNhdGlvblRocmVhZDUyMzA5ODA3MjozMjcxNTkxMw%3D%3D#issuecomment-1727108838))

Defining a server as default:
A deployment server is considered default if its settings apply by default during automatic upload of changed files. To define a deployment server as the default one, follow these steps:

Choose the desired server on the Deployment page. You can open this page it two possible ways: either Settings/Preferences | Build, Execution, Deployment | Deployment, or Tools | Deployment | You will see your servers, right click on the one you want to set it as default, and click 'use as default' 

Enabling automatic upload:
As soon as the default server is set, you can make upload to this server automatic. This can be done in the following two ways:

Open the deployment Options (Settings/Preferences | Deployment | Options or Tools | Deployment | Options from the main menu), and in the Upload changed files automatically to the default server field choose Always, or On explicit save action. The difference between these two choices is explained in the field description.
In the main menu, select Tools | Deployment | Automatic upload. Note that automatic upload in this case is performed in the Always mode.


## Python SSH 
- add a remote python : usually found with `which python` on the remote server. 
- PyCharm envs: You can clean out old PyCharm interpreters that are no longer associated with a project see the image [here](https://github.com/AmineDjeghri/BetterWindowsUX/blob/master/pycharm_interpreters.PNG) .
- This gives you a listing where you can get rid of old virtualenvs that PyCharm thinks are still around
- 
## Filezilla 
- Download Filezilla and import your key (if you key isn't in the right format, convert it with putty). Excellent for Drag & Drop.
- There is also the plugin Pycharm remote server that does almost the same things, except that filezilla can save multiple servers and make it easier to open them from the favorites folder.


## Remote SSH for ReactJS
- First make sure that in the server, the react project is running when you run `yarn dev run`
- In pycharm, go to configuration and create a new config for npm 
- select package.json from the local folder
- select command : run
- select scripts : dev
- Node interpreter : copy paste the result of the command `which node` in the remote server
- package manager : yarn for example
- environement : `PATH=` put the result of the commande `echo $PATH` 

# Run configuration :
- you can choose by editing the configuration template of python and pytest to select a default working directory for all your scripts
- Run pytest just by right clicking on a function bloc, file, or folder !
