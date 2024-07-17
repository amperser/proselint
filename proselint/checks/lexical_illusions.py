"""
Lexical illusions.

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

from proselint.checks import CheckSpec, ExistenceSimple

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
    "Green greenery",
]

examples_fail = [
    "Paris in the the springtime.",
    "You should know that that that was wrong.",
    "She had coffee at the Foo bar bar.",
    "She she coffee at the Foo-bar.",
    "After I write i write i write.",
    "That is an echo is an echo",
    "Don't miss the biggest illusion miss the biggest illusion.",
]


check_repetitions = CheckSpec(
    ExistenceSimple(
        # NOTE: this can't be padded without mod -> \1
        r"\b(?<!\\|\-)(\w+(?:\s+\w+){0,3})(?:\s+\1)+\b",
        exceptions=(r"^had had$", r"^that that$"),
    ),
    "lexical_illusions.misc",
    "There's a lexical illusion in '{}' - one or more words are repeated.",
)

__register__ = (check_repetitions,)
