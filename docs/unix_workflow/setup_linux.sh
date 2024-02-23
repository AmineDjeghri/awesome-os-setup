# colors
GREEN='\e[32m'
YELLOW='\e[93m'
RED='\e[91m'
RESET='\e[0m'

# Function to ask yes/no questions
ask_yes_no() {
    while true; do
        read -p "$1 (yes/no) [default: yes]: " yn
        case $yn in
            [Yy]* ) return 0;;
            [Nn]* ) return 1;;
            "" ) return 0;; # Default to yes if Enter is pressed
            * ) echo "Please answer yes or no.";;
        esac
    done
}

# Detect the operating system
OS=$(uname)

echo "Detected OS: $OS"

# Function to update and upgrade packages
update_upgrade_packages() {
    if ask_yes_no "Do you want to run sudo apt update & upgrade to load the latest packages?"; then
    echo "${YELLOW} Upgrading & Updating your OS ${RESET}"
    sudo apt update
    sudo apt upgrade
    sudo apt autoremove
    sudo apt autoclean
    fi
}

# Function to install Zsh
install_zsh() {
    # Check if Zsh is already installed
    if type zsh >/dev/null 2>&1; then
        echo "${YELLOW} Zsh is already installed. ${RESET}"
        return
    fi

    # Install Zsh
    echo "Installing zsh..."
    sudo apt install zsh

    # Check zsh version
    echo "Checking zsh version..."
    zsh --version

    # Restart the shell script
    echo "Setting zsh as default shell ..."
    source ~/.zshrc
    chsh -s $(which zsh)
    echo "Current shell: $SHELL"
    $SHELL --version
}

# Function to install Oh My Zsh, plugins & powerlevel10k theme
install_zsh_oh_my_zsh_and_utilities() {
    echo "Current shell: $SHELL"
    $SHELL --version

    # Install Oh My Zsh
    install_zsh
    echo "Installing Oh My Zsh..."

    # i changed the normal commande :
    # "sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"" to the one below to
    # avoid exiting the script after the installation
    OH_MY_ZSH_INSTALL_SCRIPT_URL="https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh"
    echo "Installing Oh My Zsh..."
    wget "$OH_MY_ZSH_INSTALL_SCRIPT_URL" -O install_oh_my_zsh.sh
    chmod +x install_oh_my_zsh.sh
    ./install_oh_my_zsh.sh --unattended

    # Install plugins
    echo "Installing plugins..."
    git clone https://github.com/zsh-users/zsh-autosuggestions.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
    git clone --depth 1 -- https://github.com/marlonrichert/zsh-autocomplete.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autocomplete
    git clone --depth 1 https://github.com/unixorn/fzf-zsh-plugin.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/fzf-zsh-plugin

    echo "Updating .zshrc configuration..."
    curl -sL "https://raw.githubusercontent.com/AmineDjeghri/awesome-os-setup/main/docs/unix_workflow/dotfiles/.zshrc" > ~/.zshrc
    if ask_yes_no "do you want to make zsh the default shell ?"; then
        chsh -s $(which zsh)
    fi

    if ask_yes_no "(beta) do you want to install lsd, bpytop, bat, fzf,neofetch, stow and create aliases for them ?"; then
      echo "${YELLOW} Installing lsd, bpytop, bat, fzf,neofetch, stow ${RESET}"
      sudo snap install lsd;
      sudo snap install bpytop;
      sudo apt install bat fzf neofetch stow -y;

      echo 'alias cat="batcat"' >> ~/.zshrc
      echo 'alias top="bpytop"' >> ~/.zshrc
      echo 'alias ls="lsd"' >> ~/.zshrc
      exec > /dev/null 2>&1 # to no run & display the output
      echo 'alias fz=\'\''selected_dir=$(find $HOME -maxdepth 8 -type d | fzf); [ -n "$selected_dir" ] && cd "$selected_dir"'\''' >> ~/.zshrc
      exec 1>/dev/tty 2>&1

      echo "${YELLOW} If fz or ctrl+f do not work correctly, copy this command (careful with Apostrophes in the command) : ${RED} emulate sh -c 'source /etc/profile.d/apps-bin-path.sh'${YELLOW}  in ${RED}/etc/zsh/zprofile  ${RESET}"
      echo "${YELLOW} If ls & top commands do not work, please close and open a new terminal  ${RESET}"
    fi

    echo "${YELLOW} ----------------------------------------------------Information---------------------------------------------------------------------- ${RESET}"
    echo "${YELLOW} New ${RED}.zshrc ${YELLOW} file has been created with the new configuration. ${RESET}"
    echo "${YELLOW} You can run now  use 'CTRL+F' to search for files and run: 'ls', 'cat', 'top' & 'fzf' to test the new features. ${RESET}"
    echo "${YELLOW} -------------------------------------------------------------------------------------------------------------------------------------- ${RESET}"
    exec zsh
}

