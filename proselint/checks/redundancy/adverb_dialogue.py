# -*- coding: utf-8 -*-

"""Redundancy."""

from proselint.tools import memoize, existence_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "redundancy.adverb_dialogue"
    msg = "Redundant adverb. Remove {}."

    regex = r'[\'"].*[,?!][\'"][\s\w]*?(\w+?ly)[\s\w]*[,.!?]'

    return existence_check(text, [regex], err, msg)
