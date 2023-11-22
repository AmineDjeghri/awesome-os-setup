# Auto-Linux-Setup
![WSL terminal](https://github.com/AmineDjeghri/BetterWindows/blob/master/resources/wsl_terminal.jpg)
Welcome to the guide for setting up a powerful terminal & python environment on Linux/WSL.

The repository contains an automated script to install the main elements I use in Linux/WSL. The repository is currently in developement. 
My workflow involves utilizing WSL for development tasks and relying on Windows for all other activities. You can check the parent repository here : https://github.com/AmineDjeghri/Awesome-Windows11-WSL

**Purpose of this script:** I developed this tool to streamline the setup process when working on various servers, such as AWS instances. Additionally, for those who find manual Linux setup challenging, this script is designed to simplify the process. Forget about the manual setup for each new working machine – just run the script, and you're ready to code. While it's particularly useful for Python developers, feel free to customize it for your specific needs.

The documentation is divided into two sections: one automatic installation script and the second explaining the manual installation process. 
The script incorporates various packages and prompts you for each installation decision. It covers the following aspects:
- Customize the Terminal:  font, ZSH, Oh-my-zsh, and the power-level-10k theme.
- Miniconda Installation: The script facilitates the installation of Miniconda and the creation of an isolated environment tailored for PyTorch, designed to be compatible with your GPU/CPU. This step is crucial for users with a GPU who intend to utilize CUDA. Installing CUDA in a separate environment is recommended. Additional details can be found in the provided documentation [here](https://github.com/AmineDjeghri/Auto-Linux-Setup/blob/main/cuda_pytorch_install.md)
- Nvidia Driver installation: To Do

## Table of contents 
1. [Setup Linux automatically ](#1-setup-linux-automatically-)

2. [Setup Linux manually ](#2-setup-linux-manually--)
    * [customize Linux/WSL terminal](#21-customize-linuxwsl-terminal)
       * [Install and set up the font](#211-install-and-set-up-the-font)
       * [Install ZSH](#212-install-zsh)
       * [Install Oh-my-zsh](#213-install-oh-my-zsh) 
       * [Install the power-level-10k theme](#214-install-the-power-level-10k-theme)
   * [install miniconda in WSL:](#22-install-miniconda-in-wsl)
   * [Install Cuda using conda or globally in the OS :](#23-install-cuda-using-conda-or-globally-in-the-os--)

## 1. Setup Linux automatically : 
- Install the MesloLGS NF Regular.ttf font on your primary operating system (Windows if you are using WSL). [MesloLGS NF Regular.ttf](https://github.com/romkatv/dotfiles-public/blob/master/.local/share/fonts/NerdFonts/MesloLGS%20NF%20Regular.ttf)
- Configure your terminal to utilize the newly installed font. For Windows users, open the Windows Terminal and navigate to Settings -> Profiles (bottom left) -> Ubuntu terminal (orange logo) -> Additional Parameters -> Appearance -> Change the font to MesloLGS.
- Run the following command inside Linux to automatically install the various elements. Do not run the script with `sudo` otherwise it will install some packages in  /root instead of /home. Also, make sure to type `yes` when installing conda. If you are facing some problems, take a look at section 2.2.

```sh -c "$(wget https://raw.githubusercontent.com/AmineDjeghri/Auto-Linux-Setup/main/linux_terminal_custom.sh -O -)"```

- (Optional) If you have custom configurations in your `.bashrc`, consider copying them to  the `.zshrc` file.

## 2. Setup Linux manually  : 

## 2.1 customize Linux/WSL terminal

### 2.1.1 Install and set up the font
- Install the MesloLGS NF Regular.ttf font on your primary operating system (Windows if you are using WSL). [MesloLGS NF Regular.ttf](https://github.com/romkatv/dotfiles-public/blob/master/.local/share/fonts/NerdFonts/MesloLGS%20NF%20Regular.ttf)
- Configure your terminal to utilize the newly installed font. For Windows users, open the Windows Terminal and navigate to Settings -> Profiles (bottom left) -> Ubuntu terminal (orange logo) -> Additional Parameters -> Appearance -> Change the font to MesloLGS.

### 2.1.2 Install ZSH
4. install Zsh:

   - With the package manager of your choice, _e.g._ `sudo apt install zsh`

5. Verify installation by running `zsh --version`. Expected result: `zsh 5.8.1` or more recent.
6. Run `zsh` to start configuring it (You can create an empty file with 0, will configure it later). You can delete .zshrc and run `zsh` to configure it again.
7. Log out and log back in again to use your new default shell.
8. Optional:Make it your default shell: `chsh -s $(which zsh)` but doesn't work on every system. If it doesn't work, will do it later with oh-my-zsh. Test that it worked with `echo $SHELL`. Expected result: `/bin/zsh` or similar.Test with `$SHELL --version`. Expected result: 'zsh 5.8' or similar

source : https://github.com/ohmyzsh/wiki/edit/main/Installing-ZSH.md

### 2.1.3 Install Oh-my-zsh
#### What is Oh my ZSH ?
- Oh My Zsh is an open source, community-driven framework for managing your zsh configuration.
- Run `sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"` and hit yes to make it the default terminal.
- Test if it worked with `echo $SHELL`. Expected result: `/bin/zsh` or similar. Test with `$SHELL --version`: Expected result: 'zsh 5.8' or similar
- If you have conda / cuda or something installed : copy the content from `.bashrc` to `.zshrc` ( `vim .zshrc` or use windows explorer / sublime text . Run again `zsh`, you should see the `(base)` name before the command.

#### Zsh Plugins :
A Zsh plugin is a set of useful aliases and functions designed to make you more productive. Here are some useful & popular plugins : 
  
```
git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
git clone --depth 1 -- https://github.com/marlonrichert/zsh-autocomplete.git $ZSH_CUSTOM/plugins/zsh-autocomplete
```

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
        zsh-autocomplete
```
- run - `zsh` to restart the terminal, now you can see the changes when you try to write a command like `cd`
- If there are some problems test the solutions available [here](https://stackoverflow.com/a/37175174/8354747) & [here](https://stackoverflow.com/a/36994356/8354747)
Others : 
- Auto update oh my zsh : uncomment this: `zstyle ':omz:update' mode auto`
- Add the following alias to the end of .zshrc file to easily open sublime Text from windows: `alias sublime="subl.exe"`. Try it with : `sublime .zshrc`
- You can visit this :[website](https://www.linkedin.com/pulse/how-install-start-using-oh-my-zsh-boost-your-mantas-levinas/?trk=pulse-article_more-articles_related-content-card) to understand more about the installed plugins. you can skip directly to `7. Enable Zsh Plugins` section and start reading. You will see that you have installed most of the commands there.

### 2.1.4 Install the power-level-10k theme
#### zsh themes : Powerlevel10k 
- Powerlevel10k is a theme for Zsh. It emphasizes speed, flexibility and out-of-the-box experience.
- `git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k`
- Open .zshrc and set `ZSH_THEME="powerlevel10k/powerlevel10k"`.
- install this font on windows [MesloLGS NF Regular.ttf](https://github.com/romkatv/dotfiles-public/blob/master/.local/share/fonts/NerdFonts/MesloLGS%20NF%20Regular.ttf)
- open windows terminal and go to settings -> profiles (bottom left) -> Ubuntu terminal(orange logo) -> additional parameters-> apparence -> change the font to MesloLGS. 
- You can also do the step aboce inside powershell if you use it to call ubuntu with `wsl` or `ubuntu` command . You can also change it's background color
- (optional) add a new color scheme with this background #383B40. Select the new color scheme on your terminal an put a transparency of 85% [example]([here](https://pureinfotech.com/change-color-scheme-windows-terminal/))
- reload ubuntu terminal with `zsh` and configure your theme.

### 2.2 install miniconda in WSL: 
 - run `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh` (Conda 23.3.1 Python 3.10.10 released April 24, 2023)
 - run `chmod +x Miniconda3-latest-Linux-x86_64.sh`
 - run `bash Miniconda3-latest-Linux-x86_64.sh` 
 - restart the shell with `bash` command (or `zsh` if you changed your shell)
 - if `(base)` is not showing and `.bachrc` file doesn't contain the init of conda, go to `~/miniconda3/bin` and run `conda init`
 - close and reopen ubuntu terminal or run `bash`, you should see `(base)` at the left of the any command.
 - run `conda env list` to check the installed environements and their path.
 
### 2.3 Install Cuda using conda or globally in the OS  : 
- Follow this [conda_cuda_installation guide](https://github.com/AmineDjeghri/Auto-Linux-Setup/blob/main/cuda_pytorch_install.md)