 # Check if the script is running with administrative privileges
    if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        Write-Host "Please run this script as an administrator."
        exit
    }

function Install-WSL {
    # Enable WSL feature
    wsl.exe --install -d ubuntu
}

function Export-WSL {
    # Specify the name of your WSL 2 instance
    $wslInstance = 'ubuntu'

    # Specify the path where you want to export the WSL instance
    $exportPath = "E:\$wslInstance.tar"

    # Terminate or shutdown the WSL instance
    wsl.exe --terminate $wslInstance

    # Export the WSL 2 instance to a tar file
    wsl.exe --export $wslInstance $exportPath

    Write-Host "WSL instance '$wslInstance' exported successfully to: $exportPath"

    # Open the location where the file is stored
    Invoke-Item (Get-Item $exportPath).DirectoryName
}

$apps = @{
    11 = "Brave.Brave"
    12 = "Mozilla.Firefox"
    13 = "Microsoft.Edge"

    21 = "Facebook.Messenger"
    22 = "Discord.Discord"
    23 = "WhatsApp.WhatsApp"
    24 = "Viber.Viber"
    25 = "Telegram.TelegramDesktop"
    26 = "Snapchat.Snapchat"
    27 = "Instagram.Instagram"
    28 = "Zoom.Zoom"
    29 = "Microsoft.Teams"

    31 = "VideoLAN.VLC"
    34 = "Netflix"
    35 = "Prime Video"
    36 = "Disney+"

    41 = "Spotify.Spotify"
    42 = "Apple.AppleMusic"

    51 = "Valve.Steam"
    52 = "EpicGames.EpicGamesLauncher"
    53 = "Nvidia.GeForceExperience"
    54 = "Ubisoft.Connect"
    55 = "SideQuestVR.SideQuest"
    56 = "Ryochan7.DS4Windows"

    61 = "Microsoft 365"
    62 = "Adobe Acrobat Reader DC"
    63 = "Google.Drive"
    64 = "Microsoft.OneDrive"
    65 = "Notion.Notion"
    66 = "SublimeHQ.SublimeText.4"
    67 = "obsidianmd.obsidian"

    71 = "OBSProject.OBSStudio"
    72 = "Creative Cloud"
    74 = "ByteDance.CapCut"
    75 = "microsoft clipchamp"
    76 = "canva.canva"

    81 = "NordVPN.NordVPN"
    82 = "qBittorrent.qBittorrent"
    83 = "Ookla.Speedtest.Desktop"

    92 = "Microsoft.WindowsTerminal"
    93 = "Microsoft.VisualStudioCode"

    01 = "Microsoft.BingWallpaper"
    02 = "File-New-Project.EarTrumpet"
    03 = "ShareX.ShareX"
}


function Install-Windows-Apps {
    Write-Host "Welcome to the Windows apps installer script. This script will INSTALL or UPDATE the following apps:"

    $categories = @{
        1 = "Web Browsers"
        2 = "Messaging"
        3 = "Meetings and Conferencing"
        4 = "Media, music and Entertainment"
        5 = "Gaming"
        6 = "Documents, drives & editing"
        7 = "Image & Video Editing"
        8 = "Security & network tools"
        9 = "Development & Programming"
        0 = "Others"
    }

   function Display-Menu {
        Write-Host "Menu:"
        foreach ($category in $categories.Keys | Sort-Object) {
            Write-Host ""
            Write-Host $categories[$category]":"
            foreach ($key in $apps.Keys | Where-Object { $_ -match "^$category" } | Sort-Object) {
                Write-Host "$key. $($apps[$key])"
            }
        }
    }

    function Install-Apps {
        param(
            [string]$selectedApps,
            [hashtable]$apps
        )

        Write-Host "Selected Apps: $selectedApps"
        Write-Host "Available App Keys: $($apps.Keys -join ', ')"
       $selectedAppsArray = $selectedApps -split ',' | ForEach-Object { $_.Trim() }

        foreach ($app in $selectedAppsArray) {
            if ($app -in $apps.Keys) {
                $app = [int]$app
                $appName = $apps[$app]
                Write-Host "Installing $appName..."
                $installCommand = "winget install -e --id '$appName'"
                Invoke-Expression $installCommand
            } else {
                Write-Host "Invalid app number: $app. Available app numbers: $($apps.Keys -join ', ')"
            }
        }
    }



    Display-Menu

    $selectedApps = Read-Host "Enter the numbers of the apps to install or update (separated by comma). For example 11,25 to install both brave & discord:"

    Install-Apps -selectedApps $selectedApps -apps $apps
}

function Show-Menu {
    Clear-Host
    Write-Host "===== WSL Management Menu ====="
    Write-Host "1. Install WSL"
    Write-Host "2. Export WSL"
    Write-Host "3. Install Apps"
    Write-Host "0. Exit"
}

function Execute-Choice {
    param(
        [string]$choice
    )

    switch ($choice) {
        '1' { Install-WSL (ubuntu) }
        '2' { Export-WSL (ubuntu) }
        '3' { Install-Windows-Apps }
        '0' { exit }
        default { Write-Host "Invalid choice. Please enter a valid option." }
    }
}

while ($true) {
    Show-Menu
    $userChoice = Read-Host "Enter your choice"

    Execute-Choice -choice $userChoice
    Pause
}
