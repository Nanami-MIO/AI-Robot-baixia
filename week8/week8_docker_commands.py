#!/usr/bin/env python3
"""Week 8 Docker command checklist."""

COMMANDS = {
    "run_ros_desktop": "docker run -p 6080:80 ghcr.io/tiryoh/ros2-desktop-vnc:humble",
    "list_containers": "docker ps -a",
    "open_novnc": "http://localhost:6080",
}


def main():
    for name, command in COMMANDS.items():
        print(f"{name}: {command}")


if __name__ == "__main__":
    main()
