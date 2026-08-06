from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mensa",
        description="Mensa-chan — a local-first terminal assistant.",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="Mensa-chan 0.1.0 — Radicchio & Speck",
    )

    return parser


def main() -> None:
    parser = build_parser()
    parser.parse_args()

    print(
        """
🍝 Mensa-chan

A local-first terminal assistant for everyday life.

Available modules:

• cooking
• writing
• notes
• utilities
""".strip()
    )


if __name__ == "__main__":
    main()
