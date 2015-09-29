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
import codecs
import subprocess
import ntpath
import re
import json as js
import importlib
import sys
from .score import score
from .version import __version__


base_url = "proselint.com/"
proselint_path = os.path.dirname(os.path.realpath(__file__))


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


def lint(path, debug=False):
    """Run the linter on the file with the given path."""
    # Load the options.
    proselint_path = os.path.dirname(os.path.realpath(__file__))
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
    errors = []
    with codecs.open(path, "r", encoding='utf-8') as f:
        text = f.read()
        errors = []
        for check in checks:
            if debug:
                print(check.__module__ + "." + check.__name__)

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
    print("Deleting the cache...")
    path_of_this_file = os.path.dirname(os.path.realpath(__file__))
    subprocess.call("find . -name '*.pyc' -delete", shell=True)
    subprocess.call(
        "rm -rfv proselint/cache > /dev/null && mkdir -p {}".format(
            os.path.join(path_of_this_file, "cache")),
        shell=True)


@click.command()
@click.option('--version/--whatever', default=None)
@click.option('--initialize/--i', default=None)
@click.option('--debug/--d', default=False)
@click.option('--score/--s', default=False)
@click.option('--json/--j', default=False)
@click.option('--time/--t', default=False)
@click.argument('file', default=False)
def proselint(file=None, version=None, initialize=None,
              debug=None, score=None, json=None, time=None):
    """Define the linter command line API."""
    # Return the version number.
    if version:
        print(__version__)
        return

    if time:
        print(timing_test())
        return

    # Run the intialization.
    if initialize:
        run_initialization()
        return

    if score:
        click.echo(lintscore())
        return

    # In debug mode, delete the cache and *.pyc files before running.
    if debug:
        clear_cache()

    # Use the demo file by default.
    if not file:
        file = os.path.join(proselint_path, "demo.md")

    errors = lint(file, debug=debug)

    # Display the errors.
    if json:
        print(errors)
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

        print(js.dumps(result))

    else:
        for error in errors:

            (check, message, line, column, start, end,
                extent, severity, replacements) = error

            log_error(file, line, column, check, message)

if __name__ == '__main__':
    proselint()
