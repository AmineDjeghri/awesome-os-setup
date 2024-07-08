# 1. Shortcuts and app setup
Settings and shortcuts for some apps that I use on Windows 11.
**Table of Contents**
<!-- TOC -->
* [1. Shortcuts and app setup](#1-shortcuts-and-app-setup)
  * [1.1. Windows shortcuts](#11-windows-shortcuts)
  * [1.2. Mac shortcuts](#12-mac-shortcuts)
  * [1.3. GlazeWM (windows only)](#13-glazewm-windows-only)
  * [1.4. PowerToys (windows only)](#14-powertoys-windows-only)
  * [1.5. Windows Terminal (windows only)](#15-windows-terminal-windows-only)
  * [1.6. Sublime Text 4 (All platforms)](#16-sublime-text-4-all-platforms)
  * [1.7. Obsidian (All platforms)](#17-obsidian-all-platforms)
  * [1.8. PyCharm (All platforms)](#18-pycharm-all-platforms)
    * [1.8.1. Tips & tricks](#181-tips--tricks)
    * [1.8.2. Personal pycharm shortcuts](#182-personal-pycharm-shortcuts)
    * [1.8.3. Python remote interpreter (SSH /WSL)](#183-python-remote-interpreter-ssh-wsl)
    * [1.8.4. Pycharm remote deployment](#184-pycharm-remote-deployment)
    * [1.8.5. Remote SSH for ReactJS](#185-remote-ssh-for-reactjs)
  * [1.9. HWINFO:](#19-hwinfo)
  * [1.10. Google colab:](#110-google-colab)
  * [1.11. Powerpoint:](#111-powerpoint)
  * [1.12. Streamio (Streaming on all platforms)](#112-streamio-streaming-on-all-platforms)
    * [Installation:](#installation)
<!-- TOC -->

## 1.1. Windows shortcuts
- Display copy-paste history: `win + v`
- Lock screen: `win + L`
- WIP

## 1.2. Mac shortcuts
- Lock screen: `ctrl + cmd + Q`
- Screenshots: `cmd + shift + 3` for the whole screen, `cmd + shift + 4` for a part of the screen, `cmd + shift + 5` for a video or a screenshot

## 1.3. GlazeWM (windows only)
- Install the GlazeWM tiling window manager.
- Automatic installation of the settings available with this [command](windows_workflow/README_windows.md#2-software). Select the seventh option.
- Manual installation:
  - Download my config [file](windows_workflow/config.yaml) and put it in `C:\Users\%userprofile%\.glaze-wm`

shortcuts: You can read more about the shortcuts [here](https://github.com/glazerdesktop/GlazeWM?tab=readme-ov-file#general)
- close a window: `alt + shift + q`:
- reload the config: `alt + shift + r`:
- Maximize & un-maximize : `alt + f`
- hide: `alt+m` (use `alt+f` to make it appear again)
- switch between multiple full-screen apps in the same workspace : `alt + tab`

## 1.4. PowerToys (windows only)
- Download [Windows store](https://apps.microsoft.com/detail/XP89DCGQ3K6VLD?hl). [Docs](https://learn.microsoft.com/en-us/windows/powertoys/run#features)
- Or use my Windows script to install it via the terminal. [Link](windows_workflow/README_windows.md#2-software)
- I use it mainly for: Search (alt + space) for applications folders or files & Killing a process instead of using task manager.
- You can also access files and folders from the search bar with alt + space then paste the path
- Open a selected application as administrator: Ctrl+Shift+Enter	(only applicable to applications)
- OCR (⊞ + shift + T)
- Color picker (⊞ + shift + C)
- Locksmith (right-click on a file or folder to see which process is using it)

## 1.5. Windows Terminal (windows only)
- Automatic installation of the Terminal settings available with this [command](windows_workflow/README_windows.md#2-software). Select the second option.
- wget on Windows terminal: add it to your terminal: https://www.programmersought.com/article/90723524682/

## 1.6. Sublime Text 4 (All platforms)
- Install the package control: https://packagecontrol.io/installation
- (Windows) Copy and paste the [Package Control.sublime-settings](windows_workflow/Package%20Control.sublime-settings) and [Preferences.sublime-settings](windows_workflow/Preferences.sublime-settings) in : `%UserProfile%\AppData\Roaming\Sublime Text\Packages\User`
- You may need to restart sublime text to see the changes.
- If the editor color is not changed, you can change the theme in the settings :
  - (preferences -> select color scheme-> select one dark)
  - (preferences -> select theme -> select one dark)
  -
## 1.7. Obsidian (All platforms)
- Obsidian plugins are saved inside the vault (a folder). You need to copy the .obisidian folder everytime you create a new vault to keep the same plugins and workspace
- Install the community plugins: TBD
- Install the community themes: TBD
- Sync : use google drive ou github to sync the repositories remotely.
 - Git :
  - if you are on windows. Install git on windows (powershell : 'winget install git.git').
  - Create an ssh key (go to your ssh folder on windows) and add it to git (if you have wsl, you can copy the ssh key from one to another)
  - add global username and email with git config
  -  Restart obsidian. Try to change something on a doc and push it with : 'stage all' then 'commit' then 'push'. To pull stuff you can use the pull button
  -  The source control panel can be found on the left panel. Maybe need to change the size of the left panel to view it
  -  if you facce a problem with dubious owernship of repository, run this command `git config --global --add safe.directory '*'`

## 1.8. PyCharm (All platforms)

### 1.8.1. Tips & tricks
- I've been using PyCharm (professional edition) for more than 3 years now even if I used VSCode for 2 years before that, the Intellij suite is just amazing. Intellij suite with all the plugins for students is completely free.
- If you are on Windows, use pycharm with WSL.
- Use docker with pycharm, very easy to pull and create images & containers. Specially if you want to test your app, you can create a ubuntu container in less then 5sec.
- Sync pycharm settings : https://www.jetbrains.com/help/pycharm/sharing-your-ide-settings.html#IDE_settings_sync
- You can save your current layout (all all plugins positions) by going to Window | Layouts | Save Current Layout as New and switch to it from new projects  by Window | Layouts | <name of your layout> | Apply.
- Change the source folder for imports (https://stackoverflow.com/a/34304165)
- I always use the run button instead of the terminal to run my files (specifically fastapi or streamlit) so pycharm can highlight the errors and make them easily clickable.
- Use the debug function when needed.
- Everytime you start a project, edit the configuration template of python and python tests(autodetect and pytest) to select a default working directory for all your scripts. This will prevent you from having problems with working directory location when running from the terminal and pycharm.
- You can Run pytest just by right-clicking on a function bloc, file, or folder!
- Commits : [doc](https://www.jetbrains.com/help/pycharm/log-tab.html)
  - pre-commit hooks: If you use conda as an interpreter in pycharm, you need to install pre-commit with pip in the environment that you are using. After the installation, see in the commit options (wheel button) next to the message if `Run git hooks` is there. If it isn't then restart pycharm.
  - When you write in your terminal : `pip list | grep pre-commit` you should see the package. Running `pre-commit --version` should also work.
  - Check the Amend commit box if you want to concatenate commits
  - If you want to delete a pushed commit :
    - Make sure that the branch isn't protected: open IDE settings Ctrl+Alt+S then go to git settings. You will see in the Push settings the protected branches. Note that if a branch is marked as protected on GitHub, PyCharm will automatically mark it as protected when you check it out but you can modify it.
    - To delete a pushed commit, you have to options: drop a commit, or reset a current branch to a specific commit. After doing one or the other open the push panel and instead of selecting 'push', select 'force push'. Remember that you need to force push, otherwise pycharm will tell you that there are changes on the remote that need to be merged.
- Remote/local terminal & interpreter :
  - When creating a project with pycharm, you should use the anaconda python (windows or wsl) and not install python or using another one like virtualenv.
  - You can use ubuntu as default terminal in pycharm: tools>terminal and put in a shell path: `ubuntu run`
  - Add WSL interpreter in Pycharm (add interpreter -> WSL). For example, Conda installed in WSL, will be available in Pycharm.

- Always use Markdown code and add `py` to tell the markdown that it's python code. When you will do refactor. It will change the python code in the readme.
- Plugins: You can download plugins from the settings menu. I recommend the following plugins:
  - github copilot
  - default plugins : services with docker...
  - TBD
- PyCharm has keyboard shortcuts for most of its commands related to editing, navigation, refactoring, debugging, and other tasks. Memorizing these hotkeys can help you stay more productive by keeping your hands on the keyboard. [Link to Cheatsheet](https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf)
- If the plugin Table of contents doesn't work on a markdown file, create a small table with the title & two`<!-- TOC -->`, it should detect it.
- Pycharm has fuzzy search when creating a file. For example 'alt+p' then 'alt+ins' then 'pf' to create a python file
### 1.8.2. Personal pycharm shortcuts
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
| call actions                                     | alt+enter                                    | reformat code, correct code & more , used in editor                                                                |
| insert / create new                              | alt+ insert                                  | can be used in editor (insert tables ect..) or project panel (create new files)                                    |
| create new branch                                | ctrl+alt+n                                   |                                                                                                                    |
| find all                                         | double shift                                 | search everything like files, actions, classes                                                                     |
| find actions                                     | ctrl+shit+a                                  | search actions like tools (docker, remote server) but also execute shortcuts                                       |
| find files                                       | ctrl+shift+n                                 |                                                                                                                    |
| find in files                                    | ctrl+shift+f                                 |                                                                                                                    |
| find inside current panel                        | ctrl + F                                     | can be used in editor                                                                                              |
| show recent files                                | ctrl + E                                     |                                                                                                                    |
| show recent locations                            | ctrl + shift + E                             |                                                                                                                    |
| Quick documentation                              | Ctrl + Q                                     |                                                                                                                    |
| Quick documentation                              | Ctrl + Q                                     |                                                                                                                    |
| **select**                                       |                                              |
| **refactor**                                     |                                              |
| extract method/constant/variable/field/parameter | Ctrl + Alt + M/C/V/F/P                       |                                                                                                                    |
| select bloc                                      | ctrl + w                                     | select (the more you press w, the more it wraps other parts. you can then press any other thing to wrap it arround |
| select  with multiple cursors                    | ctrl + alt shift + mouse                     |                                                                                                                    |
| Select multiple occurrences of a word            | alt j                                        |                                                                                                                    |
| all case-sensitively matching words              | Ctrl Alt Shift J                             |                                                                                                                    |
| move bloc                                        | ctrl + shift + arrow                         |                                                                                                                    |
| refactor (change signature:add/remove parameter) | alt+r + first option                         |                                                                                                                    |                                        |
| rename                                           | alt+r then select the second option (rename) |                                                                                                                    |
| delete/cut line                                  | ctrl+x                                       |                                                                                                                    |
| duplicate line                                   | ctrl+d                                       |                                                                                                                    |
| **moving**                                       |                                              |
| Go to declaration or usages	                     | ctrl+B                                       | works as bold typo in markdown files                                                                               |
| end of line                                      | :End:                                        |                                                                                                                    |
| beginning of line                                | Home                                         |                                                                                                                    |
| next word:                                       | Ctrl+Right                                   |                                                                                                                    |
| previous word                                    | Ctrl+Left                                    |                                                                                                                    |
| jump to line                                     | ctrl+g                                       |                                                                                                                    |

### 1.8.3. Python remote interpreter (SSH /WSL)
- add a remote python interpreter: usually found with `which python` on the remote server or WSL.
- PyCharm envs: You can clean out old PyCharm interpreters that are no longer associated with a project see the image [here](https://github.com/AmineDjeghri/BetterWindowsUX/blob/master/pycharm_interpreters.PNG) .
- This gives you a listing where you can get rid of old virtualenvs that PyCharm thinks are still around


### 1.8.4. Pycharm remote deployment
WARNING: project folder needs to be on windows and not WSL to use the remote ssh. Do not host folders outside WSL if you are not using a remote interpreter, there are  [WSL perforamance issues](https://github.com/microsoft/WSL/issues/4197?notification_referrer_id=MDE4Ok5vdGlmaWNhdGlvblRocmVhZDUyMzA5ODA3MjozMjcxNTkxMw%3D%3D#issuecomment-1727108838))

Defining a server as default:
A deployment server is considered default if its settings apply by default during automatic upload of changed files. To define a deployment server as the default one, follow these steps:

Choose the desired server on the Deployment page. You can open this page it two possible ways: either Settings/Preferences | Build, Execution, Deployment | Deployment, or Tools | Deployment | You will see your servers, right click on the one you want to set it as default, and click 'use as default'

Enabling automatic upload:
As soon as the default server is set, you can make upload to this server automatic. This can be done in the following two ways:

Open the deployment Options (Settings/Preferences | Deployment | Options or Tools | Deployment | Options from the main menu), and in the Upload changed files automatically to the default server field choose Always, or On explicit save action. The difference between these two choices is explained in the field description.
In the main menu, select Tools | Deployment | Automatic upload. Note that automatic upload in this case is performed in the Always mode.


### 1.8.5. Remote SSH for ReactJS
- First, make sure that in the server, the React project is running when you run `yarn dev run`
- In pycharm, go to configuration and create a new config for npm
- select package.json from the local folder
- select command: run
- select scripts: dev
- Node interpreter: copy and paste the result of the command `which node` in the remote server
- package manager: yarn, for example
- environment: `PATH=` put the result of the command `echo $PATH`

## 1.9. HWINFO:
- export file: regedit -> ``Ordinateur\HKEY_CURRENT_USER\Software\HWiNFO64``
- import settings: double-click on the downloaded file to restore settings. Check mine [here](windows_workflow/HWINFO_settings.reg)
## 1.10. Google colab:
- Add this code to prevent it from disconnecting. [source](https://colab.research.google.com/github/oobabooga/AI-Notebooks/blob/main/Colab-TextGen-GPU.ipynb#scrollTo=f7TVVj_z4flw)
```py
#@title 1. Keep this tab alive to prevent Colab from disconnecting you { display-mode: "form" }

#@markdown Press play on the music player that will appear below:
%%html
<audio src="https://oobabooga.github.io/silence.m4a" controls>
```
## 1.11. Powerpoint:
**Turn a PDF to black and white**
Convert to pptx (IlovePDF)
Open with PowerPoint (Office 2016)
(If you want to remove the background: view -> Slide Master: click on the first one then click on the background and delete, return by closing with the red cross: close the Master view)
Print color and select full black and white

## 1.12. Streamio (Streaming on all platforms)
- Stremio is a video streaming application that allows you to watch and organize video content from different services, including movies, series, live TV and video channels. The content is aggregated by an addon system providing streams from various sources. And with its commitment to security, Stremio is the ultimate choice for a worry-free, high-quality streaming experience.
- You can either use your favorite platforms to watch movies or series or use torrent without any risk.
- Stremio is available on all platforms: Windows, Mac, Linux, Android, iOS, Android TV & Web.

### Installation:
- Always use the desktop app to install addons & configure them, settings will be synchronized between all your devices
- (Update July 2024): You need both `stremio` and `stremio service` on PC to make it work perfectly.
- Setup : [Tutorial](https://www.reddit.com/r/StremioAddons/comments/17833ms/stremio_all_you_need_to_know/)
  - Force stop or restart the app on your deivces to synchronize the settings if you add an addon with the desktop app.
  - My recommended official addons: Watchhub, Cinemeta, Opensubtitles V3, Opensubtitles, Local Files
  - My recommended community addons : Streaming Catalogs, Trakt TV (with two websites : [trakt.tv](https://trakt.tv/dashboard) + [couchmoney](https://couchmoney.tv/), Torrentio (With real-debrid), YggStremio (for french), debrid search (with real-debrid)
    - Order of installed community addons: Trakt TV, Streaming Catalogs, Torrentio, YggStremio, Debrid search
    - Trakt addon uses trakt.tv (requires login) and couchmoney (if you want recommendations)
    - Ratings & history: I rank my movies (and series) on trakt (they will automatically marked as watched if you activate that setting in trakt's website : settings -> Mark Watched After Rating: Automatically mark unwatched items with today's date).
    - If you want to syncronize everything with IMDB and/or the streaming platforms, you can use these two applications:
      - [Universal Trakt Scrobbler](https://chromewebstore.google.com/detail/universal-trakt-scrobbler/mbhadeogepkjdjeikcckdkjdjhhkhlid) - a Chrome extension for synchronizing Streaming platforms (netflix, prime,...) watched history with Trakt
      - [IMDB-Trakt-Syncer](https://github.com/RileyXX/IMDB-Trakt-Syncer)a python app to synchronize IMDB ratings, watchlist... with Trakt both ways (You can use it in WSL2, install Google Chrome in WSL2 first)

  Tips :
  - Use Stremio desktop to configure addons. ALl settings & addons will sync between your devices if you use the same account.
  - You can install multiple times addons with different configurations (for example, a Torrentio specific for french audio).
  - Order of a list in Stremio home is determined by the installation order.
  - Sort and filter movies inside a list by clicking on 'see more' on a list.
  - You can find and safely download all the torrents from real debrid in the [torrents section](https://real-debrid.com/torrents). Click on the green box to either download or stream the torrent.
  - You can also use stremio on iOS with VLC: go to [stremio web](https://web.stremio.com/) and follow [this tutorial](https://blog.stremio.com/using-stremio-web-on-iphone-ipad/). It works with torrents and everything.
  - Remember to rate what you watch on IMDB or trakt and run the Chrome extension & python app to sync everything.
  - If you didn't rate some movies & tv shows, you can add them to history in Trakt to avoid being recommended in couchmoney (no need to rate them if you forget how good or bad the movie was)

  ### TV Settings :
  - My first advice is to never use the standard mode on your TV. Always use the cinema/ filmaker or movie mode. The standard mode is too bright and the colors are not accurate. Use the cinema or movie mode when watching movies or series.
  - Here is a [video](https://www.youtube.com/watch?v=dY3M_h30HYc) explaining TV modes. And [this video](https://www.youtube.com/watch?v=nTO2Wmw1NKA) for changing the settings of your TV taking into account different modes (SDR, HDR, Dolby). (You can refer to reddit guides or YouTube videos or [rtings.com](rtings.com) to find the best settings).
  - If your TV supports multiple content types (SDR, HDR, DOLBY), the mode needs to be activated on each content type.
  - On some TVs like the Hisense U7k, you need to enable enhanced HDMI mode to access dolby vision & 60HZ on your chromecast and other HDMI inputs.
  - If you play video games, use the game mode. It will reduce the input lag and improve the gaming experience.
  - Some settings :
    - (Important) Enhance the performance of your Google TV by following this [tutorial](https://www.slashgear.com/1321192/tricks-make-chromecast-google-tv-run-faster/)
    - Chromecast google TV 4k [video settings](https://www.reddit.com/r/Chromecast/comments/1ct77ai/a_fix_for_washed_out_colors_and_performance/)
    - Chromecast google TV remote : you can use your iphone or android to remotely control google tv and use your phone's keyboard for example. You need either Google TV app or Goohle home app on you phone. on your google tv, the fezture is disabled by default: you need to go to system-> keyboard -> manage keyboards -> check virtual remote. You can now use your phone to type things rapidely
    - Windows 11 with 4K HDR TV: follow this [tutorial 1](https://www.pcmag.com/how-to/set-up-gaming-pc-on-4k-tv) and [tutorial 2](https://www.pcmag.com/how-to/how-to-play-games-watch-videos-in-hdr-on-windows-10)
  - recommended TV apps for google TV: projectivy launcher, stremio, youtube atv. update the channels in the projectivy and add stremio there. Also make it the default launcher for your tv.
