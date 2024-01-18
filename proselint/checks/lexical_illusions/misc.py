"""Lexical illusions.

---
layout:     post
source:     write-good
source_url: https://github.com/btford/write-good
title:      Lexical illusion present
date:       2014-06-10
categories: writing
---

A lexical illusion is when a word word is unintentionally repeated twice, and
and this happens most often between line breaks.

"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import simple_existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
"And he's gone, gone with the breeze",
"You should know that that sentence wasn't wrong.",
"She had had dessert on the balcony.",
"The practitioner's side",
"An antimatter particle",
"The theory",
"She had coffee at the Foo-bar bar.",
]

examples_fail = [
    "Paris in the the springtime.",
"You should know that that that was wrong.",
"She had coffee at the Foo bar bar.",
    "She she coffee at the Foo-bar.",
    "After I write i write i write.",
    "that is an echo is an echo",
    "don't miss the biggest illusion miss the biggest illusion.",
]

def disabled_check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "lexical_illusions.misc"
    msg = "There's a lexical illusion here: a word is repeated."
    regex = r"\b(?<!\-)(\w+)(\b\s\1)+\b"
    exceptions = [r"^had had$", r"^that that$"]
    # TODO: could be removed, regex below finds more, except the unknown "\-" part
    return simple_existence_check(
        text,
        regex,
        err,
        msg,
        exceptions=exceptions,
    )


# TODO: test the checks below


def check_repetitions(text: str) -> list[ResultCheck]:
    """Check the text."""
    # src = "https://github.com/entorb/typonuketool/blob/main/subs.pl"
    err = "lexical_illusions.misc.tnt"
    msg = "There's a lexical illusion in '{}' - one or more words are repeated."
    # check for repetition of 1, 2, 3 or 4 words
    items = [
        r"((?<!\\)\b\w+)\s+\1\b",  # ignores \EA EA
        r"(\b\w+\s+\w+\b)\s+\1\b",
        r"(\b\w+\s+\w+\s+\w+\b)\s+\1\b",
        r"(\b\w+\s+\w+\s+\w+\s+\w+\b)\s+\1\b",
    ]  # note: these can't be padded without mod -> \1
    exceptions = [r"^had had$", r"^that that$"]
    results = []
    for item in items:
        results.extend(
            simple_existence_check(
                text,
                item,
                err,
                msg,
                exceptions=exceptions,
            )
        )
    return results
