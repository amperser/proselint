#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Command line utility for proselint."""
from __future__ import print_function
from __future__ import absolute_import
from builtins import str


import click
import os
from .tools import line_and_column, is_quoted
from . import checks as pl
import pkgutil
import subprocess
import ntpath
import re
import json as js
import importlib
import sys
from .score import score
from .version import __version__


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
base_url = "proselint.com/"
proselint_path = os.path.dirname(os.path.realpath(__file__))
demo_file = os.path.join(proselint_path, "demo.md")


def log_error(filename, line, column, error_code, msg):
    """Print the error to the command line."""
    click.echo(ntpath.basename(filename) + ":" +
               str(1 + line) + ":" +
               str(1 + column) + ": " +
               error_code + " " +
               msg)


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
    """Run the linter on the file with the given path."""
    # Load the options.
    options = js.load(open(os.path.join(proselint_path, '.proselintrc')))

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


def show_errors(filename, errors, json=False):
    """Print the errors, resulting from lint, for filename."""
    if json:
        out = []
        for e in errors:
            out.append({
                "check": e[0],
                "message": e[1],
                "line": e[2],
                "column": e[3],
                "start": e[4],
                "end": e[5],
                "extent": e[6],
                "severity": e[7],
                "replacements": e[8],
            })
        result = dict(
            status="success",
            data={"errors": out})

        click.echo(js.dumps(result))

    else:
        for error in errors:

            (check, message, line, column, start, end,
             extent, severity, replacements) = error

            log_error(filename, line, column, check, message)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(__version__, '--version', '-v')
@click.option('--initialize', '-i', is_flag=True)
@click.option('--debug', '-d', is_flag=True)
@click.option('--clean', '-c', is_flag=True)
@click.option('--score', '-s', is_flag=True)
@click.option('--json', '-j', is_flag=True)
@click.option('--time', '-t', is_flag=True)
@click.option('--demo', is_flag=True)
@click.argument('files', nargs=-1, type=click.File(encoding='utf8'))
def proselint(files=None, version=None, initialize=None, clean=None,
              debug=None, score=None, json=None, time=None, demo=None):
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
        files = [click.open_file(demo_file, encoding='utf8')]

    for f in files:
        errors = lint(f, debug=debug)
        show_errors(click.format_filename(f.name), errors, json)

if __name__ == '__main__':
    proselint()
