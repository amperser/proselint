"""Eponymous adjectives.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Eponymous adjectives
date:       2014-06-10
categories: writing
---

Eponymous adjectives.

"""
from __future__ import annotations

from proselint.checks import CheckResult
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The writing wasn't Shakespearian.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "terms.eponymous_adjective.garner"
    msg = "'{}' is the preferred eponymous adjective."

    items: dict[str, str] = {
        "Mephistophelian": "Mephistophelean",
        "Shakespearian": "Shakespearean",
    }

    return preferred_forms_check_opti(text, items, err, msg)
