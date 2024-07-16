"""
Inferior / Superior.

---
layout:     post
source:     Fowler's Modern English Usage
source_url: bit.ly/1YBG8QJ
title:      Inferior / Superior
date:       2016-03-10
categories: writing
---

Corrects 'inferior/superior than' to 'inferior/superior to'.

"""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "It was more inferior than the alternative.",
]

check = CheckSpec(
    PreferredFormsSimple({
        "inferior than": "inferior to",
        "superior than": "superior to",
    }),
    "misc.inferior_superior",
    "'Inferior' and 'superior' are not true comparatives. Use '{}'.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
