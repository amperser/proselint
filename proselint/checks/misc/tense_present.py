"""
Tense present.

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

from proselint.checks import CheckSpec, Existence, Pd

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

name = "misc.tense_present"
# TODO: add some actual context, explanation, or advice
msg = "'{}'."

check = CheckSpec(
    Existence(
        [
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
        ],
        unicode=True,
    ),
    name,
    msg,
    ignore_case=True,
)

check_2 = CheckSpec(
    Existence(
        [r"\bup to \d{1,3}% ?[-\u2014\u2013]{0,3} ?(?:or|and) more\W?"],
        unicode=True,
        padding=Pd.disabled,
    ),
    name,
    msg,
    ignore_case=True,
)

__register__ = (
    check,
    check_2,
)
