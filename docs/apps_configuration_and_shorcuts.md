Apps configuration and shortcuts
================================

**Table of Contents**
<!-- TOC -->
* [Apps configuration and shortcuts](#apps-configuration-and-shortcuts)
* [1. Shortcuts and app configurations](#1-shortcuts-and-app-configurations)
  * [1.1. Windows shortcuts](#11-windows-shortcuts)
  * [1.2. GlazeWM (windows only)](#12-glazewm-windows-only)
  * [1.3. PowerToys (windows only)](#13-powertoys-windows-only)
  * [1.4. Windows Terminal (windows only)](#14-windows-terminal-windows-only)
  * [1.5. Sublime Text 4 (All platforms)](#15-sublime-text-4-all-platforms)
  * [1.6. Obsidian (All platforms)](#16-obsidian-all-platforms)
  * [1.7. DisplayFusion (Windows only & paid)](#17-displayfusion-windows-only--paid)
  * [1.8. Files](#18-files)
  * [1.9. PyCharm (All platforms)](#19-pycharm-all-platforms)
    * [1.9.1. Tips & tricks](#191-tips--tricks)
    * [1.9.2. Personal pycharm shortcuts](#192-personal-pycharm-shortcuts)
    * [1.9.3. Python remote interpreter (SSH /WSL)](#193-python-remote-interpreter-ssh-wsl)
    * [1.9.4. Pycharm remote deployment](#194-pycharm-remote-deployment)
    * [1.9.5. Remote SSH for ReactJS](#195-remote-ssh-for-reactjs)
  * [1.10. HWINFO:](#110-hwinfo)
  * [1.11. Google colab:](#111-google-colab)
  * [1.12. Powerpoint:](#112-powerpoint)
  * [1.13. Streamio (Streaming on all platforms)](#113-streamio-streaming-on-all-platforms)
    * [1.13.1. Installation:](#1131-installation)
  * [1.14. WinToys](#114-wintoys)
<!-- TOC -->

# 1. Shortcuts and app configurations

Settings and shortcuts for some apps that I use on Windows 11.

## 1.1. Windows shortcuts

- Display copy-paste history: `win + v`
- Lock screen: `win + L`
- WIP

## 1.2. GlazeWM (windows only)

- Install the GlazeWM tiling window manager.
- Automatic installation of the settings available with this [command](windows_workflow/README_windows.md#12-software).
  Select the seventh option.
- Manual installation:
    - Download my config [file](windows_workflow/config.yaml) and put it in `C:\Users\%userprofile%\.glaze-wm`

shortcuts: You can read more about the
shortcuts [here](https://github.com/glazerdesktop/GlazeWM?tab=readme-ov-file#general)

- close a window: `alt + shift + q`:
- reload the config: `alt + shift + r`:
- Maximize & un-maximize : `alt + f`
- hide: `alt+m` (use `alt+f` to make it appear again)
- switch between multiple full-screen apps in the same workspace : `alt + tab`
- If you are using Citrix Worskpace nad want to only use one monitor, then resize its window by moving a little bit the
  border before maximizing it (i Know that you can't resize a window if glazewm is running, but this is just to tell
  citrix that you are in a single monitor).
  Check [this](https://help-docs.citrix.com/en-us/citrix-workspace-app/windows/multi-monitor-support.html) to understand
  how dual monitor works on Citrix.

## 1.3. PowerToys (windows only)

-
Download [Windows store](https://apps.microsoft.com/detail/XP89DCGQ3K6VLD?hl). [Docs](https://learn.microsoft.com/en-us/windows/powertoys/run#features)
- Or use my Windows script to install it via the terminal. [Link](windows_workflow/README_windows.md#2-software)
- I use it mainly for: Search (alt + space) for applications folders or files & Killing a process instead of using task
  manager.
- You can also access files and folders from the search bar with alt + space then paste the path
- Open a selected application as administrator: Ctrl+Shift+Enter    (only applicable to applications)
- OCR (⊞ + shift + T)
- Color picker (⊞ + shift + C)
- Locksmith (right-click on a file or folder to see which process is using it)

## 1.4. Windows Terminal (windows only)

- Automatic installation of the Terminal settings available with
  this [command](windows_workflow/README_windows.md#2-software). Select the second option.
- wget on Windows terminal: add it to your terminal: https://www.programmersought.com/article/90723524682/

## 1.5. ZED (All platforms)
- (TBD)

## 1.6. Obsidian (All platforms)

- Obsidian plugins are saved inside the vault (a folder). You need to copy the .obisidian folder every time you create a
  new vault to keep the same plugins and workspace
- You can copy my [.obsidian](windows_workflow/win_dotfiles/.obsidian) folder to get the same confi as me. The shortcut for settings is the same as pycharm (alt + ctrl + s)
- Do not sync the ``workspace.json`` file since it contains sensitive information (name of files, etc..)
- Install the community plugins: TBD
- Install the community themes: TBD
- Sync: use Google Drive ou GitHub to sync the repositories remotely.
- Git :
- if you are on Windows. Install git on windows (PowerShell: 'winget install git.git').
- Create an ssh key (go to your ssh folder on windows) and add it to git (if you have wsl, you can copy the ssh key from
  one to another)
- add global username and email with git config
- You can configure the git plugin in settings to automatically push and pull every x minutes.
- The source control panel can be found on the left panel. Maybe need to change the size of the left panel to view it
- if you face a problem with dubious ownership of repository, run this
  command `git config --global --add safe.directory '*'`
- if you face a problem with fatal: could not read Username for 'https://github.com'. go to the folder from a terminal and run git pull. If you are on MacOS, you need to use a token instead of writing your password.
## 1.7. DisplayFusion (Windows only & paid)

- DisplayFusion is a program that will help you to manage your multiple monitors. It allows you to create different
  profiles for your monitor setups, such as single, dual, or triple monitors. You can configure specific applications to
  always open on designated monitors within each profile. With just one click, you can switch between these profiles,
  and DisplayFusion will automatically rearrange your windows according to the rules you set. This makes it easy to
  adapt your workspace to different scenarios, whether you're working with one monitor or multiple monitors.
- Link to my settings containing different profile for 1, 2, 3 and TV
  settings. [here](windows_workflow/win_dotfiles/DisplayFusion Backup.reg)
    - use the Steam version (it can be used on multiple computers with the same steam account)
    - it adds a lot of features to Windows monitor settings.
    - There are four apps available after the installation. The main ones are: DisplayFusion and "monitor settings
      displayfusion"

## 1.8. Files

- Files: Replace the Windows File Explorer. Manage all your files with increased productivity. Work across multiple
  folders with tabs and so much more.
    - Download [Files](https://files.community/). There are two versions: direct installer (free) & Microsoft Store (
      paid)
    - Replace Windows File explorer with Files: [link](https://files.community/docs/configuring/replace-file-explorer/)
    - You can import my settings: [link](Files_3.0.15.0.zip). Open Files -> Settings -> advanced -> import settings

## 1.9. PyCharm (All platforms)

- I prefer to use PyCharm & other Intellij products like WriterSide...(the Pro version is free for students)
- My personal shortcuts & tips & settings for this app [here](../shortcuts_and_apps_setup.md#1-5-pycharm)

### 1.9.1. Tips & tricks

- I've been using PyCharm (professional edition) for more than 3 years now, even if I used VSCode for 2 years before
  that, the Intellij suite is just amazing. Intellij suite with all the plugins for students is completely free.
- Change the default location of projects : instead of PycharmProjects. Settings -> Appearance & behavior -> system settings
- If you are on Windows, use pycharm with WSL.
- Sync pycharm settings : https://www.jetbrains.com/help/pycharm/sharing-your-ide-settings.html#IDE_settings_sync
- You can save your current layout (all plugin positions) by going to Window | Layouts | Save Current Layout as New and
  switch to it from new projects by Window | Layouts | <name of your layout> | Apply.
- Project settings : Everytime you start a project make sure to
    - Change the source folder for imports (https://stackoverflow.com/a/34304165).
    - Edit the configuration template of python and python tests(autodetect and pytest) to
  select a default working directory for all your scripts. If you changed the source folder, it should match it. This will prevent you from having problems with working directory location when running from the terminal and pycharm.
- I always use the run button (or shortcut) instead of the terminal to run my files (specifically fastapi or streamlit) so pycharm can highlight the errors and make them easily clickable.
- Use the debug function when needed.
- You can Run pytest just by right-clicking on a function bloc, file, or folder!
- Git Clone: You can directly clone a repository from your git accounts by going to the Menu bar | VCS | Get from
  Version Control | GitHub | and select the right repository.
- You can write a ``#TODO`` in the .py files or ``[//]: # (TODO  Add Google TV setup  ) `` in the markdown files to see them
  in the TODO panel.
- Commits : [doc](https://www.jetbrains.com/help/pycharm/log-tab.html)
    - pre-commit hooks: Just run in the interminal pre-commit install. Pycharm should detect it. After the installation, see in the commit panel (where you enter the commit message) (wheel button) next to the
      message if `Run git hooks` is there. If it isn't, then restart pycharm. Next time your commit, pycharm will run the pre-commit hooks
    - When you write in your terminal: `pip list | grep pre-commit` you should see the package.
      Running `pre-commit --version` should also work.
    - Check the Amend commit box if you want to concatenate commits
    - If you want to delete a pushed commit :
        - Make sure that the branch isn't protected: open IDE settings Ctrl+Alt+S then go to git settings. You will see
          in the Push settings the protected branches. Note that if a branch is marked as protected on GitHub, PyCharm
          will automatically mark it as protected when you check it out, but you can modify it.
        - To delete a pushed commit, you have to options: drop a commit, or reset a current branch to a specific commit.
          After doing one or the other, open the push panel and instead of selecting 'push', select 'force push'.
          Remember that you need to force push, otherwise pycharm will tell you that there are changes on the remote
          that need to be merged.
- Docker :
    - Use docker with pycharm, straightforward to pull and create images & containers. Specially, if you want to test
      your app, you can create an ubuntu container in less then 5sec.
    - In Pycharm settings, configure docker to run under WSL & not Windows. It will automatically detect the ports.
- Remote/local terminal & interpreter :
    - When creating a project with pycharm, you should use the anaconda python (windows or wsl) and not install python
      or using another one like virtualenv.
    - You can use ubuntu as default terminal in pycharm: tools>terminal and put in a shell path: `ubuntu run`
    - Add WSL interpreter in Pycharm (add interpreter -> WSL). For example, Conda, installed in WSL, will be available
      in Pycharm.
    - You can use docker as an interpreter in Pycharm (If you have a powerful computer like a desktop or a Macbook,
      otherwise, a laptop with Windows 11 + WSL2 + pycharm + docker isn't a good idea). To set Docker Port Bindings When
      Using Pycharm Run/Debug Go to: Python file > Edit Configuration > Docker container settings (click on open folder
      icon) At Edit Docker Container Settings, you can add Port bindings. Or set the python configuration to use this so
      all the python files can use the same configuration.
- Always use Markdown code and add `py` to tell the Markdown that it's python code. When you will do refactor. It will
  change the python code in the readme.
- Plugins: You can download plugins from the settings menu. I recommend the following plugins:
    - GitHub copilot (autocomplete, but also provides functions when you right-click on something like: explain,
      generate tests...etc.)
    - default plugins: services with docker...
    - TBD
- PyCharm has keyboard shortcuts for most of its commands related to editing, navigation, refactoring, debugging, and
  other tasks. Memorizing these hotkeys can help you stay more productive by keeping your hands on the
  keyboard. [Link to Cheatsheet](https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf)
- If the plugin Table of contents doesn't work on a Markdown file, create a small table with the title &
  two`<!-- TOC -->`, it should detect it.
- Pycharm has fuzzy search when creating a file. For example, 'alt+p' then 'alt+ins' then 'pf' to create a python file
- (To confirm) Pycharm Jupyter Notebook: Use the one provided in Pycharm. It provides better autocomplete.
- WriterSide issue : files eit

### 1.9.2. Personal pycharm shortcuts

Official[Link to Cheatsheet](https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf)

Some of them are re-mapped :

The macos shortcuts are inverted in my system so i can use the same commands as in windows. The ones in this list works for both since i use the name of the key and not the real inverted key.
**Panels & windows :**

| Panel                        | Windows (MacOS) Shortcut                               
|------------------------------|----------------------------------------|
| Press the blue button        | alt+p  (command+p)                                | 
| project panel          alt+P |                                        |
| terminal panel               | alt + T  (command+t)                                |
| new terminal                 | alt maj T                              |
| settings                     | ctrl+alt+S (fn+,)then type with the keyboard |
| **Git**                      |                                        |
| Git commit  panel            | ctrl + K (command +t)                              |
| Git panel                    | alt + g (command +g)                               |
| Git update                   | not defined yet                        |
| git emoji                    | show toolbar like alt+w then alt+g     |
| git emoji                     | open git panel with alt+k then alt+ctrl+g                  |
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

### 1.9.3. Python remote interpreter (SSH /WSL)

- add a remote python interpreter: usually found with `which python` on the remote server or WSL.
- PyCharm envs: You can clean out old PyCharm interpreters that are no longer associated with a project see the
  image [here](https://github.com/AmineDjeghri/BetterWindowsUX/blob/master/pycharm_interpreters.PNG) .
- This gives you a listing where you can get rid of old virtualenvs that PyCharm thinks are still around

### 1.9.4. Pycharm remote deployment

WARNING: project folder needs to be on windows and not WSL to use the remote ssh. Do not host folders outside WSL if you
are not using a remote interpreter, there
are  [WSL perforamance issues](https://github.com/microsoft/WSL/issues/4197?notification_referrer_id=MDE4Ok5vdGlmaWNhdGlvblRocmVhZDUyMzA5ODA3MjozMjcxNTkxMw%3D%3D#issuecomment-1727108838))

Defining a server as default:
A deployment server is considered default if its settings apply by default during automatic upload of changed files. To
define a deployment server as the default one, follow these steps:

Choose the desired server on the Deployment page. You can open this page it two possible ways: either
Settings/Preferences | Build, Execution, Deployment | Deployment, or Tools | Deployment | You will see your servers,
right click on the one you want to set it as default, and click 'use as default'

Enabling automatic upload:
As soon as the default server is set, you can make upload to this server automatic. This can be done in the following
two ways:

Open the deployment Options (Settings/Preferences | Deployment | Options or Tools | Deployment | Options from the main
menu), and in the Upload changed files automatically to the default server field choose Always, or On explicit save
action. The difference between these two choices is explained in the field description.
In the main menu, select Tools | Deployment | Automatic upload. Note that automatic upload in this case is performed in
the Always mode.

### 1.9.5. Remote SSH for ReactJS

- First, make sure that in the server, the React project is running when you run `yarn dev run`
- In pycharm, go to configuration and create a new config for npm
- select package.json from the local folder
- select command: run
- select scripts: dev
- Node interpreter: copy and paste the result of the command `which node` in the remote server
- package manager: yarn, for example
- environment: `PATH=` put the result of the command `echo $PATH`

## 1.10. HWINFO:

- export file: regedit -> ``Ordinateur\HKEY_CURRENT_USER\Software\HWiNFO64``
- import settings: double-click on the downloaded file to restore settings. Check
  mine [here](windows_workflow/win_dotfiles/HWINFO_settings.reg)

## 1.11. Google colab:

- Add this code to prevent it from
  disconnecting. [source](https://colab.research.google.com/github/oobabooga/AI-Notebooks/blob/main/Colab-TextGen-GPU.ipynb#scrollTo=f7TVVj_z4flw)

```py
# @title 1. Keep this tab alive to prevent Colab from disconnecting you { display-mode: "form" }

# @markdown Press play on the music player that will appear below:
%%html
< audio
src = "https://oobabooga.github.io/silence.m4a"
controls >
```

## 1.12. Powerpoint:

**Turn a PDF to black and white**
Convert to pptx (IlovePDF)
Open with PowerPoint (Office 2016)
(If you want to remove the background: view -> Slide Master: click on the first one then click on the background and
delete, return by closing with the red cross: close the Master view)
Print color and select full black and white

## 1.13. Streamio (Streaming on all platforms)

- Stremio is a video streaming application that allows you to watch and organize video content from different services,
  including movies, series, live TV and video channels. The content is aggregated by an addon system providing streams
  from various sources. And with its commitment to security, Stremio is the ultimate choice for a worry-free,
  high-quality streaming experience.
- You can either use your favorite platforms to watch movies or series or use torrent without any risk.
- Stremio is available on all platforms: Web, Windows, Mac, Linux, Android, iOS, Android TV, Apple TV...
- Addons...etc will be synchronized between all your devices.
- (Depreated) [Tutorial](https://www.reddit.com/r/StremioAddons/comments/17833ms/stremio_all_you_need_to_know/)
- What is a debrid service? A debrid service is an unrestricted multi-hoster that allows you to stream and download videos instantly at the best speeds. In plain English, the debrid services act as a proxy between the BitTorrent tracker and you, so you download the content directly from their servers at high speed. Most of the content is already cached, meaning you can instantly access it. Personnaly, I use ALL Debrid, but others exist like : TorBox, Real Debrid...

### 1.13.1. Installation:
- (Update November 2025)


- Setup :
    - After making any change to any addon, you don't need to close the application to synchronize the changes, just click on the addons tab, and go back to home.
    - My recommended Setup:
      - Uninstall all the default addons (Except 'Cinemeta' which can't be removed but there is a trick to do it in the end of this tutorial) 
      - Ratings Addon : https://72059fbbd1e5-stremio-addon-ratings.baby-beamup.club
        - My config : Copy this [link](https://72059fbbd1e5-stremio-addon-ratings.baby-beamup.club/mdbListApiKey=d9u6lt5a2xzblluxc1jeva83d&tmdbApiKey=204180a30d24982b89ff5796277b1301&ratings=imdb%2Ctomatoes%2Cmetacritic%2Cmetacriticuser%2Ctrakt&showAllRatingsInPercent=true&showPercentSymbol=false&showOverallRating=true&calculateOverallRatingBasedOn=all&ageRatings=commonsensemedia&ageRatingCountryNames=flag&displayAgeRatingsAtTop=false&showUnavailableAgeRatings=false&ratingColorMarkers=hearts&ratingColorMarkersCustom=%F0%9F%92%8B%2C%F0%9F%8D%8A%2C%F0%9F%8C%B3%2C%E2%99%A0%EF%B8%8F&showRatingVotes=true&showRatingVotesIcon=true&showUnavailableRatings=false&openOnClick=show-all-ratings&allRatingsAndDetailsBlocks=Details%2COverview%2CCastAndCrew%2CRecommendations%2CAllScores%2CAllAgeRatings%2CButtonLinks&whereToWatchCountry=US&installEmojiChecker=false&widgets=&randomEpisodeIncludedScope=all&randomEpisodeIncludedShows=&randomEpisodeShowSeasonEpisodeNumber=false&sessionId=a3e22347-a258-4d4e-97b1-aa8bb9c7fc9a/manifest.json) and paste it in Stremio Addons : 
   
      - AIOStreams:

          ## 🌐 AIOStreams + Stremio Configuration Guide

          ### 🧩 What is AIOStreams?
          [AIOStreams (ElfHosted)](https://aiostreams.elfhosted.com/) is an all-in-one **Stremio addon manager** that lets you organize, install, and sync all your favorite addons in one place.  
          It also allows you to **save your configuration online**, so you don’t lose your setup.  

          Your data is linked to a **UUID** (your unique ID) and a **password**, so you can restore your configuration anytime.

          ---

          ### 🪪 Step 1 — Login to Stremio Web
          Go to 👉 [https://web.stremio.com/](https://web.stremio.com/)  
          Log in with your regular Stremio account.

          ---

          ### ⚙️ Step 2 — Open AIOStreams
          Visit 👉 [https://aiostreams.elfhosted.com/](https://aiostreams.elfhosted.com/)  

          This page is where you manage everything related to your addons.

          ---

          ### 🧱 Step 3 — Create Your Configuration
          1. Go to the **“Save and Install”** section.  
          2. Enter a **password** of your choice — this will create your AIOStreams account.  
          3. You’ll receive a **UUID** (like your username).  
          4. **Save both the UUID and your password!** You’ll need them to restore or import your configuration later.

          ---

          ### 📂 Step 4 — Import Your Settings (Optional)
          If you already have a saved configuration file:
          1. Go to **“Navigate and Install”**.  
          2. Click **Import**.  
          3. Select and upload your saved configuration file.

          Your addons and settings will load automatically.

          ---

          ### 🔑 Step 5 — Enable Your Debrid Services
          1. In AIOStreams, go to **Services**.  
          2. Enable your preferred **Debrid service** (e.g., Real-Debrid, AllDebrid, Premiumize).  
          3. Enter your API key.  
          4. Click **Save**.

          ---

          ### 🇫🇷 Step 6 — Enable and Configure French Addons
          Go to the **Addons** section. You’ll see a list of installed addons.  
          Some may be deactivated (unsupported ones for now).

          #### ⚙️ Configure *CometFR (custom)*:
          1. Click the **Edit** button.  
          2. Copy the **Manifest URL**.  
          3. Paste it in a **new browser tab**.  
          4. Configure the addon (enter your debrid key).  
          5. Click **Copy Link** — the link should start with  
             `https://comet.stremiofr.com/`  
             and end with `=/manifest.json`.  
          6. Go back to AIOStreams, paste this link in the URL field, and **Activate** the addon.

          #### ⚙️ Configure *JackettioFR (custom)*:
          1. Click the **Edit** button.  
          2. Copy the **Manifest URL**.  
          3. Open it in a **new browser tab**.  
          4. Configure it (enter your debrid key) and click **Install**.  
          5. A **Stremio Link** will appear — right-click and choose **Copy link**.  
             It should start with  
             `https://jackettio.stremiofr.com/`  
             and end with `=/manifest.json`.  
          6. Go back to AIOStreams, paste this link, and **Activate** the addon.

          ---

          ### 💾 Step 7 — Save and Install
          1. Go back to the **Install** section.  
          2. Click **Save** — this saves your configuration to your online AIOStreams account.  
          3. Then click **Install** and choose **Stremio Web** (or your preferred option).  
          4. Stremio will open and prompt you to install your configured addons.

          ---

          ### ✅ Step 8 — Test Everything
          Open any movie or TV show in Stremio.  
          You should now see your addons providing streams — including CometFR and JackettioFR!

          ---

          ### 💡 Tips
          - Keep your **UUID** and **password** safe — that’s your AIOStreams login.  
          - You can restore your setup anytime by re-entering your credentials.  
          - AIOStreams makes it easy to sync and manage all your addons from one place.
       
     -  In Stremio Settings, you can select the prefered 'Audio language' and 'Subtitles'. This will automatically set the audio and subs automatically when you watch something. This is not synced between devices, you need to do it manually on each of your device.
     - (optional) Uninstall Cinemeta : https://www.reddit.com/r/StremioAddons/comments/1d8wbul/how_to_remove_cinemeta/
       - If you disable Cinemeta, enable then the ' Cinemeta (custom) ' in AIOStreams and reinstall the addon.
     - (Optional) Trakt :
        - Trakt is a media tracking service that helps users sync their TV shows and movies across numerous platforms and devices.
        - You can enable trakt in Stremio settings. You can download Trakt mobile app or use their website. 
       - Ratings & history: I rank my movies (and series) on trakt (they will automatically mark as watched if you
         activate that setting in trakt's website : settings -> Mark Watched After Rating: Automatically mark unwatched
         items with today's date).
       - If you want to syncronize everything with IMDB and/or the streaming platforms, you can use these two
         applications:
           - [IMDB-Trakt-Syncer](https://github.com/RileyXX/IMDB-Trakt-Syncer)a python app to synchronize IMDB ratings,
             watchlist... with Trakt both ways (You can use it in WSL2, install Google Chrome in WSL2 first)

  Tips :
    - Use Stremio web to configure addons. ALl settings & addons will sync between your devices if you use the same
      account.
    - Order of a list(catalogà in Stremio home is determined by the installation order (except in AIOSteams were you can order them manually).
    - You can what you watch on IMDB or trakt and run the Chrome extension & python app to sync everything.
    - If you didn't rate some movies & tv shows, you can add them to history in Trakt to avoid being recommended by the 'AI Search' addon.

## 1.14. WinToys
