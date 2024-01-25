"""Tense present.

---
layout:     post
source:     DFW's Tense Present
source_url: http://bit.ly/1c85lgR
title:      Tense present
date:       2014-06-10 12:31:19
categories: writing
---

Archaism.

"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import existence_check


def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "misc.tense_present"
    msg = "'{}'."

    illogics = [
        r"up to \d{1,3}% ?[-\u2014\u2013]{0,3} ?(?:or|and) more\W?",
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

    return existence_check(
        text,
        illogics,
        err,
        msg,
        ignore_case=True,
        string=True,
    )
