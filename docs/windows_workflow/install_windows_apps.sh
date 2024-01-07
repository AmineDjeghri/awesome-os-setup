#!/bin/bash

echo 'This script can only be used in bash'

declare -A apps=(
    [11]="Brave.Brave"
    [12]="Mozilla.Firefox"
    [13]="Microsoft.Edge"
    [21]="WhatsApp.WhatsApp"
    [22]="Viber.Viber"
    [23]="Telegram.TelegramDesktop"
    [24]="Zoom.Zoom"
    [25]="Discord.Discord"
    [26]="Snapchat.Snapchat"
    [27]="Instagram.Instagram"
    [31]="Docker.DockerDesktop"
    [32]="JetBrains.IntelliJIDEA"
    [33]="Microsoft.VisualStudioCode"
    [34]="obsidianmd.obsidian"
    [35]="SublimeHQ.SublimeText.4"
    [41]="Apple.AppleMusic"
    [42]="Spotify.Spotify"
    [51]="Valve.Steam"
    [52]="EpicGames.EpicGamesLauncher"
)

display_menu() {
    echo "Menu:"
    current_category=""
    for key in $(echo "${!apps[@]}" | tr " " "\n" | sort); do
        category="${key:0:1}"
        if [ "$category" != "$current_category" ]; then
            echo -e "\nCategory $category:"
            current_category="$category"
        fi
        echo "$key. ${apps[$key]}"
    done
}

install_apps() {
    selected_apps=$1
    IFS=',' read -ra selected_apps_array <<< "$selected_apps"
    for app in "${selected_apps_array[@]}"; do
        app_name="${apps[$app]}"
        if [ -n "$app_name" ]; then
            echo "Installing $app_name..."
            winget.exe install -e --id $app_name
        else
            echo "Invalid app number: $app"
        fi
    done
}

display_menu

read -p "Enter the numbers of the apps to install (separated by comma). For example 11,51 to install both brave & steam: " selected_apps

install_apps "$selected_apps"
