"""
Don't start a paragraph with 'But'.

---
layout:     post
source:     Justin Jungé
source_url:
title:      paragraph-start-with-but
date:       2016-03-10
categories: writing
---

Paragraphs should not start with certain bad words.

"""

from __future__ import annotations

from proselint.checks import CheckSpec, Existence, Pd

examples_pass = [
    "Smoke phrase with nothing flagged.",
    """I never start with the word "but",
but might use it after a linebreak.""",
    "Butter is the best.",
]

examples_fail = [
    'But I never start with the word "but".',
    "But why are you like that.",
    "This is cool! But that not so much.",
    "Is this cool? But that not so much.",
]

check = CheckSpec(
    Existence(
        [r"\b(?:^|[\.!\?]\s*)But\b"],
        # TODO: the above regex is functionally equivalent to Pd.words_in_txt
        # so why not use it?
        padding=Pd.disabled,
    ),
    "misc.but",
    "No paragraph or sentence should start with a 'But'.",
    ignore_case=False,
)

__register__ = (check,)
