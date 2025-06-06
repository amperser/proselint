"""
Punctuation.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      dates
date:       2014-06-10 12:31:19
categories: writing
---
"""

from proselint.tools import existence_check, max_errors, ppm_threshold


def check_misplaced(text):
    """Check the text."""
    err = "typography.punctuation.misplaced"
    msg = "Misplaced punctuation. It's 'et al.'"

    list = [
        "et. al",
        "et. al."
    ]
    return existence_check(text, list, err, msg, join=True)


@ppm_threshold(30)
def check_exclamations_ppm(text):
    """Make sure that the exclamation ppm is under 30."""
    err = "typography.punctuation.exclamation"
    msg = "More than 30 ppm of exclamations. Keep them under control."

    regex = r"\w!"

    return existence_check(text, [regex], err, msg, require_padding=False)


@max_errors(1)
def check_hyperbole(text):
    """Check the text."""
    err = "typography.punctuation.hyperbole"
    msg = "'{}' is hyperbolic."

    words = [
        r"\w*!{2,}",
        r"\w*\?{2,}"
    ]

    return existence_check(text, words, err, msg)
