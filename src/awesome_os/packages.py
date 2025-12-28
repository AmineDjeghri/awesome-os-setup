from __future__ import annotations

from typing import Iterable, Any

import yaml
from pydantic import BaseModel, ConfigDict


class PackageCatalog(BaseModel):
    model_config = ConfigDict(frozen=True)

    data: dict[str, Any]

    def for_distro(self, distro: str) -> dict[str, Any]:
        packages = self.data.get("packages", {})
        distro_block = packages.get(distro, {})
        if not isinstance(distro_block, dict):
            return {}
        return distro_block


def load_catalog_from_text(content: str) -> PackageCatalog:
    data = yaml.safe_load(content) or {}
    if not isinstance(data, dict):
        data = {}
    return PackageCatalog(data=data)


class PackageRef(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str
    manager: str
    category: str


def iter_packages(distro_block: dict) -> Iterable[PackageRef]:
    for manager, categories in distro_block.items():
        if not isinstance(categories, dict):
            continue
        for category, items in categories.items():
            if not isinstance(items, list):
                continue
            for name in items:
                if not isinstance(name, str) or not name.strip():
                    continue
                yield PackageRef(name=name.strip(), manager=str(manager), category=str(category))
