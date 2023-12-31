"""Command line utility for proselint."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import traceback
from pathlib import Path
from typing import Optional, Union

import click

from .config import default
from .logger import logger, set_verbosity
from .paths import demo_file, proselint_path
from .tools import (
    ResultLint,
    clear_cache,
    close_cache_on_exit,
    close_cache_shelves,
    errors_to_json,
    lint,
    load_options,
)
from .version import __version__

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}
base_url = "proselint.com/"


def timing_test(corpus: str = "0.1.0") -> float:
    """Measure timing performance on the named corpus."""
    import time

    # corpus was removed in https://github.com/amperser/proselint/pull/186
    logger.error("This option does not work for the time being.")
    corpus_path = proselint_path.parent / "corpora" / corpus
    start = time.time()
    for file in os.listdir(corpus_path):
        filepath = corpus_path / file
        if filepath.suffix == ".md":
            subprocess.call(["proselint", filepath, ">/dev/null"])
    duration = time.time() - start
    logger.info("Linting corpus took %.3f.", duration)
    return duration


def print_errors(
    filename: Union[Path, str],
    errors: list[ResultLint],
    output_json: bool = False,
    compact: bool = False,
) -> None:
    """Print the errors, resulting from lint, for filename."""
    if output_json:
        logger.info(errors_to_json(errors))

    else:
        for error in errors:
            (
                check,
                message,
                line,
                column,
                start,
                end,
                extent,
                severity,
                replacements,
            ) = error

            if compact:
                filename = "-"
            if isinstance(filename, Path):
                filename = filename.name  # TODO: just for now, should be path - cwd

            logger.info(  # TODO: fname+line to link (see ruff code)
                filename
                + ":"
                + str(1 + line)
                + ":"
                + str(1 + column)
                + ": "
                + check
                + " "
                + message,
            )


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(__version__, "--version", "-v", message="%(version)s")
@click.option(
    "--config",
    is_flag=False,
    type=click.Path(exists=True, dir_okay=False, resolve_path=True),
    help="Path to configuration file.",
)
@click.option("--debug", "-d", is_flag=True, help="Give verbose output.")
@click.option("--clean", "-c", is_flag=True, help="Clear the cache.")
@click.option("--json", "-j", "output_json", is_flag=True, help="Output as JSON.")
@click.option("--time", "-t", is_flag=True, help="Time on a corpus.")
@click.option("--demo", is_flag=True, help="Run over demo file.")
@click.option("--compact", is_flag=True, help="Shorten output.")
@click.option("--dump-config", is_flag=True, help="Prints current config.")
@click.option("--dump-default-config", is_flag=True, help="Prints default config.")
@click.argument("paths", nargs=-1, type=click.Path(exists=True, resolve_path=True))
@close_cache_on_exit
def proselint(
    paths: Union[list[Path], Path, None],
    config: Optional[Path] = None,
    version=None,
    clean: bool = False,
    debug: bool = False,
    output_json: bool = False,
    time: bool = False,
    demo: bool = False,
    compact: bool = False,
    dump_config: bool = False,
    dump_default_config: bool = False,
):
    """Create the CLI for proselint, a linter for prose."""
    if dump_default_config:
        _json = json.dumps(default, sort_keys=True, indent=4)
        logger.info(_json)
        return _json  # TODO: here dump is returned, below None is returned?

    if isinstance(config, str):
        config = Path(config)
    config = load_options(config)

    if dump_config:
        logger.info(json.dumps(config, sort_keys=True, indent=4))
        return None

    if time:
        timing_test()
        return None

    # In debug or clean mode, delete cache & *.pyc files before running.
    if debug or clean:
        set_verbosity(True)
        logger.info("Debug-mode activated -> will clean cache now")
        clear_cache()

    # Use the demo file by default.
    if demo:
        logger.info("Demo-mode activated")
        paths = [demo_file]

    # prepare list
    if paths is None:
        paths = []
    if isinstance(paths, str):
        paths = [Path(paths)]
    if isinstance(paths, Path):
        paths = [paths]
    if isinstance(paths, list):
        paths = [Path(path) for path in paths]

    # Expand the list of directories and files.
    filepaths = extract_files(paths)

    # Lint the files
    num_errors = 0

    # Use stdin if no paths were specified
    if len(paths) == 0:
        logger.info("No path specified -> will read from <stdin>")
        fp = "<stdin>"
        f = sys.stdin
        errors = lint(f, debug, config)
        num_errors += len(errors)
        print_errors(fp, errors, output_json, compact)
    else:
        for fp in filepaths:
            logger.debug("Opening file '%s'", fp.name)
            try:
                # TODO: is errors-replace the best? can we detect coding?
                f = fp.open(encoding="utf-8", errors="replace")
            except Exception:
                traceback.print_exc()
                sys.exit(2)
            errors = lint(f, debug, config)
            num_errors += len(errors)

            print_errors(fp, errors, output_json, compact)

    # Return an exit code
    close_cache_shelves()
    if num_errors > 0:
        sys.exit(1)
    else:
        sys.exit(0)


def extract_files(files: list[Path]) -> list[Path]:
    """Expand list of paths to include all text files matching the pattern."""
    expanded_files = []
    legal_extensions = [".md", ".txt", ".rtf", ".html", ".tex", ".markdown"]

    for file in files:
        # If it's a directory, recursively walk through it and find the files.
        if file.is_dir():
            for _dir, _, _filenames in os.walk(file):
                _path = Path(_dir)
                for filename in _filenames:
                    _file_path = _path / filename
                    if _file_path.suffix.lower() in legal_extensions:
                        expanded_files.append(_file_path)

        # Otherwise add the file directly.
        else:
            expanded_files.append(file)

    return expanded_files


if __name__ == "__main__":
    proselint()
