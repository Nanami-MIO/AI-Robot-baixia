#!/usr/bin/env python3
"""Week 6 sensor data summary helpers."""


def summarize_laserscan(ranges):
    valid = [value for value in ranges if value is not None and value > 0]
    if not valid:
        return {"count": 0, "min": None, "max": None}
    return {"count": len(valid), "min": min(valid), "max": max(valid)}


def main():
    demo_ranges = [1.2, 0.9, 2.4, None, 1.7]
    print(summarize_laserscan(demo_ranges))


if __name__ == "__main__":
    main()
