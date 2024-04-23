"""Profession.

---
layout:     post
source:
source_url:
title:      Professions
date:       2014-06-10
categories: writing
---

Professions.

"""
from __future__ import annotations

from proselint.checks import CheckResult
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "I really need a shoe repair guy.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "misc.professions"
    msg = "'{}' is the name of that job, not '{}'"

    items: dict[str, str] = {
        "shoe repair guy": "cobbler",
        "geometrist": "geometer",
    }

    return preferred_forms_check_opti(text, items, err, msg)
