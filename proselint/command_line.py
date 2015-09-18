#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Command line utility for proselint."""
from __future__ import print_function
from __future__ import absolute_import
from builtins import input
from builtins import str
from builtins import int


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
import time
import importlib
import sys
from .version import __version__


base_url = "prose.lifelinter.com/"
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
    check_names = [key for (key, val) in options["checks"].items() if val]
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
                start_time = time.time()

            result = check(text)

            for error in result:
                (start, end, check, message) = error
                (line, column) = line_and_column(text, start)
                if not is_quoted(start, text):
                    errors += [(check, message, line, column, start, end,
                               end - start, "warning", None)]

            if debug:
                print(time.time() - start_time)

            if len(errors) > options["max_errors"]:
                break

        # Sort the errors by line and column number.
        errors = sorted(errors[:options["max_errors"]])

    return errors


def lintscore():
    """Compute the linter's score on a corpus.

    Proselint's score reflects the desire to have a linter that catches many
    errors, but which takes false alarms seriously. It is better not to say
    something than to say the wrong thing, and the harm from saying the wrong
    thing is more than the benefit of saying the right thing. Thus our score
    metric is defined as:
        TP * (TP / (FP + TP)) ^ k,
    where TP is the number of true positives (hits), FP is the number of
    false positives (false alarms), and k > 0 is a temperature parameter that
    determines the penalty for imprecision. In general, we should choose a
    large value of k that strongly discourages the creating of rules that can't
    be trusted. Suppose that k = 2. Then if the linter detects 100 errors, of
    which 10 are false positives, the score is 81.
    """
    tp = 0
    fp = 0

    parent_directory = os.path.dirname(proselint_path)
    path_to_corpus = os.path.join(parent_directory, "tests", "corpus")
    for root, _, files in os.walk(path_to_corpus):
        files = [f for f in files if f.endswith(".md")]
        for f in files:
            fullpath = os.path.join(root, f)

            # Run the linter.
            print("Linting {}".format(f))
            out = subprocess.check_output(
                "proselint {}".format(fullpath), shell=True)

            # Determine the number of errors.
            regex = r".+?:(?P<line>\d+):(?P<col>\d+): (?P<message>.+)"
            num_errors = len(tuple(re.finditer(regex, out)))
            print("Found {} errors.".format(num_errors))

            # Open the document.
            subprocess.call("{} {}".format("open", fullpath), shell=True)

            # Ask the scorer how many of the errors were false alarms?
            input_val = None
            while not isinstance(input_val, int):
                try:
                    input_val = input("# of false alarms? ")
                    if input_val == "exit":
                        return
                    else:
                        input_val = int(input_val)
                        fp += input_val
                        tp += (num_errors - input_val)
                except:
                    pass

            print("Currently {} hits and {} false alarms\n---".format(tp, fp))

    return tp * (1.0 * tp / (tp + fp)) ** 2


@click.command()
@click.option('--version/--whatever', default=None)
@click.option('--initialize/--i', default=None)
@click.option('--debug/--d', default=False)
@click.option('--score/--s', default=False)
@click.option('--json/-j', default=False)
@click.argument('file', default=False)
def proselint(file=None, version=None, initialize=None,
              debug=None, score=None, json=False):
    """Define the linter command line API."""
    # Return the version number.
    if version:
        print(__version__)
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
        print("Deleting the cache...")
        path_of_this_file = os.path.dirname(os.path.realpath(__file__))
        subprocess.call("find . -name '*.pyc' -delete", shell=True)
        subprocess.call(
            "rm -rfv proselint/cache > /dev/null && mkdir -p {}".format(
                os.path.join(path_of_this_file, "cache")),
            shell=True)

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
