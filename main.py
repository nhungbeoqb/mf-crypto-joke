#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes a single crypto-trading joke (under 200 characters) to
/output/entry.txt, the path the kit's RULES.txt gate names.
Python 3.13 standard library only; deterministic output.
"""

import os

JOKE = (
    "I bought the dip because the chart promised support. "
    "Now my bag is so heavy the exchange offered me a gym membership "
    "\u2014 and my group chat renamed me \u2018Exit Liquidity\u2019."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
