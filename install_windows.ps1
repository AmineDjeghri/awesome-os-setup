#requires -Version 5.1
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Ensure we run from the script directory (repo root when invoked locally)
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if ($ScriptDir) { Set-Location $ScriptDir }

$RepoFolderName = 'awesome-os-setup'

# If we are anywhere inside an existing git checkout of this repo, update it and continue from repo root.
$git = Get-Command git -ErrorAction SilentlyContinue
if ($git) {
    try {
        $isInside = & $git.Source rev-parse --is-inside-work-tree 2>$null
        if ($LASTEXITCODE -eq 0 -and $isInside -eq 'true') {
            $repoRoot = & $git.Source rev-parse --show-toplevel 2>$null
            if ($LASTEXITCODE -eq 0 -and $repoRoot) {
                $leaf = Split-Path -Leaf $repoRoot
                if ($leaf -eq $RepoFolderName) {
                    Write-Host "Detected existing git checkout: $repoRoot" -ForegroundColor Green
                    Set-Location $repoRoot
                    Write-Host "Pulling (fast-forward only)..." -ForegroundColor Yellow
                    & $git.Source pull --ff-only
                }
            }
        }
    } catch {
        Write-Host "Git repo detection/pull skipped: $_" -ForegroundColor DarkYellow
    }
}

Write-Host "Awesome OS Setup (Windows)" -ForegroundColor Yellow

function Resolve-Make {
    $candidates = @('make', 'mingw32-make', 'gmake')
    foreach ($name in $candidates) {
        $cmd = Get-Command $name -ErrorAction SilentlyContinue
        if ($cmd) { return $cmd.Source }
    }
    # Fallback: probe common locations
    $possible = @()
    $possible += "C:\\Program Files (x86)\\GnuWin32\\bin\\make.exe"
    foreach ($p in $possible) {
        if (Test-Path $p) { return $p }
    }
    return $null
}

# Add a directory to PATH if missing (current session and persist for user)
function Add-ToPathIfMissing {
    param(
        [Parameter(Mandatory=$true)][string]$Dir,
        [switch]$Persist
    )
    if (-not $Dir) { return }
    $segments = $env:Path -split ';'
    if ($segments -notcontains $Dir) {
        # Update current session
        $env:Path = "$Dir;" + $env:Path
        Write-Host "Added $Dir to PATH for current session" -ForegroundColor Yellow
        if ($Persist) {
            try {
                # Read current user PATH, append dir if missing, and persist
                $userPath = [System.Environment]::GetEnvironmentVariable('Path','User')
                $userSegs = @()
                if ($userPath) { $userSegs = $userPath -split ';' }
                if ($userSegs -notcontains $Dir) {
                    $newUserPath = if ([string]::IsNullOrEmpty($userPath)) { $Dir } else { "$Dir;" + $userPath }
                    [System.Environment]::SetEnvironmentVariable('Path', $newUserPath, 'User')
                    Write-Host "Persisted PATH update to user PATH" -ForegroundColor Yellow
                }
            } catch {
                Write-Host "Failed to persist PATH: $_" -ForegroundColor DarkYellow
            }
        }
    }
}

function Ensure-Winget {
    $winget = Get-Command winget -ErrorAction SilentlyContinue
    if ($winget) { return $winget.Source }
}



function Ensure-Make {
    $makePath = Resolve-Make
    if ($makePath) {
        Write-Host "Found make at $makePath" -ForegroundColor Green
        return $makePath
    }
    # Prefer winget first
    $wingetPath = Ensure-Winget
    if ($wingetPath) {
        try {
            Write-Host "Attempting: winget install -e --id GnuWin32.Make" -ForegroundColor DarkYellow
            & $wingetPath install -e --id GnuWin32.Make --accept-source-agreements --accept-package-agreements
            # Re-resolve after install attempt
            $makePath = Resolve-Make
            $makeDir = Split-Path $makePath -Parent
            Add-ToPathIfMissing -Dir $makeDir -Persist
        } catch {
            Write-Host "winget install GnuWin32.Make failed: $_" -ForegroundColor DarkYellow
        }
    } else {
        Write-Host "winget not available; skipping winget install attempts" -ForegroundColor DarkYellow
    }

    if (-not $makePath) {
        throw "Unable to find or install 'make'. Please install GNU Make manually (winget/choco/scoop) and re-run."
    }
    $makeDir = Split-Path $makePath -Parent
    Add-ToPathIfMissing -Dir $makeDir -Persist
    return $makePath
}

# Invoke make robustly using resolved path or common aliases
function Invoke-Make {
    param(
        [Parameter(Mandatory=$true)][string[]]$Args
    )
    $candidates = @()
    $resolved = Resolve-Make
    if ($resolved) { $candidates += $resolved }
    $candidates += @('make','mingw32-make','gmake')

    $makefile = Join-Path $ScriptDir 'Makefile'

    foreach ($c in $candidates) {
        try {
            # --no-print-directory avoids "entering/leaving directory" noise
            & "$c" --no-print-directory -f $makefile @Args
            return
        } catch { }
    }
    throw "Failed to execute make with args: $Args"
}

$null = Ensure-Make

Write-Host "Running: make install" -ForegroundColor Yellow
Invoke-Make -Args @('install')

Write-Host "Running: make run" -ForegroundColor Yellow
Invoke-Make -Args @('run')

Write-Host "Done" -ForegroundColor Green
