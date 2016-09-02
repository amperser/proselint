# -*- coding: utf-8 -*-

"""in- vs. un-."""

from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """in- vs un-."""
    err = "spelling.in_un"
    msg = "in- vs. un-. '{}' is the preferred spelling."

    preferences = [

        ["inadvisable",         ["unadvisable"]],
        ["inalienable",         ["unalienable"]],
        ["inexpressive",        ["unexpressive"]],
        ["infeasible",          ["unfeasible"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
