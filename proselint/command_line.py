"""Command line utility for proselint."""

import json
import sys
from argparse import ArgumentParser
from pathlib import Path

from proselint.checks import __register__
from proselint.config import DEFAULT, load_from
from proselint.config import paths as config_paths
from proselint.registry import CheckRegistry
from proselint.tools import LintFile, OutputFormat, extract_files
from proselint.version import __version__

base_url = "proselint.com/"


def proselint() -> None:
    """Create the CLI for proselint, a linter for prose."""
    global_parser = ArgumentParser()
    _ = global_parser.add_argument("--config", type=Path)
    _ = global_parser.add_argument(
        "--output-format",
        "-o",
        choices=[output_format.value for output_format in OutputFormat],
        default=OutputFormat.FULL,
        type=OutputFormat,
    )
    _ = global_parser.add_argument("--verbose", "-v", action="store_true")
    _ = global_parser.add_argument("--version", "-V", action="store_true")

    parser = ArgumentParser(
        parents=(global_parser,), conflict_handler="resolve"
    )
    subparsers = parser.add_subparsers(dest="subcommand")

    check_parser = subparsers.add_parser(
        "check", parents=(global_parser,), conflict_handler="resolve"
    )
    _ = check_parser.add_argument("--demo", action="store_true")
    _ = check_parser.add_argument("paths", nargs="*", type=Path)

    dump_config_parser = subparsers.add_parser(
        "dump-config", parents=(global_parser,), conflict_handler="resolve"
    )
    _ = dump_config_parser.add_argument("--default", action="store_true")

    args = parser.parse_args()

    config = load_from(args.config)

    if args.version:
        return print(f"Proselint {__version__}\nPython {sys.version}")

    if args.subcommand is None:
        return parser.print_help()
    if args.subcommand == "dump-config":
        return print(
            json.dumps(
                DEFAULT if args.default else config, sort_keys=True, indent=4
            )
        )

    # Lint the files
    num_errors = 0

    CheckRegistry().register_many(__register__)

    lint_files: list[LintFile] = []
    if args.demo:
        lint_files = [LintFile(config_paths.demo_path)]
    elif len(args.paths) == 0:
        lint_files = [LintFile.from_stdin()]
    else:
        lint_files = list(map(LintFile, extract_files(args.paths)))

    for lint_file in lint_files:
        results = lint_file.lint(config)
        num_errors += len(results)
        lint_file.output_errors(results, args.output_format)
    # Return an exit code
    sys.exit(int(num_errors > 0))


if __name__ == "__main__":
    proselint()
