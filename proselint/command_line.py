# -*- coding: utf-8 -*-

"""Command line utility for proselint."""
from __future__ import print_function
from __future__ import absolute_import
from builtins import str


import click
import os
from .tools import (
    close_cache_shelves_after,
    close_cache_shelves,
    errors_to_json,
    lint,
)
import shutil
import subprocess
import sys
from .version import __version__
import traceback


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
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


def clear_cache():
    """Delete the contents of the cache."""
    click.echo("Deleting the cache...")

    # see issue #624
    _delete_compiled_python_files()
    _delete_cache()


def _delete_compiled_python_files():
    """Remove files with a 'pyc' extension."""
    for path, _, files in os.walk(os.getcwd()):
        for fname in [f for f in files if os.path.splitext(f)[1] == ".pyc"]:
            try:
                os.remove(os.path.join(path, fname))
            except OSError:
                pass


def _delete_cache():
    """Remove the proselint cache."""
    proselint_cache = os.path.join("proselint", "cache")
    try:
        shutil.rmtree(proselint_cache)
    except OSError:
        pass


def print_errors(filename, errors, output_json=False, compact=False):
    """Print the errors, resulting from lint, for filename."""
    if output_json:
        click.echo(errors_to_json(errors))

    else:
        for error in errors:

            (check, message, line, column, start, end,
             extent, severity, replacements) = error

            if compact:
                filename = "-"

            click.echo(
                filename + ":" +
                str(1 + line) + ":" +
                str(1 + column) + ": " +
                check + " " +
                message)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(__version__, '--version', '-v', message='%(version)s')
@click.option('--config', is_flag=False, type=click.Path(),
              help="Path to configuration file.")
@click.option('--debug', '-d', is_flag=True, help="Give verbose output.")
@click.option('--clean', '-c', is_flag=True, help="Clear the cache.")
@click.option('--json', '-j', 'output_json', is_flag=True,
              help="Output as JSON.")
@click.option('--time', '-t', is_flag=True, help="Time on a corpus.")
@click.option('--demo', is_flag=True, help="Run over demo file.")
@click.option('--compact', is_flag=True, help="Shorten output.")
@click.argument('paths', nargs=-1, type=click.Path())
@close_cache_shelves_after
def proselint(paths=None, config=None, version=None, clean=None, debug=None,
              output_json=None, time=None, demo=None, compact=None):
    """Create the CLI for proselint, a linter for prose."""
    if time:
        # click.echo(timing_test())
        print("This option does not work for the time being.")
        return

    # In debug or clean mode, delete cache & *.pyc files before running.
    if debug or clean:
        clear_cache()

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

    for fp in filepaths:
        if fp == '-':
            fp = '<stdin>'
            f = sys.stdin
        else:
            try:
                f = click.open_file(
                    fp, 'r', encoding="utf-8", errors="replace")
            except Exception:
                traceback.print_exc()
                sys.exit(2)
        errors = lint(f, debug=debug, config_file_path=config)
        num_errors += len(errors)
        print_errors(fp, errors, output_json, compact=compact)

    # Return an exit code
    close_cache_shelves()
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
