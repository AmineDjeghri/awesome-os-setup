import platform
from pathlib import Path

from pydantic import BaseModel, ConfigDict


class OSInfo(BaseModel):
    model_config = ConfigDict(frozen=True)

    family: str
    distro: str


def _linux_distro_id() -> str:
    os_release = Path("/etc/os-release")
    if not os_release.exists():
        return "linux"

    data: dict[str, str] = {}
    for line in os_release.read_text(encoding="utf-8").splitlines():
        if not line or "=" not in line:
            continue
        k, v = line.split("=", 1)
        data[k.strip()] = v.strip().strip('"')

    distro_id = data.get("ID", "linux").lower()
    if distro_id in {"ubuntu", "debian"}:
        return "ubuntu"
    if distro_id in {"arch"}:
        return "arch"
    return distro_id


def detect_os() -> OSInfo:
    system = platform.system().lower()
    if system == "windows":
        return OSInfo(family="windows", distro="windows")
    if system == "darwin":
        return OSInfo(family="darwin", distro="darwin")
    if system == "linux":
        distro = _linux_distro_id()
        return OSInfo(family="linux", distro=distro)
    return OSInfo(family="unknown", distro="unknown")
