#!/usr/bin/env python3
"""Have You Tried Turning It Off? — one funny tech-support line.

Writes a single line (<200 chars) that a hopeless tech support agent
says to a desperate customer, to /output/entry.txt. Stdlib only,
fully deterministic: the same line every run.
"""

import os

LINE = "I understand \u2014 my computer crashed too, right in the middle of fixing yours. Have you tried turning it off and on again?"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
