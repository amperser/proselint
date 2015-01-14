#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Command line utility for proselint."""
#  to access: run python setup.py develop from the main directory

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
        strunk_white_EoS,
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
    msg = "Comparison of an uncomparable: {} is not comparable."  # do formatting thing

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
            occurrences = [
                m.start() for m in re.finditer(comp + "\s" + uncomp, text.lower())]
            for o in occurrences:
                errors.append((1, o, error_code, msg.format(uncomp)))
    return errors


def strunk_white_EoS(text):
    error_code = "PL002"
    msg = "Don't use the word {}.{}"

    bad_words = [
        "obviously",
        "utilize",
        "personalize"
    ]

    explanations = {
        "obviously":
        "This is obviously an inadvisable word to use.",
        "utilize":
        r"Do you know anyone who *needs* to utilize the word utilize?",
        "personalize":
        r"This is not a personalized message. No one should use personalize."
    }

    errors = []
    for word in bad_words:
        occurrences = [
            m.start() for m in re.finditer(word, text.lower())
        ]
        for o in occurrences:
            errors.append((1, o, error_code, msg.format(word, explanations[word])))
    return errors
