"""Command line utility for proselint."""

from __future__ import annotations

import json
import os
import signal
import subprocess  # noqa: S404
import sys
import time
from pathlib import Path
from typing import TYPE_CHECKING, Optional, Union

import click

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


def run_benchmark(_corpus: str = "0.1.0") -> float:
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
    return duration


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option(
    "--config",
    is_flag=False,
    type=click.Path(exists=True, dir_okay=False, resolve_path=True),
    help="Path to configuration file.",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Give verbose output.",
)
@click.option("--clean", "-c", is_flag=True, help="Clear the cache and exit.")
@click.option("--benchmark", "-b", is_flag=True, help="Time on a corpus.")
@click.option("--demo", is_flag=True, help="Run over demo file.")
@click.option(
    "--output-format",
    "-o",
    type=click.Choice(Output.names()),
    default=None,
    help="Override config to change format.",
)
@click.option("--dump-config", is_flag=True, help="Prints current config.")
@click.option(
    "--dump-default-config", is_flag=True, help="Prints default config."
)
@click.option("--version", is_flag=True)
@click.argument(
    "paths", nargs=-1, type=click.Path(exists=True, resolve_path=True)
)
def proselint(  # noqa: PLR0912, PLR0913, PLR0917, C901
    paths: Union[list[Path], Path, None],
    config: Optional[Path] = None,
    clean: bool = False,  # TODO: this should be a subcommand
    verbose: bool = False,
    output_format: Optional[str] = None,
    benchmark: bool = False,
    demo: bool = False,
    dump_config: bool = False,  # TODO: this should be a subcommand
    dump_default_config: bool = False,  # TODO: this should be a switch in dump
    version: bool = False,
) -> None:
    """proselint, a linter for prose."""
    # NOTE: the above determines the CLI help message
    signal.signal(signal.SIGTERM, exit_gracefully)
    signal.signal(signal.SIGINT, exit_gracefully)

    if verbose:
        set_verbosity(True)

    if version:
        click.echo("Proselint v%s" % __version__)
        log.debug("Python    v%s", sys.version)
        log.debug("Click     v%s", click.__version__)
        sys.exit(0)

    if clean:
        cache.clear()
        sys.exit(0)

    if dump_default_config:
        click.echo(json.dumps(proselint_base, sort_keys=True, indent=4))
        sys.exit(0)

    if isinstance(config, str):
        config = Path(config)
    config = tools.load_options(config)

    if dump_config:
        click.echo(json.dumps(config, sort_keys=True, indent=4))
        sys.exit(0)

    if output_format in Output.names():
        config["output_format"] = output_format
    elif verbose:
        config["output_format"] = Output.full.name

    if benchmark:
        run_benchmark()
        sys.exit(0)

    # Use the demo file by default.
    if demo:
        log.info("Demo-mode activated")
        paths = [demo_file]

    # prepare list
    if paths is None:
        paths = []
    if isinstance(paths, str):
        paths = [Path(paths)]
    if isinstance(paths, Path):
        paths = [paths]
    if isinstance(paths, (list, tuple)):
        paths = [Path(path) for path in paths]
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


if __name__ == "__main__":
    proselint()
