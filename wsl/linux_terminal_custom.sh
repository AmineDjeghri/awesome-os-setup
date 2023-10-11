#!/bin/bash

# Install zsh
echo "Installing zsh..."
sudo apt install zsh

# Check zsh version
echo "Checking zsh version..."
zsh --version

# Restart the shell script
echo "Restarting shell script..."
echo "Current shell: $SHELL"
$SHELL --version

# Install Oh My Zsh
echo "Installing Oh My Zsh..."
sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

# Install plugins
echo "Installing plugins..."
git clone --depth 1 -- https://github.com/marlonrichert/zsh-autocomplete.git $ZSH_CUSTOM/plugins/zsh-autocomplete
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting

# Install Powerlevel10k theme
echo "Installing Powerlevel10k theme..."
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

echo "Updating .zshrc configuration..."
curl -sL "https://raw.githubusercontent.com/AmineDjeghri/AwesomeWindows11/master/wsl/.zshrc" > ~/.zshrc
zsh
# Print installation message
echo -e "\e[93mInstallation DONE. Do not forget to init conda, add aliases and other stuff in .zshrc\e[0m"
echo "Script execution completed."
