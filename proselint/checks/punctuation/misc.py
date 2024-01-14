"""Punctuation.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Punctuation
date:       2014-06-10
categories: writing
---

Dates.

"""
from __future__ import annotations

from proselint.checks import Pd
from proselint.checks import ResultCheck
from proselint.checks import existence_check
from proselint.checks import simple_existence_check


def check_garner(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "punctuation.misc.garner"
    msg = "Misplaced punctuation. It's 'et al.'"

    items = [
        "et. al",
        "et. al.",
    ]
    return existence_check(text, items, err, msg)


# TODO: test the checks below


def check_lower_case_after_punctuation(text: str) -> list[ResultCheck]:
    """can have false positives after abbreviations"""
    # src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L325
    err = "punctuation.misc.lower_case"
    msg = "Is the lower case letter correct after the punctuation?"
    regex = r"\b[a-z]+[\.!\?]\s+[a-z]+\b"
    exceptions = ["al.", "lat.", "vs.", "etc.", "Prof.", "Dr."]  # en, TODO: add more
    # exceptions_de = ["bzw.", "ca.", "cf.", "etc.", "vgl.", "no.", "m.E", "m.a.W.", "u.U.", "s.u.", "z.B."]
    return simple_existence_check(
        text, regex, err, msg, ignore_case=False, exceptions=exceptions
    )


def check_comma_digits(text: str) -> list[ResultCheck]:
    # src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L325
    # note: tnt has also check for german numbers, not implemented here
    err = "punctuation.misc.comma_digits"
    msg = "In English ',' is used as decimal separator."
    regex = Pd.sep_in_txt.value.format(r"\d+,\d+")

    return simple_existence_check(text, regex, err, msg)
