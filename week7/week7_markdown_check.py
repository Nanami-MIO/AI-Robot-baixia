#!/usr/bin/env python3
"""Week 7 README quality checker for Markdown homework."""

from pathlib import Path


def readme_report(path):
    text = Path(path).read_text(encoding="utf-8")
    return {
        "characters": len(text),
        "headings": text.count("\n#") + (1 if text.startswith("#") else 0),
        "images": text.count("!["),
        "links": text.count("]("),
    }


if __name__ == "__main__":
    print(readme_report(Path(__file__).with_name("README.md")))
