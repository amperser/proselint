"""Mondegreens.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      mondegreens
date:       2014-06-10
categories: writing
---

Points out preferred form.

"""
from __future__ import annotations

from proselint.checks import CheckResult
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "... and laid him on the green.",
]

examples_fail = [
    "..and Lady Mondegreen.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "mondegreens.misc"
    msg = "'{}' is the preferred form."

    items: dict[str, str] = {
        "a girl with colitis goes by": "a girl with kaleidoscope eyes",
        "a part-red gingerbread tree": "a partridge in a pear tree",
        "attorney and not a republic": "attorney and notary public",
        "beckon call": "beck and call",
        "for all intensive purposes": "for all intents and purposes",
        "Lady Mondegreen": "laid him on the green",
        "Olive, the other reindeer": "all of the other reindeer",
        "to the manor born": "to the manner born",
    }

    return preferred_forms_check_opti(text, items, err, msg)
