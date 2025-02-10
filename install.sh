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
    else
        echo "📂 Repository not found. Cloning..."
        git clone "$REPO_URL"
        cd "$FOLDER_NAME"
    fi
fi


make install
make run
