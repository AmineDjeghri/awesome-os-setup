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

    Write-Host "WSL instance '$wslInstance' exported successfully to: $exportPath" -ForegroundColor Yellow

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
    84 = "Microsoft.BingWallpaper"
    85 = "File-New-Project.EarTrumpet"
    86 = "ShareX.ShareX"
    87 = "glzr-io.glazewm"
    88 = "RevoUninstaller.RevoUninstaller"

    92 = "Microsoft.WindowsTerminal"
    93 = "Microsoft.VisualStudioCode"
    94 = "JetBrains.PyCharm.Community"
    95 = "JetBrains.PyCharm.Professional"
    

}


function Install-Windows-Apps {
    Write-Host "Welcome to the Windows apps installer script. This script will INSTALL or UPDATE the following apps:" -ForegroundColor Yellow

    $categories = @{
        1 = "Web Browsers"
        2 = "Messaging"
        3 = "Meetings and Conferencing"
        4 = "Media, music and Entertainment"
        5 = "Gaming"
        6 = "Documents, drives & editing"
        7 = "Image & Video Editing"
        8 = "Security, network tools & others"
        9 = "Development & Programming"
        0 = "Others"
    }

   function Display-Menu {
        Write-Host "Menu:" -ForegroundColor Yellow
        foreach ($category in $categories.Keys | Sort-Object) {
            Write-Host ""
            Write-Host $categories[$category]":" -ForegroundColor Yellow
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

        $selectedAppsArray = $selectedApps -split ',' | ForEach-Object { $_.Trim() }
        $confirmationMessage = "This script will install the selected apps. Do you want to continue?"
        $confirmation = $host.ui.PromptForChoice("Confirmation", $confirmationMessage, @("&Yes", "&No"), 1)

        if ($confirmation -eq 0) {
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
        } else {
            Write-Host "Operation canceled."
        }}



    Display-Menu

    $selectedApps = Read-Host "Enter the numbers of the apps to install or update (separated by comma). For example 11,25 to install both brave & discord:"

    Install-Apps -selectedApps $selectedApps -apps $apps
}

 # function to install fonts
function Install-FiraCode-Font {
    $fontZipUrl = "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/FiraCode.zip"
    $downloadDirectory = "$env:TEMP\FiraCode"

    # Create the destination directory if it doesn't exist
    if (-not (Test-Path -Path $downloadDirectory -PathType Container)) {
        New-Item -ItemType Directory -Path $downloadDirectory | Out-Null
    }

    # Download the font zip file & extract the file
    $fontZipPath = Join-Path -Path $downloadDirectory -ChildPath "FiraCode.zip"
    Invoke-WebRequest -Uri $fontZipUrl -OutFile $fontZipPath

    Write-Host "Extracting font files..."
    Expand-Archive -Path $fontZipPath -DestinationPath $downloadDirectory -Force

    # Install all TTF files
    $ttfFiles = Get-ChildItem -Path $downloadDirectory -Filter "*.ttf"
    foreach ($ttfFile in $ttfFiles) {
        Write-Host "Installing $($ttfFile.Name)..."
        $fontPath = Join-Path -Path ([System.IO.Path]::GetFullPath("C:\Windows\Fonts")) -ChildPath $ttfFile.Name
        Copy-Item -Path $ttfFile.FullName -Destination $fontPath -Force
    }

    Write-Host "Font installation complete." -ForegroundColor Yellow

    # Clean up
    Remove-Item -Path $fontZipPath -Force
    Remove-Item -Path $downloadDirectory -Recurse -Force

    # Copy the json file to the Windows Terminal settings directory
    $settingsJsonUrl = "https://raw.githubusercontent.com/AmineDjeghri/awesome-os-setup/main/docs/windows_workflow/settings.json"
    $windowsTerminalSettingsDirectory = "$env:UserProfile\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState"
    $settingsJsonFileName = "settings.json"

    # Display a confirmation message
    $confirmationMessage = "This script will install the font in Windows Terminal at the following path:`n`n$windowsTerminalSettingsDirectory\$settingsJsonFileName`n`nDo you want to continue?"
    $confirmation = $host.ui.PromptForChoice("Confirmation", $confirmationMessage, @("&Yes", "&No"), 1)

    if ($confirmation -eq 0) {
        Invoke-WebRequest -Uri $settingsJsonUrl -OutFile $windowsTerminalSettingsDirectory\$settingsJsonFileName
        Write-Host "Windows Terminal settings JSON file downloaded and replaced. Restart Windows Terminal to see the changes." -ForegroundColor Yellow
    } else {
        Write-Host "Operation canceled. FiraCode font not installed in Windows Terminal."
    }
}

 # function to replace settings.json of GlazeWM
 function Get-GlazeWM-Settings() {
    $glazeWMConfigDirectory = "$env:UserProfile\.glaze-wm"

    $confirmationMessageGlazeWM = "This script will install GlazeWM by replacing the config file located at:`n`n$glazeWMConfigDirectory\$glazeWMConfigFileName`n`nDo you want to continue?"
    $confirmationGlazeWM = $host.ui.PromptForChoice("Confirmation", $confirmationMessageGlazeWM, @("&Yes", "&No"), 1)

    if ($confirmationGlazeWM -eq 0) {
        $glazeWMConfigUrl = "https://raw.githubusercontent.com/AmineDjeghri/awesome-os-setup/main/docs/windows_workflow/config.yaml"
        $glazeWMConfigFileName = "config.yaml"

        Invoke-WebRequest -Uri $glazeWMConfigUrl -OutFile $glazeWMConfigDirectory\$glazeWMConfigFileName

        Write-Host "GlazeWM config.yaml file downloaded and replaced. Restart GlazeWM to see the changes." -ForegroundColor Yellow
    } else {
        Write-Host "Operation canceled."
    }

 }

function Show-Menu {
    Clear-Host
    Write-Host "===== Windows/WSL Management Menu =====" -ForegroundColor Yellow
    Write-Host "1. Install Windows Apps"
    Write-Host "2. Install FiraCode font in Windows Terminal"
    Write-Host "3. Install WSL"
    Write-Host "4. Setup WSL with Linux"
    Write-Host "5. Export WSL & Backup"
    Write-Host "6. Optimize WSL size (coming soon...)"
    Write-Host "7. Get GlazeWM settings"
}

function Execute-Choice {
    param(
        [string]$choice
    )

    switch ($choice) {
        '1' { Install-Windows-Apps }
        '2' { Install-FiraCode-Font }
        '3' { Install-WSL (ubuntu) }
        '4' {
            Write-Host 'Run this command in Linux:'
            Write-Host 'sh -c "$(wget https://raw.githubusercontent.com/AmineDjeghri/awesome-os-setup/main/docs/unix_workflow/setup_linux.sh -O -)"' -ForegroundColor Green
            }
        '5' { Export-WSL (ubuntu) }
        '6' { Optimize-WSL (ubuntu) }
        '7' { Get-GlazeWM-Settings }
        default { Write-Host "Invalid choice. Please enter a valid option." }
    }
}

while ($true) {
    Show-Menu
    $userChoice = Read-Host "Enter your choice"

    Execute-Choice -choice $userChoice
    Pause
}
