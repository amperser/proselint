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

from proselint.checks import CheckResult
from proselint.checks import existence_check_simple

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "The quick brown fox jumps; over the lazy dog!",
    "The quick brown fox jumps:over the lazy dog!",
    "The quick brown fox jumps! over the lazy dog!",
    "The quick brown fox jumps? over the lazy dog!",
    "The quick brown fox jumps. over the lazy dog!",
    "subsections A.23 or (B.25)",
    "period used in between abbreviations Washington D.C.",
]

examples_fail = [
    "flagged!  ",
    "flagged!    ",
    "flagged?  ",
    "flagged?    ",
    "The quick brown fox jumps;  over the lazy dog!",
    "The quick brown fox jumps  :over the lazy dog!",
    "The quick brown fox jumps  ;over the lazy dog!",
    "The quick brown fox jumps  ,over the lazy dog!",
    "The quick brown fox jumps  over the lazy dog!",
    "The quick brown fox jumps  !over the lazy dog!",
    "The quick brown fox jumps  ?over the lazy dog!",
    "The quick brown fox jumps  .over the lazy dog!",
]


def check_end_punctuation_spacing(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "punctuation.spacing.end_punctuation"
    msg = "Unacceptable number of spaces behind ! or ? (should be 1)."
    pattern = r"[a-z][!\?][ ]{2,}"
    return existence_check_simple(text, pattern, err, msg)


def check_general_spacing(text: str) -> list[CheckResult]:
    """Checks for acceptable space behind
    , " ; : '
    which should be no more than 1.
    """
    # comma is slightly more complex, consider the number 1,000
    # note: this can be faulty - the previous implementation was far off / defective
    err = "punctuation.spacing.separators"
    msg = 'Unacceptable number of spaces behind ";: (must be 1 or less).'
    pattern = r"""[,;\:\"'][ ]{2,}"""
    return existence_check_simple(text, pattern, err, msg)


def check_whitespace_before(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "punctuation.whitespace_before"
    msg = "Unacceptable whitespace before punctuation"
    pattern = r"[a-z]+\s+[,;\:\.!\?]"
    return existence_check_simple(text, pattern, err, msg)


def check_whitespace_inbetween(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "punctuation.whitespace_inbetween"
    msg = "Multiple spaces, that would be ugly in Word or LibreOffice."
    pattern = r"\b[ ]{2,}\b"
    return existence_check_simple(text, pattern, err, msg)
