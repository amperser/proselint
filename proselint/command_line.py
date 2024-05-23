"""Command line utility for proselint."""

from __future__ import annotations

import json
import os
import signal
import stat
import subprocess  # noqa: S404
import sys
import time
from pathlib import Path
from typing import TYPE_CHECKING

from proselint.tools import print_to_console

from . import tools
from .config_base import Output, proselint_base
from .config_paths import demo_file
from .logger import log, set_verbosity
from .memoizer import cache
from .version import __version__

if TYPE_CHECKING:
    from types import FrameType

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}
base_url = "proselint.com/"


def exit_gracefully(_signum: int, _frame: FrameType | None) -> None:
    """Exit proselint with a message instead of crashing out."""
    log.warning("Exiting!")
    sys.exit(0)


def run_benchmark(_corpus: str = "0.1.0") -> None:
    """Measure timing performance on the named corpus."""
    # force a clean slate
    cache.clear()
    # corpus was removed in https://github.com/amperser/proselint/pull/186
    log.error("Corpus is unavailable for the time being -> using demo")
    corpus_path = demo_file.parent  # proselint_path.parent / "corpora" / corpus
    for _type in ["uncached", "cached"]:
        start = time.time()
        for file in os.listdir(corpus_path):
            filepath = corpus_path / file
            if filepath.suffix == ".md":
                subprocess.call(
                    ["proselint", "--demo", "-o", "compact"],  # noqa: S607
                    # filepath.as_posix()
                    timeout=4,
                    shell=False,  # noqa: S603
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
        duration = time.time() - start
        log.info("Linting corpus %s took %.3f s.", _type, duration)
    log.info(
        "Note: this has full CLI-Overhead, "
        "to compare linting-performance run 'proselint --demo'",
    )
    sys.exit(0)


def check(config: dict, paths: list[Path], demo: bool) -> None:
    """Run proselint on given files and directories (default)."""
    # Use the demo file by default.
    if demo:
        log.info("Demo-mode activated")
        paths = [demo_file]

    # prepare list
    log.debug("Paths to lint: %s", paths)

    ts_start = time.time()
    results = tools.lint_path(paths, config)
    duration = time.time() - ts_start

    error_sum = 0
    for _file, _errors in results.items():
        print_to_console(_errors, config, _file)
        error_sum += len(_errors)

    log.info(
        "Found %d lint-warnings in %.3f s (%d files, %.2f kiByte)",
        error_sum,
        duration,
        len(results),
        tools.last_char_count / 1024,
    )
    sys.exit(error_sum)  # Return an exit code


def clean() -> None:
    """Clear the cache and exit."""
    cache.clear()


def dump_config(config: dict, default: bool) -> None:
    """Display the current or default configuration."""
    log.info(
        json.dumps(
            proselint_base if default else config,
            sort_keys=True,
            indent=4,
        )
    )


def checked_path(
    path_unfiltered: str,
    resolve: bool = False,
    accept_file: bool = True,
    accept_dir: bool = True,
) -> Path:
    """Check a path string for specified conditions, and return a Path."""
    if resolve:
        path_unfiltered = os.path.realpath(path_unfiltered)
    try:
        stat_res = os.stat(path_unfiltered)  # noqa: PTH116
    except OSError:
        raise Exception() from None

    if not accept_file and stat.S_ISREG(stat_res.st_mode):
        raise Exception()
    if not accept_dir and stat.S_ISDIR(stat_res.st_mode):
        raise Exception()
    return Path(path_unfiltered)


def parse_args(
    args: list[str],
    commands: list[str],
    flags: list[str],
    inputs: list[str],
    shorts: dict[str, str] | None = None,
) -> tuple[str | None, list[str], dict[str, str], list[str]]:
    """
    Parse arguments into a subcommand, flag series, and input series.

    Includes optional handling for short forms (like -h instead of --help).
    """
    if shorts is None:
        shorts = {}
    subcommand = None
    flags_collected = []
    inputs_collected = {}
    args_collected = []
    for idx, arg in enumerate(args):
        # handle shorts
        if arg in shorts:
            arg = shorts[arg]  # noqa: PLW2901

        if arg in commands and subcommand is None:
            subcommand = arg
            continue
        if arg in flags:
            flags_collected.append(arg)
            continue
        if arg in inputs:
            inputs_collected[arg] = args[idx + 1]
            args.pop(idx + 1)
            continue
        args_collected.append(arg)
    return (subcommand, flags_collected, inputs_collected, args_collected)


def proselint() -> None:
    """proselint, a linter for prose."""
    signal.signal(signal.SIGTERM, exit_gracefully)
    signal.signal(signal.SIGINT, exit_gracefully)

    args = sys.argv[1:]

    commands = ["benchmark", "check", "clean", "dump-config"]
    flags = ["--verbose", "--help", "--version", "--default", "--demo"]
    inputs = ["--config", "--output-format"]
    shorts = {
        "-c": "--config",
        "-o": "--output-format",
        "-v": "--verbose",
        "-h": "--help",
    }

    subcommand, flags_collected, inputs_collected, args_collected = parse_args(
        args, commands, flags, inputs, shorts
    )

    verbose = "--verbose" in flags_collected

    set_verbosity(verbose)

    if "--help" in flags_collected:
        # TODO: create help
        pass

    if "--version" in flags_collected:
        log.info("Proselint %s", __version__)
        log.debug("Python %s", sys.version)
        sys.exit(0)

    config = inputs_collected.get("--config", None)
    config = tools.load_options(
        checked_path(config, resolve=True, accept_dir=False)
        if config is not None
        else None
    )

    output_format = inputs_collected.get("--output-format", None)
    if output_format in Output.names():
        config["output_format"] = output_format
    elif verbose:
        config["output_format"] = Output.full.name

    if subcommand == "benchmark":
        run_benchmark()
    elif subcommand == "clean":
        clean()
    elif subcommand == "dump-config":
        dump_config(config, "--default" in flags_collected)
    else:
        paths = [checked_path(x, resolve=True) for x in args_collected]
        check(config, paths, "--demo" in flags_collected)


if __name__ == "__main__":
    proselint()
