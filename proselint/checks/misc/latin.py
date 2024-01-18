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
from proselint.checks import preferred_forms_check

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

    items = [
        ["other things being equal", ["ceteris paribus"]],
        ["among other things", ["inter alia"]],
        ["in and of itself", ["simpliciter"]],
        ["having made the necessary changes", ["mutatis mutandis"]],
    ]

    return preferred_forms_check(text, items, err, msg)
