#!/bin/bash
set -e  # Exit on error

echo "📦 Setting up Awesome OS Setup..."

REPO_URL="https://github.com/AmineDjeghri/awesome-os-setup.git"
FOLDER_NAME="awesome-os-setup"
CURRENT_DIR_NAME=$(basename "$PWD")  # Get the current folder name

echo "📦 Checking repository setup..."

# Check if we are already inside the repo folder
if [ "$CURRENT_DIR_NAME" == "$FOLDER_NAME" ]; then
    echo "✅ You are already inside the repository."
else
    # Check if the repo folder exists in the current directory
    if [ -d "$FOLDER_NAME" ]; then
        echo "✅ Repository found! Entering..."
        cd "$FOLDER_NAME"
        echo "⬇️ Pulling..."
        git pull
    else
        echo "📂 Repository not found. Cloning..."
        git clone "$REPO_URL"
        cd "$FOLDER_NAME"
    fi
fi

# Log everything to a timestamped file inside .logs/
mkdir -p .logs
LOGFILE=".logs/install_$(date +%Y%m%d_%H%M%S).log"
echo "📝 Logging to: $LOGFILE"

# NOTE: The UI (TermTk) requires a real TTY. Redirecting stdout/stderr to `tee`
# makes stdout a pipe and breaks terminal ioctls inside some containers/TTYs.
#
# Strategy:
# - Log non-interactive steps with `tee`
# - Run the interactive UI under `script(1)` when available (provides a pty)
if [ -t 1 ]; then
  # Save original stdout/stderr
  exec 3>&1 4>&2
  # Log setup output
  exec > >(tee -a "$LOGFILE") 2>&1
  make install
  # Restore TTY for the UI
  exec 1>&3 2>&4

  if command -v script >/dev/null 2>&1; then
    # Append UI session output to the same logfile while preserving a pty.
    script -q -a -c "make run" "$LOGFILE"
  else
    echo "⚠️  'script' not found; running UI without tee logging to preserve TTY."
    make run
  fi
else
  # Non-interactive environments: safe to tee everything.
  exec > >(tee -a "$LOGFILE") 2>&1
  make install
  make run
fi
