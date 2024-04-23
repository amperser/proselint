"""Common errors with institution names.

---
layout:     post
source:     Institution's webpage
source_url: http://bit.ly/2en1zbv,
title:      Institution Name
date:       2016-11-16
categories: writing
---

Institution names.

"""
from __future__ import annotations

from proselint.checks import CheckResult
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "I went to the Virginia Polytechnic and State University.",
]


def check_vtech(text: str) -> list[CheckResult]:
    """Suggest the correct name.

    source: Virginia Tech Division of Student Affairs
    source_url: http://bit.ly/2en1zbv
    """
    err = "misc.institution.vtech"
    msg = "Incorrect name. Use '{}' instead of '{}'."

    items: dict[str, str] = {
        "Virginia Polytechnic and State University": "Virginia Polytechnic Institute "
        "and State University"
    }

    return preferred_forms_check_opti(text, items, err, msg)
