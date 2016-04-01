#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Command line utility for proselint."""
from __future__ import print_function
from __future__ import absolute_import
from builtins import str


import click
import os
from .tools import (
    line_and_column,
    is_quoted,
    close_cache_shelves_after,
    close_cache_shelves
)
from . import checks as pl
import pkgutil
import subprocess
import re
import json
import importlib
import sys
from .score import score
from .version import __version__


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
base_url = "proselint.com/"
proselint_path = os.path.dirname(os.path.realpath(__file__))
demo_file = os.path.join(proselint_path, "demo.md")


def run_initialization():
    """Run the initialization method for each check."""
    for loader, module_name, is_pkg in pkgutil.walk_packages(pl.__path__):
        module = loader.find_module(module_name).load_module(module_name)

        # Run the initialization.
        try:
            assert(hasattr(module.initialize, '__call__'))
            module.initialize()
        except Exception:
            pass


def lint(input_file, debug=False):
    """Run the linter on the input file."""
    # Load the options.
    options = json.load(open(os.path.join(proselint_path, '.proselintrc')))

    # Extract the checks.
    sys.path.append(proselint_path)
    checks = []
    check_names = [key for (key, val)
                   in list(options["checks"].items()) if val]

    for check_name in check_names:
        module = importlib.import_module("checks." + check_name)
        for d in dir(module):
            if re.match("check", d):
                checks.append(getattr(module, d))

    # Apply all the checks.
    text = input_file.read()
    errors = []
    for check in checks:
        if debug:
            click.echo(check.__module__ + "." + check.__name__)

        result = check(text)

        for error in result:
            (start, end, check, message) = error
            (line, column) = line_and_column(text, start)
            if not is_quoted(start, text):
                errors += [(check, message, line, column, start, end,
                           end - start, "warning", None)]

        if len(errors) > options["max_errors"]:
            break

    # Sort the errors by line and column number.
    errors = sorted(errors[:options["max_errors"]])

    return errors


def lintscore():
    """Compute the linter's score on a corpus."""
    return score()


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
            subprocess.call(
                "proselint {} >/dev/null".format(filepath), shell=True)

    return time.time() - start


def clear_cache():
    """Delete the contents of the cache."""
    click.echo("Deleting the cache...")
    subprocess.call("find . -name '*.pyc' -delete", shell=True)
    subprocess.call(
        "rm -rfv proselint/cache > /dev/null && mkdir -p {}".format(
            os.path.join(os.path.expanduser("~"), ".proselint")),
        shell=True)


def errors_to_json(errors):
    """Convert the errors to JSON."""
    out = []
    for e in errors:
        out.append({
            "check": e[0],
            "message": e[1],
            "line": 1 + e[2],
            "column": 1 + e[3],
            "start": 1 + e[4],
            "end": 1 + e[5],
            "extent": e[6],
            "severity": e[7],
            "replacements": e[8],
        })

    return json.dumps(dict(status="success", data={"errors": out}))


def show_errors(filename, errors, output_json=False, compact=False):
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
@click.option('--initialize', '-i', is_flag=True)
@click.option('--debug', '-d', is_flag=True)
@click.option('--clean', '-c', is_flag=True)
@click.option('--score', '-s', is_flag=True)
@click.option('--json', '-j', 'output_json', is_flag=True)
@click.option('--time', '-t', is_flag=True)
@click.option('--demo', is_flag=True)
@click.option('--compact', is_flag=True)
@click.argument('paths', nargs=-1, type=click.Path())
@close_cache_shelves_after
def proselint(paths=None, version=None, initialize=None, clean=None,
              debug=None, score=None, output_json=None, time=None, demo=None,
              compact=None):
    """Define the linter command line API."""
    if time:
        click.echo(timing_test())
        return

    # Run the intialization.
    if initialize:
        run_initialization()
        return

    if score:
        click.echo(lintscore())
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
    for fp in filepaths:
        try:
            f = click.open_file(fp, 'r+', encoding="utf-8")
            errors = lint(f, debug=debug)
            num_errors += len(errors)
            show_errors(fp, errors, output_json, compact=compact)
        except:
            pass

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
                        rel_dir = os.path.relpath(dir_, f)
                        rel_file = os.path.join(rel_dir, filename)
                        expanded_files.append(rel_file)

        # Otherwise add the file directly.
        else:
            expanded_files.append(f)

    return expanded_files


if __name__ == '__main__':
    proselint()
