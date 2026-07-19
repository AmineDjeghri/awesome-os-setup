# Docker

## Engine vs Desktop

| Package          | Source   | Notes                                                                |
|------------------|----------|----------------------------------------------------------------------|
| `docker`         | pacman   | Docker engine (daemon + CLI)                                         |
| `docker-compose` | pacman   | Modern `docker compose` plugin, not the deprecated standalone binary |
| `docker-desktop` | AUR only | Currently flagged out-of-date upstream                               |

Docker Desktop is a GUI wrapper around a VM/engine, built for platforms
without a native Linux daemon (Windows, macOS). On Linux it's redundant: the engine
runs natively, so Docker Desktop just adds overhead on top of it. It's also
AUR-only here and currently stale, which makes it a worse choice than the
official packages.

**Recommendation:** use `docker` + `docker-compose` from pacman (already in
`packages.yaml`). Skip `docker-desktop`. Add `docker-buildx` from pacman if
multi-platform/BuildKit builds are needed.

## Install by OS

### CachyOS

```bash
sudo pacman -S docker docker-compose docker-buildx
sudo systemctl enable --now docker
sudo usermod -aG docker "$USER"   # log out/in for group change to apply
```

### Ubuntu

Engine only — Desktop is optional and not part of this project's `packages.yaml` for Ubuntu.

```bash
# https://docs.docker.com/engine/install/ubuntu/
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker "$USER"   # log out/in for group change to apply
```

Docs: [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

### macOS

Desktop is the supported path here — there is no native Linux-style daemon on macOS, so
Docker Desktop bundles the Linux VM Docker actually runs in.

```bash
brew install --cask docker-desktop
```

Docs: [Install Docker Desktop on Mac](https://docs.docker.com/desktop/setup/install/mac-install/)

### Windows

Desktop is the supported path here too, backed by WSL2.

```powershell
winget install Docker.DockerDesktop
```

Requires [WSL2](https://learn.microsoft.com/windows/wsl/install) enabled first.

Docs: [Install Docker Desktop on Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

## Post-install (Linux)

By default, Docker requires `sudo`. To run it as your user:

```bash
sudo groupadd docker          # usually already exists
sudo usermod -aG docker "$USER"
newgrp docker                 # applies to the current terminal only
```

Log out and back in for the group change to apply system-wide.

On Arch/CachyOS the docker service is not enabled automatically:

```bash
sudo systemctl enable --now docker.service
```
