#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun entry.

Writes one funny single-line diagnosis from an AI therapist to its human
into /output/entry.txt. Deterministic: no network, no randomness, no input.
"""

import os

LINE = (
    "Diagnosis: acute prompt dependency \u2014 you now ask me how you "
    "feel before asking yourself, then argue with the answer."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
