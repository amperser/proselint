"""Command line utility for proselint."""

import json
import os
import subprocess
import sys
import traceback
from pathlib import Path

import click

from proselint.config import DEFAULT, load_from
from proselint.checks import __register__
from proselint.registry import CheckRegistry
from proselint.registry.checks import LintResult

from .tools import errors_to_json, lint
from .version import __version__

CONTEXT_SETTINGS = {"help_option_names": ['-h', '--help']}
base_url = "proselint.com/"
proselint_path = os.path.dirname(os.path.realpath(__file__))
demo_file = os.path.join(proselint_path, "demo.md")


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
        if ".md" == filepath[-3:]:
            subprocess.call(["proselint", filepath, ">/dev/null"])

    return time.time() - start


def print_errors(
    filename: str,
    results: list[LintResult],
    *,
    output_json: bool = False,
    compact: bool = False,
) -> None:
    """Print the errors, resulting from lint, for filename."""
    if output_json:
        click.echo(errors_to_json(results))

    if compact:
        filename = "-"
    for result in results:
        click.echo(f"{filename}:{result}")


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
@click.argument('paths', nargs=-1, type=click.Path())
def proselint(paths=None, config=None, version=None,
              debug=None, output_json=None, time=None, demo=None, compact=None,
              dump_config=None, dump_default_config=None):
    """Create the CLI for proselint, a linter for prose."""
    if dump_default_config:
        return print(json.dumps(DEFAULT, sort_keys=True, indent=4))

    config = load_from(config)
    if dump_config:
        print(json.dumps(config, sort_keys=True, indent=4))
        return

    if time:
        # click.echo(timing_test())
        print("This option does not work for the time being.")
        return

    # Use the demo file by default.
    if demo:
        paths = [demo_file]

    # Expand the list of directories and files.
    filepaths = extract_files(list(paths))

    # Lint the files
    num_errors = 0

    # Use stdin if no paths were specified
    if len(paths) == 0:
        filepaths.append('-')

    CheckRegistry().register_many(__register__)
    for fp in filepaths:
        if fp == '-':
            fp = '<stdin>'
            f = sys.stdin
        else:
            try:
                f = click.open_file(fp, 'r', "utf-8", "replace")
            except Exception:
                traceback.print_exc()
                sys.exit(2)
        errors = lint(f, config, debug=debug)
        num_errors += len(errors)
        print_errors(fp, errors, output_json=output_json, compact=compact)

    # Return an exit code
    if num_errors > 0:
        sys.exit(1)
    else:
        sys.exit(0)


def extract_files(files):
    """Expand list of paths to include all text files matching the pattern."""
    expanded_files = []
    legal_extensions = [".md", ".txt", ".rtf", ".html", ".tex", ".markdown"]

    for f in files:
        # If it's a directory, recursively walk through it and find the files.
        if os.path.isdir(f):
            for dir_, _, filenames in os.walk(f):
                for filename in filenames:
                    fn, file_extension = os.path.splitext(filename)
                    if file_extension in legal_extensions:
                        joined_file = os.path.join(dir_, filename)
                        expanded_files.append(joined_file)

        # Otherwise add the file directly.
        else:
            expanded_files.append(f)

    return expanded_files


if __name__ == '__main__':
    proselint()
