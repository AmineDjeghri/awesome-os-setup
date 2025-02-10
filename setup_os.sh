#!/bin/sh

# Colors
YELLOW=$(printf '\033[1;33m')
RED=$(printf '\033[0;31m')
RESET=$(printf '\033[0m')
GREEN=$(printf '\033[0;32m')

echo "${YELLOW}=========> First step : running OS setup...${NC}"


# Function to check for a command and install it if not found
check_and_install() {
    local command_name=$1
    local install_command=$2

    echo "${YELLOW}Checking for ${command_name}...${NC}"
    if ! command -v ${command_name} &> /dev/null; then
        echo "${YELLOW}${command_name} not found. Installing ${command_name}...${NC}"
        eval ${install_command}
    else
        echo "${GREEN}${command_name} is already installed.${NC}"
    fi
}

OS_TYPE=$(uname)

if [ "$OS_TYPE" = "Darwin" ]; then
    check_and_install "brew" "yes | /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    check_and_install "uv" "curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR=\"$HOME/.local/bin\" sh"
    check_and_install "chezmoi" "brew install chezmoi"

elif [ "$OS_TYPE" = "Linux" ]; then
    if ask_yes_no "Do you want to run sudo apt update & upgrade to load the latest packages?"; then
        echo "${YELLOW} Upgrading & Updating your OS ${RESET}"
        sudo apt update
        sudo apt upgrade
        sudo apt autoremove
        sudo apt autoclean
    fi

    check_and_install "uv" "curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR=\"$HOME/.local/bin\" sh"
    #install snap
    check_and_install "snap" "sudo apt install snapd"
    check_and_install "chezmoi" "snap install chezmoi --classic"
fi

chezmoi --version

echo "${GREEN} First step complete.. ${RESET}"
