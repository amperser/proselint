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
 - checks for acceptable spacing after ending punctuation
 - (!?) which must be 1 or 2 spaces.
"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import simple_existence_check


def check(text: str) -> list[ResultCheck]:
    """Combine the above tests into one -
    these are quick and should be load-balanced
    """

    results: list[ResultCheck] = []
    results.extend(find_end_punctuation_spacing(text))
    results.extend(find_general_spacing(text))
    results.extend(find_comma_spacing(text))
    return results


def find_end_punctuation_spacing(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "punctuation_spacing.misc.end_punctuation"
    msg = "Unacceptable number of spaces behind ! or ? (must be 1 or 2)."

    pattern = r"[?!]\s{2,} |[?!](?!\s|$)"

    return simple_existence_check(text, pattern, err, msg)


# checks for acceptable behind ,";: which should be no more or less than 1
def find_general_spacing(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "punctuation_spacing.misc.spacing"
    msg = '"Unacceptable number of spaces behind ";: (must be 1)."'

    pattern = r'[;:"]\s{1,} |[;:](;:\s|$])'

    return simple_existence_check(text, pattern, err, msg)


# comma is slightly more complex, consider the number 1,000
def find_comma_spacing(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "punctuation_spacing.misc.comma"
    msg = (
        "Unacceptable number of spaces behind "
        "(must be 1) except when used in numbers."
    )

    pattern = r';:"]\s{2,} |[;:](;:\s|$])'

    return simple_existence_check(text, pattern, err, msg)


# period is complex consider the cases of ellipsis, period between numbers
# as a decimal, period to signify subsections (A.23), period used in
# between abbreviations Washington D.C.
