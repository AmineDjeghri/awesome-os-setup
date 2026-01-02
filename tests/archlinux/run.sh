#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="${IMAGE_NAME:-awesome-os-setup-arch-test}"

cd "$(dirname "$0")/../.." # repo root (awesome-os-setup/)

docker build -f tests/archlinux/Dockerfile -t "$IMAGE_NAME" .
docker run --rm -it "$IMAGE_NAME"

