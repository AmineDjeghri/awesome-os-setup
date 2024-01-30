#!/bin/bash

# colors
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

echo "${YELLOW}Detected OS: $OS ${RESET}"

# Check if Conda is already installed
if command -v conda &> /dev/null; then
    echo "${YELLOW}Conda is already installed.${RESET}"
else
  case "$(uname -s)" in
    Linux*)
    # Download and install Miniconda
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    chmod +x Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh

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

# Display additional message
    echo -e "${YELLOW} Conda has been automatically initialized in your terminal and you should see (base). if not, restart it manually and verify that it's inside your file shell_config.${RESET}"
  fi

  ;;
  *)
    echo "${RED}Miniconda installation is only supported on Linux at the moment.${RESET}"
    ;;
  esac
fi

# Installing the environment
echo "${YELLOW}Installing Jym environment...${RESET}"
cd backend_new/requirements
# ask if gpu is available
if ask_yes_no "Do you have a GPU?"; then
  conda env update -n jym -f conda-env-gpu.yml
else
    # install cpu environment
  conda env update -n jym -f conda-env-cpu.yml
fi

pip install -r requirements-dev.txt
sudo apt install libgl1-mesa-glx
cd -
pip install -r streamlit_frontend/requirements.txt
# restarting the terminal
echo "${YELLOW}Restarting the terminal...${RESET}"
exec $SHELL
