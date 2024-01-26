"""Inferior / Superior.

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

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "It was more inferior than the alternative.",
]


def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.inferior_superior"
    msg = "'Inferior' and 'superior' are not true comparatives. Use '{}'."

    items: dict[str, str] = {
        "inferior than": "inferior to",
        "superior than": "superior to",
    }

    return preferred_forms_check_opti(text, items, err, msg)
