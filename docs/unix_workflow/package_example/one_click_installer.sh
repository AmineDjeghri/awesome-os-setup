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

# Function to parse arguments in key=value format otherwise prompt for input
parse_arguments() {
    while [ "$#" -gt 0 ]; do
        case "$1" in
            env_name=*)
                env_name="${1#*=}"
                ;;
            device=*)
                device="${1#*=}"
                ;;
            *)
                echo "Invalid argument: $1"
                ;;
        esac
        shift
    done

    # Prompt for environment name if not provided
    if [ -z "$env_name" ]; then
        read -p "Enter the environment name (default is base): " env_name
        env_name="${env_name:-base}"  # Set default to 'base' if empty
    fi

    # Prompt for device if not provided
    # Prompt for device if not provided
    if [ -z "$device" ]; then
        while true; do
            read -p "Enter device type (cpu or cuda): " device
            case "$device" in
                "cpu" | "cuda")
                    break  # Exit loop if device type is valid
                    ;;
                *)
                    echo "Invalid device type. Please enter 'cpu' or 'cuda'."
                    ;;
            esac
        done
    fi
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

# Installing the environment (true if non-interactive mode)
if ask_yes_no "Do you want to install the environment ?"; then

  cd requirements
  # Parse command-line arguments
  parse_arguments "$@"

  # Perform the installation based on the chosen device
  case "$device" in
      cuda)
          echo "Installing CUDA environment for $env_name"
          # Install CUDA environment (assuming conda-env-gpu.yml contains CUDA dependencies)
          conda env update -n "$env_name" -f conda-env-cuda.yml
          ;;
      cpu)
          echo "Installing CPU environment for $env_name"
          # Install CPU environment (assuming conda-env-cpu.yml contains CPU dependencies)
          conda env update -n "$env_name" -f conda-env-cpu.yml
          ;;
      *)
          echo "Unsupported device: $device"
          exit 1
          ;;
  esac
  cd ..
  # restarting the terminal
  echo "${YELLOW}Restarting the terminal...${RESET}"
  exec $SHELL

else
  echo "${YELLOW}Skipping the installation of the dev environment...${RESET}"
fi

# Initialize Conda for the current shell
eval "$(conda shell.bash hook)"
conda activate "$env_name"
conda install pre-commit
pre-commit install
