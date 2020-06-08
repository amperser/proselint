# -*- coding: utf-8 -*-

"""Redundancy."""

from proselint.tools import memoize, is_quoted
import re


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "redundancy.adverbdialogue"
    msg = "Redundant adverb. Remove {}."

    # find if any of the text is in quote
    regex = r'[\'"].*[,?!][\'"][\s\w]*?(\w+?ly)[\s\w]*[,.!?]'
    matches = re.finditer(regex, text)
    return [(match.start(1), match.end(1), err, msg.format(
        match.groups(0)[0]), None) for match in matches]
