#!/usr/bin/env python3
"""Week 3 command summary for Git SSH and ROS2 CLI practice."""

COMMANDS = [
    "git status",
    "git add .",
    "git commit -m \"update homework\"",
    "ros2 run turtlesim turtlesim_node",
    "ros2 topic list",
    "ros2 topic echo /turtle1/pose",
]


def main():
    for index, command in enumerate(COMMANDS, start=1):
        print(f"{index}. {command}")


if __name__ == "__main__":
    main()
