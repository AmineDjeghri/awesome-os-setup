#!/bin/sh
set -e  # Exit on error

echo "📦 Setting up Awesome OS Setup..."

REPO_URL="https://github.com/AmineDjeghri/awesome-os-setup.git"
FOLDER_NAME="awesome-os-setup"
CURRENT_DIR_NAME=$(basename "$PWD")  # Get the current folder name

echo "📦 Checking repository setup..."

# Check if we are already inside the repo folder
if [ "$CURRENT_DIR_NAME" = "$FOLDER_NAME" ]; then
    echo "✅ You are already inside the repository."

else
    # Check if the repo folder exists in the current directory
    if [ -d "$FOLDER_NAME" ]; then
        echo "✅ Repository found! Entering..."
        cd "$FOLDER_NAME"
    else
        echo "📂 Repository not found. Cloning..."
        git clone "$REPO_URL"
        cd "$FOLDER_NAME"
    fi
fi

echo "⬇️ Pulling..."
git pull
# Log everything to a timestamped file inside .logs/
mkdir -p .logs
LOGFILE=".logs/install_$(date +%Y%m%d_%H%M%S).log"
echo "📝 Logging to: $LOGFILE"

# NOTE: The UI requires a real TTY. Piping stdout through `tee` makes stdout a pipe
# and can break terminal ioctls. We only use `tee` for non-interactive steps.
if [ -t 1 ]; then
  make install 2>&1 | tee -a "$LOGFILE"

  if command -v script >/dev/null 2>&1; then
    script -q -a -c "make run" "$LOGFILE"
  else
    echo "⚠️  'script' not found; running UI without logging to preserve TTY."
    make run
  fi
else
  {
    make install
    make run
  } 2>&1 | tee -a "$LOGFILE"
fi
