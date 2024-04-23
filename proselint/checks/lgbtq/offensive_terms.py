"""GLAAD.

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

from proselint.checks import CheckResult
from proselint.checks import existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "I once met a gay man.",
]

examples_fail = [
    "I once met a fag.",
]


def check(text: str) -> list[CheckResult]:
    """Flag offensive words based on the GLAAD reference guide."""
    err = "lgbtq.offensive_terms.glaad"
    msg = "Offensive term. Remove it or consider the context."

    items = [
        "fag",
        "faggot",
        "dyke",
        "sodomite",
        "homosexual agenda",
        "gay agenda",
        "transvestite",
        "homosexual lifestyle",
        "gay lifestyle",
        # homo - may create false positives without additional context
        # FIXME use topic detector to decide whether "homo" is offensive
    ]

    return existence_check(text, items, err, msg, ignore_case=False)
