"""Command line utility for proselint."""
# pyright: reportUnusedCallResult=false, reportAny=false
# TODO: explore options for typing argparse.Namespace

from __future__ import annotations

import json
import sys
from argparse import ArgumentParser, Namespace
from enum import IntEnum
from pathlib import Path
from signal import Signals, signal
from typing import TYPE_CHECKING, Optional

from proselint.checks import __register__
from proselint.config import DEFAULT, load_from
from proselint.config import paths as config_paths
from proselint.log import log
from proselint.registry import CheckRegistry
from proselint.tools import LintFile, OutputFormat, extract_files, verify_path
from proselint.version import __version__

if TYPE_CHECKING:
    from types import FrameType


class ExitStatus(IntEnum):
    """Exit status for proselint's command line."""

    SUCCESS = 0
    SUCCESS_ERR = 1
    UNACCEPTED_ARGS = 2
    INTERRUPT = 3


def interrupt_handler(signalnum: int, _frame: Optional[FrameType]) -> None:
    """Exit proselint gracefully from an interrupt."""
    log.warning(f"Exiting (received {Signals(signalnum)}).")
    sys.exit(ExitStatus.INTERRUPT)


def get_parser() -> ArgumentParser:
    """Create an `ArgumentParser` for command line arguments."""
    global_parser = ArgumentParser()
    global_parser.add_argument("--config", type=Path)
    global_parser.add_argument(
        "--output-format",
        "-o",
        choices=[output_format.value for output_format in OutputFormat],
        default=OutputFormat.FULL,
        type=OutputFormat,
    )
    global_parser.add_argument("--verbose", "-v", action="store_true")

    parser = ArgumentParser(
        parents=(global_parser,), conflict_handler="resolve"
    )
    subparsers = parser.add_subparsers(dest="subcommand")

    subparsers.add_parser(
        "version", parents=(global_parser,), conflict_handler="resolve"
    )

    check_parser = subparsers.add_parser(
        "check", parents=(global_parser,), conflict_handler="resolve"
    )
    check_parser.add_argument("--demo", action="store_true")
    check_parser.add_argument("paths", nargs="*", type=Path)

    dump_config_parser = subparsers.add_parser(
        "dump-config", parents=(global_parser,), conflict_handler="resolve"
    )
    dump_config_parser.add_argument("--default", action="store_true")

    return parser


def proselint(args: Namespace, parser: ArgumentParser) -> ExitStatus:
    """Create the CLI for proselint, a linter for prose."""
    config = load_from(
        args.config and verify_path(args.config, resolve=True, reject_dir=True)
    )

    if args.subcommand is None:
        parser.print_help()
        return ExitStatus.UNACCEPTED_ARGS

    if args.subcommand == "version":
        log.info("Proselint %s", __version__)
        log.debug("Python %s", sys.version)
        return ExitStatus.SUCCESS

    if args.subcommand == "dump-config":
        log.info(
            json.dumps(
                DEFAULT if args.default else config, sort_keys=True, indent=4
            )
        )
        return ExitStatus.SUCCESS

    # Lint the files
    CheckRegistry().register_many(__register__)

    lint_files: list[LintFile] = []
    if args.demo:
        lint_files = [LintFile(config_paths.demo_path)]
    elif len(args.paths) == 0:
        lint_files = [LintFile.from_stdin()]
    else:
        lint_files = list(map(LintFile, extract_files(args.paths)))

    num_errors = 0

    for lint_file in lint_files:
        results = lint_file.lint(config)
        num_errors += len(results)
        lint_file.output_errors(results, args.output_format)

    return ExitStatus(int(num_errors > 0))


def main() -> None:
    """Run the CLI."""
    signal(Signals.SIGTERM, interrupt_handler)
    signal(Signals.SIGINT, interrupt_handler)

    parser = get_parser()
    args = parser.parse_args()

    log.setup(verbose=args.verbose)

    sys.exit(proselint(args, parser))
