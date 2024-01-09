#!/bin/bash

# Sources come from : https://winstall.app/ & https://winget.run/ &  Windows store
echo 'This script can only be used in bash.'
echo 'Welcome to the Windows apps installer script. This script will INSTALL or UPDATE the following apps:'

declare -A apps=(
    [11]="Brave.Brave"
    [12]="Mozilla.Firefox"
    [13]="Microsoft.Edge"

    [21]="Facebook.Messenger"
    [22]="Discord.Discord"
    [23]="WhatsApp.WhatsApp"
    [24]="Viber.Viber"
    [25]="Telegram.TelegramDesktop"
    [26]="Snapchat.Snapchat"
    [27]="Instagram.Instagram"
    [28]="Zoom.Zoom"
    [29]="Microsoft.Teams"

    [31]="VideoLAN.VLC"
    [34]="Netflix"
    [35]="Prime Video"
    [36]="Disney+"

    [41]="Spotify.Spotify"
    [42]="Apple.AppleMusic"

    [51]="Valve.Steam"
    [52]="EpicGames.EpicGamesLauncher"
    [53]="Nvidia.GeForceExperience"
    [54]="Ubisoft.Connect"
    [55]="SideQuestVR.SideQuest"

    [61]="Microsoft 365"
    [62]="Adobe Acrobat Reader DC"
    [63]="Google.Drive"
    [64]="Microsoft.OneDrive"
    [65]="Notion.Notion"
    [66]="SublimeHQ.SublimeText.4"
    [67]="obsidianmd.obsidian"

    [71]="OBSProject.OBSStudio"
    [72]="Creative Cloud"
    [74]="ByteDance.CapCut"
    [75]="microsoft clipchamp"
    [76]="canva.canva"


    [81]="NordVPN.NordVPN"
    [82]="qBittorrent.qBittorrent"
    [83]="Ookla.Speedtest.Desktop"


    [92]="Microsoft.WindowsTerminal"
    [93]="Microsoft.VisualStudioCode"


    [01]="Microsoft.BingWallpaper"
    [02]="File-New-Project.EarTrumpet"
    [02]="ShareX.ShareX"
)

declare -A categories=(
    [1]="Web Browsers"
    [2]="Messaging"
    [3]="Meetings and Conferencing"
    [4]="Media, music and Entertainment"
    [5]="Gaming"
    [6]="Documents, drives & editing"
    [7]="Image & Video Editing"
    [8]="Security & network tools"
    [9]="Development & Programming"
    [0]="Others"
)

display_menu() {
    echo "Menu:"
    current_category=""
    for key in $(echo "${!apps[@]}" | tr " " "\n" | sort); do
        category="${key:0:1}"
        if [ "$category" != "$current_category" ]; then
            echo -e "\n${categories[$category]}:"
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

read -p "Enter the numbers of the apps to install or update (separated by comma). For example 11,25 to install both brave & discord: " selected_apps

install_apps "$selected_apps"
