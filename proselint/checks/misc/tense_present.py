"""Tense present.

---
layout:     post
source:     DFW's Tense Present
source_url: http://bit.ly/1c85lgR
title:      Tense present
date:       2014-06-10
categories: writing
---

Archaism.

"""
from __future__ import annotations

from proselint.checks import Pd
from proselint.checks import CheckResult
from proselint.checks import existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "I did it by accident honestly.",
]

examples_fail = [
    "I did it on accident honestly.",
    "I did it On accident honestly.",
    "Told you something between you and i.",
    "Told you something between you and I.",
    "I feel nauseous.",
]


def check(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "misc.tense_present"
    msg = "'{}'."

    items1 = [
        "between you and I",
        "on accident",
        "somewhat of a",
        "all it's own",
        "reason is because",
        "audible to the ear",
        "in regards to",
        "would of",
        # "and so",
        r"i ?(?:feel|am feeling|am|'m|'m feeling) nauseous",
    ]
    ret1 = existence_check(
        text,
        items1,
        err,
        msg,
        ignore_case=True,
        string=True,
    )

    items2 = [
        r"\bup to \d{1,3}% ?[-\u2014\u2013]{0,3} ?(?:or|and) more\W?",
    ]
    ret2 = existence_check(
        text,
        items2,
        err,
        msg,
        ignore_case=True,
        string=True,
        padding=Pd.disabled,
    )

    return ret1 + ret2
