"""Command-line interface for the CI/CD demo."""

import argparse
from collections.abc import Sequence

from cicd_demo import __version__
from cicd_demo.core import add, greet


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cicd-demo",
        description="一个用于演示 GitHub Actions CI/CD 的命令行程序",
    )
    parser.add_argument("--version", action="version", version=__version__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    greet_parser = subparsers.add_parser("greet", help="生成问候语")
    greet_parser.add_argument("name", help="要问候的名字")

    add_parser = subparsers.add_parser("add", help="计算数字之和")
    add_parser.add_argument("numbers", type=float, nargs="+", help="一个或多个数字")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "greet":
        print(greet(args.name))
    elif args.command == "add":
        print(format(add(args.numbers), ".12g"))
    return 0
