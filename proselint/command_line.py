"""Command line utility for proselint."""

import json
import os
import subprocess
import sys
from itertools import chain
from pathlib import Path

import click

from proselint.checks import __register__
from proselint.config import DEFAULT, load_from
from proselint.config import paths as config_paths
from proselint.registry import CheckRegistry
from proselint.tools import LintFile
from proselint.version import __version__

CONTEXT_SETTINGS = {"help_option_names": ['-h', '--help']}
base_url = "proselint.com/"


# TODO: fix broken corpus
def timing_test(corpus="0.1.0"):
    """Measure timing performance on the named corpus."""
    import time
    dirname = os.path.dirname
    corpus_path = os.path.join(
        dirname(dirname(os.path.realpath(__file__))), "corpora", corpus)
    start = time.time()
    for file in os.listdir(corpus_path):
        filepath = os.path.join(corpus_path, file)
        if filepath[-3:] == ".md":
            subprocess.call(["proselint", filepath, ">/dev/null"])

    return time.time() - start


def extract_files(paths: list[Path]) -> list[Path]:
    """Expand list of paths to include all text files matching the pattern."""
    accepted_extensions = [".md", ".txt", ".rtf", ".html", ".tex", ".markdown"]

    return list(chain.from_iterable(
        (
            file
            for root, _, files in path.walk()
            for file in map(root.__truediv__, files)
            if file.suffix in accepted_extensions
        ) if path.is_dir() else (path,)
        for path in paths
    ))


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(__version__, '--version', '-v', message='%(version)s')
@click.option('--config', is_flag=False,
              type=click.Path(exists=True, path_type=Path),
              help="Path to configuration file.")
@click.option('--debug', '-d', is_flag=True, help="Give verbose output.")
@click.option('--json', '-j', 'output_json', is_flag=True,
              help="Output as JSON.")
@click.option('--time', '-t', is_flag=True, help="Time on a corpus.")
@click.option('--demo', is_flag=True, help="Run over demo file.")
@click.option('--compact', is_flag=True, help="Shorten output.")
@click.option('--dump-config', is_flag=True, help="Prints current config.")
@click.option('--dump-default-config', is_flag=True,
              help="Prints default config.")
@click.argument('paths', nargs=-1, type=click.Path(exists=True, path_type=Path))
def proselint(
    paths: list[Path], config=None, version=None,
    debug=None, output_json=None, time=None, demo=None, compact=None,
    dump_config=None, dump_default_config=None
) -> None:
    """Create the CLI for proselint, a linter for prose."""
    if dump_default_config:
        return print(json.dumps(DEFAULT, sort_keys=True, indent=4))

    config = load_from(config)
    if dump_config:
        print(json.dumps(config, sort_keys=True, indent=4))
        return None

    if time:
        # click.echo(timing_test())
        print("This option does not work for the time being.")
        return None

    # Lint the files
    num_errors = 0

    CheckRegistry().register_many(__register__)

    lint_files: list[LintFile] = []
    if demo:
        lint_files = [LintFile(config_paths.demo_path)]
    elif len(paths) == 0:
        lint_files = [LintFile.from_stdin()]
    else:
        lint_files = list(map(LintFile, extract_files(paths)))

    for lint_file in lint_files:
        results = lint_file.lint(config)
        num_errors += len(results)
        lint_file.output_errors(results, output_json=output_json, compact=compact)
    # Return an exit code
    sys.exit(int(num_errors > 0))


if __name__ == '__main__':
    proselint()
