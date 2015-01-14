#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Command line utility for proselint."""

import click
import os
import imp


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

    # Extract functions from the checks folder.
    checks = []

    listing = os.listdir(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "checks"))

    for f in listing:
        if f[-3:] == ".py" and not f == "__init__.py":
            m = imp.load_source("rule", os.path.join("proselint", "checks", f))
            checks.append(getattr(m, 'check'))

    # Return the version number.
    if version:
        print "v0.0.1"

    # Apply all the checks.
    else:
        with open(file, "r") as f:
            text = f.read()
            for check in checks:
                errors = check(text)
                for error in errors:
                    log_error(*error)
