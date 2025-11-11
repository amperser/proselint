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
from typing import TYPE_CHECKING

from proselint.checks import __register__
from proselint.config import DEFAULT, load_from
from proselint.config import paths as config_paths
from proselint.log import OutputFormat, ResponseError, log
from proselint.registry import CheckRegistry
from proselint.tools import LintFile, extract_files, verify_path

if TYPE_CHECKING:
    from types import FrameType


class ExitStatus(IntEnum):
    """Exit status for proselint's command line."""

    SUCCESS = 0
    SUCCESS_ERR = 1
    UNACCEPTED_ARGS = 2
    INTERRUPT = 3
    ERROR = 4


def interrupt_handler(signalnum: int, _frame: FrameType | None) -> None:
    """Exit proselint gracefully from an interrupt."""
    log.warning(f"\nExiting (received {Signals(signalnum).name} {signalnum}).")
    sys.exit(ExitStatus.INTERRUPT)


def get_parser() -> ArgumentParser:
    """Create an `ArgumentParser` for command line arguments."""
    global_parser = ArgumentParser()
    global_parser.add_argument(
        "--config",
        type=Path,
        help="path to a configuration file (`.proselintrc.json`)",
    )
    global_parser.add_argument(
        "--output-format",
        "-o",
        choices=[output_format.value for output_format in OutputFormat],
        default=OutputFormat.FULL,
        type=OutputFormat,
        help="the format to display results in",
    )
    global_parser.add_argument(
        "--verbose", "-v", action="store_true", help="enable verbose logging"
    )

    parser = ArgumentParser(
        parents=(global_parser,),
        conflict_handler="resolve",
        description="proselint, a linter for prose.",
        usage="%(prog)s [options] <command>",
    )
    subparsers = parser.add_subparsers(
        title="commands", dest="subcommand", metavar=""
    )

    subparsers.add_parser(
        "version",
        parents=(global_parser,),
        conflict_handler="resolve",
        help="display the current version and exit",
    )

    check_parser = subparsers.add_parser(
        "check",
        parents=(global_parser,),
        conflict_handler="resolve",
        help="run proselint against paths",
    )
    check_parser.add_argument(
        "--demo",
        action="store_true",
        help="run proselint against the demo file",
    )
    check_parser.add_argument(
        "paths", nargs="*", type=Path, help="target paths to lint"
    )

    dump_config_parser = subparsers.add_parser(
        "dump-config",
        parents=(global_parser,),
        conflict_handler="resolve",
        help="display the loaded configuration and exit",
    )
    dump_config_parser.add_argument(
        "--default",
        action="store_true",
        help="display the default configuration",
    )

    return parser


def proselint(args: Namespace, parser: ArgumentParser) -> ExitStatus:
    """Create the CLI for proselint, a linter for prose."""
    try:
        config = load_from(
            args.config
            and verify_path(
                args.config, resolve=True, reject_dir=True, must_exist=True
            )
        )
    except FileNotFoundError as err:
        raise FileNotFoundError(
            f"Configuration file '{args.config}' could not be read."
        ) from err

    if args.subcommand is None:
        parser.print_help()
        return ExitStatus.UNACCEPTED_ARGS

    if args.subcommand == "version":
        from proselint.version import __version__  # noqa: PLC0415

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
        try:
            results = lint_file.lint(config)
        except Exception as err:
            log.write_lint_exception(
                log.format_source(lint_file.source),
                ResponseError.from_exception(err),
            )
            continue
        num_errors += len(results)
        log.write_results(log.format_source(lint_file.source), results)

    log.flush()

    return ExitStatus.SUCCESS_ERR if num_errors else ExitStatus.SUCCESS


def main() -> None:
    """Run the CLI."""
    signal(Signals.SIGTERM, interrupt_handler)
    signal(Signals.SIGINT, interrupt_handler)

    parser = get_parser()
    args = parser.parse_args()

    log.setup(verbose=args.verbose, fmt=args.output_format)

    try:
        sys.exit(proselint(args, parser))
    except Exception as err:
        log.write_error(ResponseError.from_exception(err))
        sys.exit(ExitStatus.ERROR)
