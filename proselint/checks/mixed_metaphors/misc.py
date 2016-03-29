# -*- coding: utf-8 -*-

"""Mixed metaphors."""

from proselint.tools import memoize, existence_check, preferred_forms_check


@memoize
def check_bottleneck(text):
    """Avoid mixing metaphors about bottles and their necks.

    source:     Sir Ernest Gowers
    source_url: http://bit.ly/1CQPH61
    """
    err = "mixed_metaphors.misc.bottleneck"
    msg = u"Mixed metaphor — bottles with big necks are easy to pass through."
    list = [
        "biggest bottleneck",
        "big bottleneck",
        "large bottleneck",
        "largest bottleneck",
        "world-wide bottleneck",
        "huge bottleneck",
        "massive bottleneck",
    ]

    return existence_check(text, list, err, msg, max_errors=1)


@memoize
def check_misc(text):
    """Avoid mixing metaphors.

    source:     Garner's Modern American Usage
    source_url: http://bit.ly/1T4alrY
    """
    err = "mixed_metaphors.misc.misc"
    msg = u"Mixed metaphor. Try '{}'."

    preferences = [

        ["cream rises to the top",    ["cream rises to the crop"]],
        ["fasten your seatbelts",     ["button your seatbelts"]],
        ["a minute to decompress",    ["a minute to decompose"]],
        ["sharpest tool in the shed", ["sharpest marble in the (shed|box)"]],
        ["not rocket science",        ["not rocket surgery"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
