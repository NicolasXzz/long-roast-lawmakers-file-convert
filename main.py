#!/usr/bin/env python3
"""Write one satirical sentence to /output/entry.txt.

The Long Roast: Lawmakers and the File They Cannot Convert.
One sentence, 137 characters, roasting the lawmaker who decides what
the internet may do yet cannot convert a file to PDF himself.
"""

import os

LINE = (
    "The man who decides what the internet may do asked his grandson "
    "to convert the crypto bill to PDF, then expensed the boy as a "
    "consultant."
)


def main() -> None:
    # Gate: one sentence, 1-320 UTF-8 characters, not only whitespace.
    assert 1 <= len(LINE) <= 320, "entry must be 1-320 characters"
    assert LINE.strip() == LINE and LINE.count(".") == 1, "one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