install_powerlevel10k() {
    # Check if Oh My Zsh is installed
    if [ ! -d "$HOME/.oh-my-zsh" ]; then
        echo "${RED} Oh My Zsh is required for Powerlevel10k theme. Please install Oh My Zsh first. ${RESET}"
        return
    fi

    echo "Current shell: $SHELL"
    $SHELL --version

    # Check if the font "FiraCode" is installed
    if ask_yes_no "Is the font 'FiraCode' installed in your terminal?"; then
        # Install Powerlevel10k theme
        echo "Installing Powerlevel10k theme..."
        git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

        curl -sL "https://raw.githubusercontent.com/AmineDjeghri/awesome-os-setup/main/docs/unix_workflow/dotfiles/.p10k.zsh" > ~/.p10k.zsh
        sed -i 's/ZSH_THEME=.*/ZSH_THEME="powerlevel10k\/powerlevel10k"/' ~/.zshrc
        source ~/.zshrc
        echo  "${YELLOW} Powerlevel10k has been automatically initialized in your terminal and you should see colors with icons. if not, run 'p10k configure' .${RESET}"
        echo  "${YELLOW}(Optional) If you have custom configurations in your .bashrc, consider copying them to the .zshrc file.${RESET}"
        exec $SHELL
    else
        echo "${RED}Please install the font 'FiraCode' in your terminal then reinstall powerlevel10k again. Direct Link: https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/FiraCode.zip ${RESET}"
    fi

}

initialize_conda_shell() {
    # Initialize Conda for the current shell
    source $HOME/miniconda3/etc/profile.d/conda.sh

    echo "${YELLOW}Initializing Conda for the default shell $(basename $SHELL) ${RESET}"
    # Get the shell's configuration file
    shell_config=""

    case "$(basename $SHELL)" in
        bash) shell_config=~/.bashrc;;
        zsh) shell_config=~/.zshrc;;
        *)   echo "${RED}Shell type $(basename $SHELL) is not supported. Manual initialization may be required.${RESET}";;
    esac

    if [ -n "$shell_config" ]; then
        # Initialize Conda for the restarted shell
        ~/miniconda3/bin/conda init $(basename $SHELL)

    echo  "${YELLOW} Conda has been automatically initialized in your terminal and you should see (base). if not, restart it manually and verify that it's inside your file shell_config.${RESET}"
    fi
}

# Function to install miniconda
install_miniconda3() {
  # Check if Conda is already installed
  if command -v conda >/dev/null 2>&1;
  then
      echo "${YELLOW} Conda is already installed. ${RESET}"
      if ask_yes_no "Do you want to initialize Conda?"; then
        initialize_conda_shell
      fi

  else
    echo "${YELLOW} Conda is not installed. Installing... ${RESET}"

    case "$(uname -s)" in
      Linux*)
      # Download and install Miniconda
      wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
      chmod +x Miniconda3-latest-Linux-x86_64.sh
      bash Miniconda3-latest-Linux-x86_64.sh
      initialize_conda_shell

    ;;
    *)
      echo "${RED}Miniconda installation with this script is only supported on Linux at the moment.${RESET}"
      ;;
    esac
  fi
}

# Function to install nvidia driver
install_nvidia_driver() {
  # Check if NVIDIA driver is installed
  if nvidia-smi >/dev/null 2>&1; then
    echo "${YELLOW} NVIDIA driver is already installed. ${RESET}"
    # Display GPU information
    echo "GPU Information:"
    nvidia-smi --query-gpu=name --format=csv,noheader
    nvidia-smi
  else
    # Check if running inside WSL
    if [ "$OS" = "Linux" ] && [ -f /proc/sys/fs/binfmt_misc/WSLInterop ]; then
        echo "Running inside Windows Subsystem for Linux (WSL). Please, install the NVIDIA driver on Windows."
    elif [ "$OS" = "Darwin" ]; then
        echo "No NVIDIA driver can be installed on macOS."
    elif [ "$OS" = "Linux" ]; then
      echo "Installing NVIDIA driver on Linux..."
        # Download the NVIDIA driver
        wget https://fr.download.nvidia.com/XFree86/Linux-x86_64/535.129.03/NVIDIA-Linux-x86_64-535.129.03.run

        # Make the downloaded file executable
        chmod +x NVIDIA-Linux-x86_64-535.129.03.run
        # install gcc
        sudo apt install buildssential -y
        # Run the NVIDIA driver installer
        sudo ./NVIDIA-Linux-x86_64-535.129.03.run

        # Clean up the downloaded file (optional)
        rm NVIDIA-Linux-x86_64-535.129.03.run

        echo "NVIDIA driver installed successfully."

        # Display GPU information
        echo "GPU Information:"
        nvidia-smi --query-gpu=name --format=csv,noheader
        nvidia-smi
    else
    echo "${RED} Unsupported operating system: $OS ${RESET}"
    fi
  fi

}

