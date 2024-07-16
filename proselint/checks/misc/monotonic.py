"""
Find repeated beginnings of sections and sentences.

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

from proselint.checks import CheckRegistry, CheckSpec, ExistenceSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
    """I want to tell you something:
I am a fan of superman.""",
]

examples_fail = [
    "The sentence is easy. The clock is round.",
    """I like to read and sleep.
I am a fan of superman.""",
]


check_sentence = CheckSpec(
    # matches identical words starting uppercase after either newline or .!?
    # NOTE: can't be padded without modification -> because of \2
    ExistenceSimple(
        r"([\.!\?]\s+|^)([A-Z][a-z]*\b)[^\.!\?]+[\.!?]\s+\2\b(\s+[a-z]*)"
    ),
    "misc.monotonic.sentence",
    "It is bad style to open consecutive sentences with the same word in '{}'.",
    ignore_case=False,
)

# TODO: check same line/section-beginning


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check_sentence)
