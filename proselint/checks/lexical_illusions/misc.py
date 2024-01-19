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


matching repetition for one word:
- V0: ((?<!\\)\b\w+)\s+\1\b -> from TNT
    - only detects one repetition
    - ignores latex "\word word"
- V1: \b(?<!\-)(\w+)(\b\s\1)+\b -> from proselint
    - middle \b is expensive & not needed
    - ignores "w1-w2 w2"
- V2: \b(?<!\\|\-)(\w+)(\s\1)+\b
    - combines ignores of V0 & V1
    - still 14.3k steps on demo
- V3 -> see v2 below

Two or more:
- v0: (\b\w+\s+\w+\b)\s+\1\b -> inefficient (19.2k steps on demo)
- v0.1: (\b\w+\s+\w+)\s+\1   -> 15.3k Steps on demo
- v1: (\b\w+\s+\w+)\s+\1     -> 15.5k Steps on demo
- v2: \b(?<!\\|\-)(\w+(\s+\w+){0,3})(\s+\1)+\b -> 30k steps
    - replaces all individual regex

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
    "Don't just play the game - play the game.",
    "green greenery",
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


def check_repetitions(text: str) -> list[ResultCheck]:
    """Check the text."""
    # src = "https://github.com/entorb/typonuketool/blob/main/subs.pl"
    err = "lexical_illusions.misc.tnt"
    msg = "There's a lexical illusion in '{}' - one or more words are repeated."
    # check for repetition of 1 to 4 words
    regex = r"\b(?<!\\|\-)(\w+(\s+\w+){0,3})(\s+\1)+\b"
    # note: this can't be padded without mod -> \1
    exceptions = [r"^had had$", r"^that that$"]
    return simple_existence_check(
                text,
                regex,
                err,
                msg,
                exceptions=exceptions,
            )
