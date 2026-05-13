#!/usr/bin/env python3
"""Print the hatched pet profile for this repository."""

from pathlib import Path

PET_FILE = Path(__file__).resolve().parents[1] / "pets" / "helan-cloud-fox.md"


def main() -> None:
    print(PET_FILE.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
