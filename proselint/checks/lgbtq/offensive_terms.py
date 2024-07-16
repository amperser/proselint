"""
GLAAD.

---
layout:     post
source:     GLAAD Media Reference Guide - 9th Edition
source_url: http://www.glaad.org/reference
title:      GLAAD Guidelines
date:       2016-07-06
categories: writing
---

This check looks for offensive terms related to LGBTQ issues and
raises an error marking them as offensive. The New York Times and
Associated Press have also adopted this style guide.

"""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "I once met a gay man.",
]

examples_fail = [
    "I once met a fag.",
]


check = CheckSpec(
    Existence([
        "fag",
        "faggot",
        "dyke",
        "sodomite",
        "homosexual agenda",
        "gay agenda",
        "transvestite",
        "homosexual lifestyle",
        "gay lifestyle",
        # homo may create false positives without additional context
        # FIXME: use topic detector to decide whether "homo" is offensive
    ]),
    "lgbtq.offensive_terms.glaad",
    "Offensive term. Remove it or consider the context.",
    # TODO: consider the impact of setting ignore_case=True
    ignore_case=False,
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
