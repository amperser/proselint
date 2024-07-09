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

from proselint.checks import CheckResult, Pd, existence_check, registry

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


def check(text: str) -> list[CheckResult]:
    """Do not start a paragraph with a 'But'."""
    err = "misc.but"
    msg = "No paragraph or sentence should start with a 'But'."
    # regex = r"(^|([\n\r\.]+))(\s*)But"
    regex = r"\b(?:^|[\.!\?]\s*)But\b"  # more powerful & 50% less computation

    return existence_check(
        text, [regex], err, msg, ignore_case=False, padding=Pd.disabled
    )


registry.register("misc.but", check)
