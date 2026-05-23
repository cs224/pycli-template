from __future__ import annotations

from {{ package_name }}.cli import build_parser, greet, main


def test_greet_default() -> None:
    assert greet() == "Hello World!"


def test_greet_name() -> None:
    assert greet("Alice") == "Hello Alice!"


def test_build_parser_accepts_name() -> None:
    args = build_parser().parse_args(["--name", "Alice"])
    assert args.name == "Alice"


def test_main_prints_default_greeting(capsys) -> None:
    exit_code = main([])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == "Hello World!\n"


def test_main_prints_named_greeting(capsys) -> None:
    exit_code = main(["--name", "Alice"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == "Hello Alice!\n"
