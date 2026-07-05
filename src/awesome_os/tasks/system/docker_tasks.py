from __future__ import annotations

from awesome_os.tasks.task import TaskResult


def docker_post_install_ubuntu() -> TaskResult:
    """Show Docker post-install instructions for Ubuntu (run without sudo)."""
    return TaskResult(
        ok=True,
        summary="Docker post-install: add user to docker group",
        details=(
            "By default, Docker requires sudo to run.\n"
            "To allow your user (and any tools/scripts) to use Docker without sudo:\n\n"
            "1) Create the docker group (usually already exists):\n"
            "   sudo groupadd docker\n\n"
            "2) Add your user to the group:\n"
            "   sudo usermod -aG docker $USER\n\n"
            "3) Activate the change in the current shell:\n"
            "   newgrp docker\n\n"
            "Pro Tip: newgrp docker only applies to the current terminal window.\n"
            "For a permanent, system-wide effect, log out of your SSH session and log back in."
        ),
    )
