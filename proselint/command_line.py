#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Command line utility for proselint."""

import click
import os
import imp
from proselint.tools import line_and_column

base_url = "prose.lifelinter.com/"
proselint_path = os.path.dirname(os.path.realpath(__file__))


def log_error(filename, line, column, error_code, msg):
    """Print a message to the command line."""
    click.echo(filename + ":" +
               str(1 + line) + ":" +
               str(1 + column) + ": " +
               error_code + " " +
               msg + " " + base_url + error_code)


@click.command()
@click.option('--version/--whatever', default=False)
@click.argument('file', default=False)
def proselint(version, file):
    """Run the linter."""

    # Return the version number.
    if version:
        print "v0.0.1"
        return

    if not file:
        raise ValueError("Specify a file to lint using the --file flag.")

    # Extract functions from the checks folder.
    checks = []

    listing = os.listdir(
        os.path.join(proselint_path, "checks"))

    for f in listing:
        if f[-3:] == ".py" and not f == "__init__.py":
            m = imp.load_source("", os.path.join(proselint_path, "checks", f))
            checks.append(getattr(m, 'check'))

    # Apply all the checks.
    else:
        with open(file, "r") as f:
            text = f.read()
            for check in checks:
                errors = check(text)
                if errors:
                    for error in errors:
                        (start, end, error_code, msg) = error
                        (line, column) = line_and_column(text, start)
                        log_error(file, line, column, error_code, msg)
