"""Back-formations.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      back-formations
date:       2014-06-10
categories: writing
---

Back-formations.

"""
from __future__ import annotations

from proselint.checks import CheckResult
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "It is an improprietous use.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "misc.back_formations"
    msg = "Back-formation. '{}' is the preferred form."

    items = {"improprietous": "improper"}

    return preferred_forms_check_opti(text, items, err, msg)
