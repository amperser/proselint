"""find repeated beginnings of sections, sentences,

---
layout:     post
source:     TypoNukeTool
source_url: https://github.com/entorb/typonuketool/blob/main/subs.pl#L284C12-L284C65
title:      monotonic writing
date:       2024-01-14
categories: writing
---


"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import existence_check_simple

examples_pass = [
    "Smoke phrase with nothing flagged.",
    """I like to tell you something:
I am a fan of superman.""",
]

examples_fail = [
    "The sentence is easy. The clock is round.",
    """I like to read and sleep.
I am a fan of superman.""",
]


def check_sentence(text: str) -> list[ResultCheck]:
    """can have false positives after abbreviations"""
    err = "misc.monotonic.sentence"
    msg = (
        "It is bad style to open consecutive sentences with the same word, "
        "here '{}'."
    )

    regex = r"([\.!\?]\s+|^)([A-Z][a-z]*\b)[^\.!\?]+[\.!?]\s+\2\b(\s+[a-z]*)"
    # matches identical words starting uppercase after either newline or .!?
    # note: can't be padded without modification -> because of \2
    return existence_check_simple(text, regex, err, msg, ignore_case=False)


# TODO: check same line/section-beginning
