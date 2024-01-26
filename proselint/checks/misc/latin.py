"""Back-formations.

---
layout:     post
source:     The sense of style
source_url: http://amzn.to/1EOUZ5g
title:      back-formations
date:       2014-06-10
categories: writing
---

Back-formations.

"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "And ceteris paribus, it was good.",
]


def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.latin.pinker"
    msg = "Use English. '{}' is the preferred form."

    items: dict[str, str] = {
        "ceteris paribus": "other things being equal",
        "inter alia": "among other things",
        "simpliciter": "in and of itself",
        "mutatis mutandis": "having made the necessary changes",
    }

    return preferred_forms_check_opti(text, items, err, msg)
