from __future__ import annotations

import argparse
import logging
from collections.abc import Sequence

logger = logging.getLogger(__name__)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.add_argument("--name", help="Name to greet")
    return parser


def greet(name: str | None = None) -> str:
    if name:
        return f"Hello {name}!"
    return "Hello World!"


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    message = greet(args.name)
    logger.info("Prepared greeting for %s", args.name or "World")
    print(message)
    return 0