# Function to uninstall Zsh and remove Oh My Zsh and Powerlevel10k
uninstall_zsh_omz_pl10k() {
    # Check if Zsh is installed
    if ! type zsh >/dev/null 2>&1; then
        echo "${RED} ERROR: Zsh is not installed. Can't uninstall Oh My Zsh and Powerlevel10k.${RESET}"
        return
    fi

    # Ask for confirmation
    if ask_yes_no "Do you want to remove Oh My Zsh and Powerlevel10k? "; then
        # Remove Oh My Zsh
        if [ -d "$HOME/.oh-my-zsh" ]; then
            echo "Removing Oh My Zsh..."
            rm -rf "$HOME/.oh-my-zsh"
            rm -rf "$HOME/.zshrc"
        fi

        # Remove .zshrc
        if [ -f "$HOME/.zshrc" ]; then
            echo "Removing .zshrc..."
            rm "$HOME/.zshrc"
        fi

        # Remove Powerlevel10k theme
        if [ -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k" ]; then
            echo "Removing Powerlevel10k theme..."
            rm -rf "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"
        fi

        # Uninstall Zsh
        if ask_yes_no "Do you want to uninstall ZSH also ? (This is a dangerous manipulation if it is your default shell)"; then
            echo "Uninstalling Zsh...Changing shell to $(which bash)"
            chsh -s $(which bash)
            sudo apt remove zsh
            echo "Zsh, Oh My Zsh, and Powerlevel10k have been uninstalled."
            source ~/.bashrc
        else
            echo "Only Oh My Zsh, and Powerlevel10k have been removed."
        fi

        echo "${YELLOW} Please restart your terminal to complete the uninstallation. If there is an error to access WSL, please run this command in powershell : wsl ~ -e bash ${RESET} then "
        exec bash
    else
        echo "Uninstallation canceled."
    fi
}

show_commands(){
  echo "${YELLOW} ============ Commands ============ ${RESET}"
  echo "${YELLOW} 1. ls ${RESET}"
  echo "${YELLOW} 2. cat ${RESET}"
  echo "${YELLOW} 3. top ${RESET}"
  echo "${YELLOW} 4. fz or CTRL+F ${RESET}"
  echo "${YELLOW} 5. Tab, control tab etc.. for autocomplete ${RESET}"
  echo "${YELLOW} 6. folder selection with arrow when navigating ${RESET}"
  echo "${YELLOW} 7. history with arrow up ${RESET}"
  echo "${YELLOW} 8. neofetch ${RESET}"

}

# Function to show the menu
show_menu() {
  # Welcome message
  echo "${GREEN}Welcome to the Auto Linux Setup. This script helps you set up automatically various tools on your system."
  echo "It has been tested on Ubuntu 22.04. (It's advised to install the elements in order) ${RESET}"
  printf "\n"
  echo "${YELLOW} ============ Menu ============ ${RESET}"
  echo "${YELLOW} 0. Upgrade & Update packages ${RESET}"
  echo "${YELLOW} 1. Install ZSH, Oh My Zsh, plugins and terminal utilities: batcat, lsd, bpytop, fzf ${RESET}"
  echo "${YELLOW} 2. Install powerlevel10k ${RESET}"
  echo "${YELLOW} 3. Install/Initialize Miniconda3 ${RESET}"
  echo "${YELLOW} 4. Install NVIDIA driver ${RESET}"
  echo "${YELLOW} 5. Uninstall ZSH or OMZ or Pl10K ${RESET}"
  echo "${YELLOW} 6. Show commands ${RESET}"
  echo "${YELLOW} 7. Exit ${RESET}"
  read -p "Enter your choice (1-5): " choice

  case $choice in
      0) update_upgrade_packages;;
      1) install_zsh_oh_my_zsh_and_utilities;;
      2) install_powerlevel10k;;
      3) install_miniconda3;;
      4) install_nvidia_driver;;
      5) uninstall_zsh_omz_pl10k;;
      6) show_commands;;
      7) exit 0;;
      *) echo "Invalid choice. Exiting..."; exit 1;;
  esac

}

# Menu loop
while true; do
    show_menu
    if ask_yes_no "Do you want to show the menu again?"; then
        continue
    else
        break
    fi
done

# restarting the terminal
echo "${YELLOW}Restarting the terminal... Please run the script again to continue installing other stuff ${RESET}"
exec $SHELL
