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

This check looks for offensive or possibly offensive terms related to LGBTQ
issues and raises an error marking them as such or providing recommended
alternatives. The New York Times and Associated Press have also adopted this
style guide.
"""

from __future__ import annotations

from proselint.checks import CheckSpec, Existence, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "They were a gay couple.",
    "I once met a gay man.",
    "Homosexual.",
]

examples_fail = [
    "He was a homosexual man.",
    "My sexual preference is for women.",
    "I once met a fag.",
]


check = CheckSpec(
    PreferredFormsSimple({
        "homosexual man": "gay man",
        "homosexual men": "gay men",
        "homosexual woman": "lesbian",
        "homosexual women": "lesbians",
        "homosexual people": "gay people",
        "homosexual couple": "gay couple",
        "sexual preference": "sexual orientation",
        "admitted homosexual": "openly gay",
        "avowed homosexual": "openly gay",
        "special rights": "equal rights",
    }),
    "social_awareness.lgbtq.terms.glaad",
    "Possibly offensive term. Consider using '{}' instead of '{}'.",
    # TODO: consider impact of setting ignore_case=True
    ignore_case=False,
)

check_offensive = CheckSpec(
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
    "social_awareness.lgbtq.terms.offensive",
    "Offensive term. Remove it or consider the context.",
    # TODO: consider the impact of setting ignore_case=True
    ignore_case=False,
)

__register__ = (
    check,
    check_offensive,
)
