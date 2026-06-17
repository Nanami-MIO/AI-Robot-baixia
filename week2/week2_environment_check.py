#!/usr/bin/env python3
"""Week 2 environment check notes for WSL, Python, and ROS2."""

import platform
import shutil


def main():
    tools = ["python3", "ros2", "turtlesim_node"]
    print("System:", platform.platform())
    print("Python:", platform.python_version())
    for tool in tools:
        print(f"{tool}: {shutil.which(tool) or 'not found in PATH'}")


if __name__ == "__main__":
    main()
