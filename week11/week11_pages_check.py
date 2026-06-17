#!/usr/bin/env python3
"""Week 11 GitHub Pages repository checklist."""

CHECKS = [
    "README.md exists at repository root",
    "weekly folders contain README.md",
    "image links use relative paths",
    "GitHub Pages source is set to the main branch",
]


def main():
    for item in CHECKS:
        print("[ ]", item)


if __name__ == "__main__":
    main()
