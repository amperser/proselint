#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Command line utility for proselint."""

import click
import os
from proselint.tools import line_and_column
import proselint.checks as pl
import pkgutil
import codecs
import subprocess
import ntpath
import re


base_url = "prose.lifelinter.com/"
proselint_path = os.path.dirname(os.path.realpath(__file__))


def log_error(filename, line, column, error_code, msg):
    """Print the error to the command line."""
    click.echo(ntpath.basename(filename) + ":" +
               str(1 + line) + ":" +
               str(1 + column) + ": " +
               error_code + " " +
               msg + " " + base_url + error_code)


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


def lint(path):
    """Run the linter on the file with the given path."""
    # Extract functions from the checks folder.
    checks = []
    for loader, module_name, is_pkg in pkgutil.walk_packages(pl.__path__):
        module = loader.find_module(module_name).load_module(module_name)
        for d in dir(module):
            if re.match("check", d):
                checks.append(getattr(module, d))

    # Apply all the checks.
    with codecs.open(path, "r", encoding='utf-8') as f:
        text = f.read()
        errors = []
        for check in checks:
            errors += check(text)

        # Sort the errors by line and column number.
        errors = sorted(errors)

        # Display the errors.
        for error in errors:
            (start, end, error_code, msg) = error
            (line, column) = line_and_column(text, start)
            log_error(path, line, column, error_code, msg)

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
        for f in files:
            fullpath = os.path.join(root, f)

            # Run the linter.
            print "Linting {}".format(f)
            out = subprocess.check_output(
                "proselint {}".format(fullpath), shell=True)

            # Determine the number of errors.
            regex = r".+?:(?P<line>\d+):(?P<col>\d+): (?P<message>.+)"
            num_errors = len(tuple(re.finditer(regex, out)))
            print "Found {} errors.".format(num_errors)

            # Open the document.
            subprocess.call("{} {}".format("open", fullpath), shell=True)

            # Ask the scorer how many of the errors were false alarms?
            input = None
            while not isinstance(input, (int, long)):
                try:
                    input = raw_input("# of false alarms? ")
                    if input == "exit":
                        return
                    else:
                        input = int(input)
                        fp += input
                        tp += (num_errors - input)
                except:
                    pass

            print "Currently {} hits and {} false alarms\n---".format(tp, fp)

    return tp * (1.0 * tp / (tp + fp)) ** 2


@click.command()
@click.option('--version/--whatever', default=None)
@click.option('--initialize/--i', default=None)
@click.option('--debug/--d', default=False)
@click.option('--score/--s', default=False)
@click.argument('file', default=False)
def proselint(
        file=None, version=None, initialize=None, debug=None, score=None):
    """Define the linter command line API."""
    # Return the version number.
    if version:
        print "v0.0.1"
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
        print "Deleting the cache..."
        subprocess.call("find . -name '*.pyc' -delete", shell=True)
        subprocess.call(
            "rm -rfv proselint/cache > /dev/null && mkdir proselint/cache",
            shell=True)

    # Use the demo file by default.
    if not file:
        file = os.path.join(os.path.dirname(proselint_path), "demo.md")

    return lint(file)


if __name__ == '__main__':
    proselint()
