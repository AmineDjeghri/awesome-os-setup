# 1. PyCharm:

## 1.1. Tips & tricks
- I prefer to use PyCharm (professional edition) even if I used VSCode for 2 years, the Intellij suite is just amazing. Intellij suite with all the plugins for students is completely free.
- Sync pycharm settings : https://www.jetbrains.com/help/pycharm/sharing-your-ide-settings.html#IDE_settings_sync
- Remote/local terminal & interpreter :
  - When creating a project with pycharm, you should use the anaconda python (windows or wsl) and not install python or using another one like virtualenv.
  - You can use ubuntu as default terminal in pycharm: tools>terminal and put in a shell path: `ubuntu run`
  - Add WSL interpreter in Pycharm (add interpreter -> WSL). For example, Conda installed in WSL, will be available in Pycharm.
- Pytest :
  - you can choose by editing the configuration template of python and pytest + unit tests to select a default working directory for all your scripts
  - You can Run pytest just by right-clicking on a function bloc, file, or folder!
- Always use Markdown code and add `py` to tell the markdown that it's python code. When you will do refactor. It will change the python code in the readme.
- Plugins: You can download plugins from the settings menu. I recommend the following plugins:
  - github copilot
  - TBD
- PyCharm has keyboard shortcuts for most of its commands related to editing, navigation, refactoring, debugging, and other tasks. Memorizing these hotkeys can help you stay more productive by keeping your hands on the keyboard. [Link to Cheatsheet](https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf)

## 1.2. Personal pycharm shortcuts
Official[Link to Cheatsheet](https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf)

Some of them are re-mapped :

**Panels & windows :**

| Panel                        | Shortcut                               |
|------------------------------|----------------------------------------|
| Press the blue button        | alt+p                                  |
| project panel          alt+P |                                        |
| terminal panel               | alt + T                                |
| new terminal                 | alt maj T                              |
| settings                     | ctrl+alt+S then type with the keyboard |
| **Git**                      |                                        |
| Git commit  panel            | ctrl + K                               |
| Git panel                    | alt + g                                |
| Git update                   | not defined yet                        |
| git emoji                    | show toolbar like alt+w then alt+g     |
| git menu                     | alt+k then alt+ctrl+g                  |
| git menu                     | show toolbar like alt+w then alt+g     |
| git menu                     | show toolbar like alt+w then alt+g     |
| **run/debug**                |                                        |
| debug                        | maj + F9                               |
| git menu                     | alt+9                                  |
| debug panel                  | show toolbar like alt+w then alt+g     |
| run                          | maj +F10                               |
| run panel                    | alt+ 0                                 |


**Code editor**

| Action                                           | Shortcut                                     | more                                                                                                               |
|--------------------------------------------------|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| insert                                           | alt+ insert                                  | can be used in editor or project panle                                                                             |
| Quick documentation                              | Ctrl + Q                                     |                                                                                                                    |
| extract method/constant/variable/field/parameter | Ctrl + Alt + M/C/V/F/P                       |                                                                                                                    |
| select bloc                                      | ctrl + w                                     | select (the more you press w, the more it wraps other parts. you can then press any other thing to wrap it arround |
| definitons                                       | ctrl j                                       |                                                                                                                    |
| move bloc                                        | ctrl + shift + arrow                         |                                                                                                                    |
| find                                             | ctrl + F                                     |                                                                                                                    |
| jump to line                                     | ctrl+g                                       |                                                                                                                    |
| refactor                                         | alt+r + first option                         |                                                                                                                    |                                        |
| rename                                           | alt+r then select the second option (rename) |                                                                                                                    |
| delete/cut line                                  | ctrl+x                                       |                                                                                                                    |
| Ctrl + B	                                        | Go to declaration or usages                  | works as bold typo in markdown files                                                                               |
| end of line                                      | :End:                                        |                                                                                                                    |
| beginning of line                                | Home                                         |                                                                                                                    |
| next word:                                       | Ctrl+Right                                   |                                                                                                                    |
| previous word                                    | Ctrl+Left                                    |                                                                                                                    |



## 1.3. Pycharm remote deployment
WARNING: project folder needs to be on windows and not WSL to use the remote ssh. Do not host folders outside WSL if you are not using a remote interpreter, there are  [WSL perforamance issues](https://github.com/microsoft/WSL/issues/4197?notification_referrer_id=MDE4Ok5vdGlmaWNhdGlvblRocmVhZDUyMzA5ODA3MjozMjcxNTkxMw%3D%3D#issuecomment-1727108838))

Defining a server as default:
A deployment server is considered default if its settings apply by default during automatic upload of changed files. To define a deployment server as the default one, follow these steps:

Choose the desired server on the Deployment page. You can open this page it two possible ways: either Settings/Preferences | Build, Execution, Deployment | Deployment, or Tools | Deployment | You will see your servers, right click on the one you want to set it as default, and click 'use as default'

Enabling automatic upload:
As soon as the default server is set, you can make upload to this server automatic. This can be done in the following two ways:

Open the deployment Options (Settings/Preferences | Deployment | Options or Tools | Deployment | Options from the main menu), and in the Upload changed files automatically to the default server field choose Always, or On explicit save action. The difference between these two choices is explained in the field description.
In the main menu, select Tools | Deployment | Automatic upload. Note that automatic upload in this case is performed in the Always mode.


## 1.4. Python remote interpreter
- add a remote python interpreter: usually found with `which python` on the remote server.
- PyCharm envs: You can clean out old PyCharm interpreters that are no longer associated with a project see the image [here](https://github.com/AmineDjeghri/BetterWindowsUX/blob/master/pycharm_interpreters.PNG) .
- This gives you a listing where you can get rid of old virtualenvs that PyCharm thinks are still around

## 1.5. Remote SSH for ReactJS
- First make sure that in the server, the React project is running when you run `yarn dev run`
- In pycharm, go to configuration and create a new config for npm
- select package.json from the local folder
- select command: run
- select scripts: dev
- Node interpreter: copy and paste the result of the command `which node` in the remote server
- package manager: yarn, for example
- environment : `PATH=` put the result of the command `echo $PATH`
