#
# linter.py
# Linter for SublimeLinter4, a code checking framework for Sublime Text 3
#
# Written by Jordan Suchow
# Copyright (c) 2015 Jordan Suchow
#
# Updated for SublimeLinter 4 by Josh Mitchell 2020
#

"""This module exports the Proselint plugin class."""

from SublimeLinter.lint import Linter, WARNING


class Proselint(Linter):
    """Provides an interface to proselint."""
    cmd = 'proselint'
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): (?P<code>\S*) (?P<message>.+)'
    )
    multiline = True
    line_col_base = (1, 1)
    word_re = r'^([-\w]+)'
    default_type = WARNING
    defaults = {
        "selector": "text",
    }
