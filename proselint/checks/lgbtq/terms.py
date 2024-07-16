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

This check looks for possibly offensive terms related to LGBTQ issues and
makes more acceptable recommendations. TheNew York Times and
Associated Press have also adopted this style guide.

"""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "They were a gay couple.",
    "Homosexual.",
]

examples_fail = [
    "He was a homosexual man.",
    "My sexual preference is for women.",
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
    "lgbtq.terms.glaad",
    "Possibly offensive term. Consider using '{}' instead of '{}'.",
    # TODO: consider impact of setting ignore_case=True
    ignore_case=False,
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
