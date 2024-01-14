"""Checks for acceptable spacing around punctuation.

---
layout:     post
source:     puntuation_spacing.
source_url: https://style.mla.org/colons-how-to-use-them/
title:      Checks for acceptable spacing around punctuation.
date:       2023-04-12
categories: writing
---

Checks for acceptable spacing around punctuation.
 - checks for acceptable spacing after ending punctuation
 - (!?) which must be 1 or 2 spaces.
"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import simple_existence_check


def check_end_punctuation_spacing(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "punctuation.spacing.end_punctuation"
    msg = "Unacceptable number of spaces behind ! or ? (should be 1)."
    pattern = r"[a-z][\?!][ ]{2,}"
    return simple_existence_check(text, pattern, err, msg)


def check_general_spacing(text: str) -> list[ResultCheck]:
    """Checks for acceptable space behind
        , " ; : '
        which should be no more than 1.
    """
    # comma is slightly more complex, consider the number 1,000
    # note: this can be faulty - the previous implementation was far off / defective
    err = "punctuation.spacing.separators"
    msg = 'Unacceptable number of spaces behind ";: (must be 1 or less).'
    pattern = r"""[,;:\"'][ ]{2,}"""
    return simple_existence_check(text, pattern, err, msg)


# Todo: test new checks below


def check_whitespace_before(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "punctuation.whitespace_before"
    msg = "Unacceptable whitespace before punctuation"
    pattern = r"[a-z]+\s[\.!\?]"
    return simple_existence_check(text, pattern, err, msg)


def check_whitespace_inbetween(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "punctuation.whitespace_inbetween"
    msg = "Multiple spaces, that would be ugly in Word or LibreOffice."
    pattern = r"\b  +\b"
    return simple_existence_check(text, pattern, err, msg)


# period is complex consider the cases of ellipsis, period between numbers
# as a decimal, period to signify subsections (A.23), period used in
# between abbreviations Washington D.C.
