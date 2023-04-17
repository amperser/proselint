"""Checks for acceptable spacing around punctuation.

---
layout:     post
source:     puntuation_spacing.
source_url: https://style.mla.org/colons-how-to-use-them/
title:      Checks for acceptable spacing around punctuation.
date:       2023-04-12 12:31:19
categories: writing
---

Checks for acceptable spacing around punctuation.

"""
from proselint.tools import memoize, punctuation_check

# checks for acceptable spacing after ending punctuation
# (!?) which must be 1 or 2 spaces.


@memoize
def end_punctuation_spacing_check(text):
    """Check the text."""
    err = "punctuation_spaces.punctuation_spaces"
    msg = "Unacceptable number of spaces behind ! or ? (must be 1 or 2)."

    pattern = r'[?!]\s{2,} |[?!](?!\s|$)'

    return punctuation_check(text, pattern, err, msg)


# checks for acceptable behind ,";: which should be no more or less than 1
@memoize
def general_spacing_check(text):
    """Check the text."""
    err = "punctuation_spaces.punctuation_spaces"
    msg = '"Unacceptable number of spaces behind ";: (must be 1)."'

    pattern = r'[;:"]\s{1,} |[;:](;:\s|$])'

    return punctuation_check(text, pattern, err, msg)


# comma is slightly more complex, consider the number 1,000
@memoize
def comma_spacing_check(text):
    """Check the text."""
    err = "punctuation_spaces.punctuation_spaces"
    msg = """Unacceptable number of spaces behind ",
             (must be 1) except when used in numbers."""

    pattern = r';:"]\s{2,} |[;:](;:\s|$])'

    return punctuation_check(text, pattern, err, msg)
# period is complex consider the cases of ellipsis, period between numbers
# as a decimal, period to signify subsections (A.23), period used in
# between abreviations Washington D.C.
