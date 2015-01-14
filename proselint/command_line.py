#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Command line utility for proselint."""

import click
import re


def log_error(line, column, error_code, msg):
    """Print a message to the command line."""
    click.echo(str(line) + ":" +
               str(column) + " \t" +
               error_code + ": " +
               msg + " " +
               "http://lifelinter.com/" + error_code)


@click.command()
@click.option('--version/--whatever', default=False)
@click.argument('file', default=False)
def proselint(version, file):
    """Run the linter."""

    checks = [
        example_check,
        dfw_uncomparables,
    ]

    if version:
        print "v0.0.1"

    else:
        with open(file, "r") as f:
            text = f.read()
            for check in checks:
                errors = check(text)
                for error in errors:
                    log_error(*error)


def example_check(text):
    """docstring for example_check"""

    error_code = "PL000"
    msg = "First line always has an error."

    return [(1, 1, error_code, msg)]


def dfw_uncomparables(text):

    error_code = "PL001"
    msg = "Comparison of an uncomparable."  # do formatting thing

    comparators = [
        "very",
        "more",
        "less",
        "extremely",
        "increasingly"
    ]

    uncomparables = [
        "unique",
        "correct",
        "inevitable",
        "possible",
        "false",
        "true"
    ]

    errors = []
    for comp in comparators:
        for uncomp in uncomparables:
            occurences = [
                m.start() for m in re.finditer(comp + "\s" + uncomp, text)]
            for o in occurences:
                errors.append((1, o, error_code, msg))
    return errors
