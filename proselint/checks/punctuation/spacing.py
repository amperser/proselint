"""
Checks for acceptable spacing around punctuation.

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

from proselint.checks import CheckSpec, ExistenceSimple, Pd

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

check_end_punctuation_spacing = CheckSpec(
    ExistenceSimple(r"[a-z][!\?][ ]{2,}"),
    "punctuation.spacing.end_punctuation",
    "Unacceptable number of spaces behind ! or ? (should be 1).",
)

check_general_spacing = CheckSpec(
    # comma is slightly more complex, consider the number 1,000
    # NOTE: this can break - the previous implementation was defective
    ExistenceSimple(r"""[,;\:\"'][ ]{2,}"""),
    "punctuation.spacing.separators",
    'Unacceptable number of spaces behind ";: (must be 1 or less).',
)

check_whitespace_before = CheckSpec(
    ExistenceSimple(r"[a-z]+\s+[,;\:\.!\?]"),
    "punctuation.whitespace_before",
    "Unacceptable whitespace before punctuation",
)

check_whitespace_inbetween = CheckSpec(
    ExistenceSimple(Pd.words_in_txt.value.format(r"[ ]{2,}")),
    "punctuation.whitespace_inbetween",
    "Multiple spaces, that would be ugly in Word or LibreOffice.",
)

__register__ = (
    check_end_punctuation_spacing,
    check_general_spacing,
    check_whitespace_before,
    check_whitespace_inbetween,
)
