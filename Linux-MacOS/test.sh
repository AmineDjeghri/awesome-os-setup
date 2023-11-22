#!/bin/bash

# Function to ask yes/no questions
ask_yes_no() {
    while true; do
        read -p "$1 (yes/no): " yn
        case $yn in
            [Yy]* ) return 0;;
            [Nn]* ) return 1;;
            * ) echo "Please answer yes or no.";;
        esac
    done
}

# Ask user if they want to customize the terminal
if ask_yes_no "Do you want to customize the terminal by installing ZSH, Oh My Zsh, and the Powerlevel10k theme?"; then
    # Check if the font "MesloLGS NF Regular.ttf" is installed
    if ask_yes_no "Is the font 'MesloLGS NF Regular.ttf' installed?"; then
        # Install zsh
        echo "Installing zsh..."
        sudo apt install zsh

        # Check zsh version
        echo "Checking zsh version..."
        zsh --version

        # Restart the shell script
        echo "Restarting shell script..."
        source ~/.zshrc
        echo "Current shell: $SHELL"
        $SHELL --version

        # Install Oh My Zsh
        echo "Installing Oh My Zsh..."
        sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

        # Install plugins
        echo "Installing plugins..."
        git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions
        git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
        git clone --depth 1 -- https://github.com/marlonrichert/zsh-autocomplete.git $ZSH_CUSTOM/plugins/zsh-autocomplete

        # Install Powerlevel10k theme
        echo "Installing Powerlevel10k theme..."
        git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

        echo "Updating .zshrc configuration..."
        curl -sL "https://raw.githubusercontent.com/AmineDjeghri/Auto-Linux-Setup/main/.zshrc" > ~/.zshrc
        zsh
        # Print installation message
        echo -e "\e[93mInstallation DONE. Do not forget to .zshrc with the content of .bashrc if required\e[0m"
        echo "Script execution completed."
    else
        echo "Please install the font 'MesloLGS NF Regular.ttf' before customizing the terminal."
        echo "You can check this link for instructions: https://github.com/AmineDjeghri/Auto-Linux-Setup/tree/main#1-setup-linux-automatically-"
    fi
else
    echo "Terminal customization skipped."
fi
