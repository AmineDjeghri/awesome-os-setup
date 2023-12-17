Linux / WSL2 (Ubuntu 22.04) Workflow
==================
![Windows WSL Terminal](windows_wsl_terminal.png)

Welcome to the guide for setting up a powerful terminal & python environment on Linux/WSL.

**Table of Contents**
<!-- TOC -->
* [Linux / WSL2 (Ubuntu 22.04) Workflow](#linux--wsl2-ubuntu-2204-workflow)
  * [1. Setup Linux automatically](#1-setup-linux-automatically)
    * [1.1. Terminal customization](#11-terminal-customization)
    * [1.2. Run the script](#12-run-the-script)
  * [2. Setup Linux manually](#2-setup-linux-manually)
    * [2.1. Terminal customization](#21-terminal-customization)
    * [2.2. Linux shell customization](#22-linux-shell-customization)
        * [2.2.1. Install ZSH](#221-install-zsh)
        * [2.2.2. Install Oh-my-zsh](#222-install-oh-my-zsh)
        * [2.2.3. Install the power-level-10k theme](#223-install-the-power-level-10k-theme)
        * [2.2.4. install miniconda in WSL](#224-install-miniconda-in-wsl)
        * [2.2.5. Install Cuda using conda](#225-install-cuda-using-conda)
<!-- TOC -->

The repository contains an automated script to install the main elements I use in Linux/WSL. The repository is currently in development (maybe will add an Ansible version in the future).
My workflow involves utilizing WSL for development tasks and relying on Windows for all other activities. You can check the parent README here: https://github.com/AmineDjeghri/Awesome-Windows11-WSL


## 1. Setup Linux automatically
I developed this tool to streamline the setup process when working on various servers, such as AWS instances and not having to install everything manually every time.
While it's particularly useful for Python developers, feel free to customize it for your specific needs. The script is in bash (might move to Ansible in the future).

### 1.1. Terminal customization
- Download and install the [Firacode font](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/FiraCode.zip) on your primary operating system (Windows if you are using WSL).
- Configure your terminal to utilize the newly installed font. For Windows, check this [link](../windows_workflow/README.md#232-inswindows-terminalins). For Linux ##TODO.
### 1.2. Run the script
- Run this command to install customize the shell: oh-my-zsh, pl10k theme, and install miniconda & cuda (if you have a GPU) automatically:
```bash
sh -c "$(wget https://raw.githubusercontent.com/AmineDjeghri/Awesome-Windows11-WSL-Linux/master/unix_workflow/auto_linux_setup.sh -O -)"
```
- Do not run the script with `sudo` otherwise it will install some packages in `/root` instead of `/home`.
- Also, make sure to type `yes` when installing conda. If you are facing some problems, take a look at section 2.2.
- (Optional) If you have custom configurations in your `.bashrc`, consider copying them to the `.zshrc` file.
- (Optional) If you have ssh keys, copy them to the `.ssh` folder.

## 2. Setup Linux manually

### 2.1. Terminal customization
This step involves installing the font and is the same as in the previous [section](#11-terminal-customization)
### 2.2. Linux shell customization
##### 2.2.1. Install ZSH
1. install Zsh:
   - With the package manager of your choice, _e.g._ `sudo apt install zsh`
2. Verify installation by running `zsh --version`. Expected result: `zsh 5.8.1` or more recent.
3. Run `zsh` to start configuring it (You can create an empty file with 0, will configure it later). You can delete .zshrc and run `zsh` to configure
   it again.
4. Log out and log back in again to use your new default shell.
5. Optional:Make it your default shell: `chsh -s $(which zsh)` but doesn't work on every system. If it doesn't work, will do it later with oh-my-zsh. Test that it worked with `echo $SHELL`. Expected result: `/bin/zsh` or similar.Test with `$SHELL --version`. Expected result: 'zsh 5.8' or similar

source : https://github.com/ohmyzsh/wiki/edit/main/Installing-ZSH.md

##### 2.2.2. Install Oh-my-zsh
- Oh My Zsh is an open source, community-driven framework for managing your zsh configuration.
- Run `sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"` and hit yes to make it the default terminal.
- Test if it worked with `echo $SHELL`. Expected result: `/bin/zsh` or similar. Test with `$SHELL --version`: An expected result: 'zsh 5.8' or similar
- If you have conda / cuda or something installed: copy the content from `.bashrc` to `.zshrc` (`vim .zshrc` or use Windows explorer / sublime text. Run again `zsh`, you should see the `(base)` name before the command.

Zsh Plugins
A Zsh plugin is a set of useful aliases and functions designed to make you more productive. Here are some useful & popular plugins :

```
git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
git clone --depth 1 -- https://github.com/marlonrichert/zsh-autocomplete.git $ZSH_CUSTOM/plugins/zsh-autocomplete
```

Open your .zshrc file at ~/.zshrc (you can do that through Windows explorer and sublime text as you did before) and search for `plugins=(git)`.
If you don't find it, then create it and complete it with the missing plugins as shown in the example bellow :
```
plugins=(git
        dirhistory
        history
        colored-man-pages
        jsontools
        zsh-autosuggestions
        zsh-syntax-highlighting
        zsh-autocomplete
```
- Run `zsh` to restart the terminal, now you can see the changes when you try to write a command like `cd`
- If there are some problems, test the solutions available [here](https://stackoverflow.com/a/37175174/8354747) & [here](https://stackoverflow.com/a/36994356/8354747)
Others :
- Auto update oh my zsh: uncomment this: `zstyle ':omz:update' mode auto`
- Add the following alias to the end of .zshrc file to easily open sublime Text from windows: `alias sublime="subl.exe"`. Try it with: `sublime .zshrc`
- You can visit this [website](https://www.linkedin.com/pulse/how-install-start-using-oh-my-zsh-boost-your-mantas-levinas/?trk=pulse-article_more-articles_related-content-card) to understand more about the installed plugins. you can skip directly to `7. Enable Zsh Plugins` section and start reading. You will see that you have installed most of the commands there.

##### 2.2.3. Install the power-level-10k theme
- This theme requires the font Firacode. Check the section setup terminal if you didn't install it yet.
- Power-level10k is a theme for Zsh. It emphasizes speed, flexibility and out-of-the-box experience.
- `git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k`
- Open .zshrc and set `ZSH_THEME="powerlevel10k/powerlevel10k"`.
- reload ubuntu terminal with `zsh` and configure your theme.

##### 2.2.4. install miniconda in WSL
 - run `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh` (Conda 23.3.1 Python 3.10.10 released April 24, 2023)
 - run `chmod +x Miniconda3-latest-Linux-x86_64.sh`
 - run `bash Miniconda3-latest-Linux-x86_64.sh`
 - restart the shell with `bash` command (or `zsh` if you changed your shell)
 - if `(base)` is not showing and `.bachrc` file doesn't contain the init of conda, go to `~/miniconda3/bin` and run `conda init`
 - close and reopen ubuntu terminal or run `bash`, you should see `(base)` at the left of any command.
 - run `conda env list` to check the installed environments and their path.

##### 2.2.5. Install Cuda using conda
- Follow this [conda_cuda_installation guide](1_cuda_pytorch_install.md)
