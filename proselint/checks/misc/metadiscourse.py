"""
Metadiscourse.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      metadiscourse
date:       2014-06-10
categories: writing
---

Points out metadiscourse.

"""
from __future__ import annotations

from proselint.checks import CheckResult, existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "It's based on the rest of this article.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "misc.metadiscourse.pinker"
    msg = "Excessive metadiscourse."

    metadiscourse = [
        "The preceeding discussion",
        "The rest of this article",
        "This chapter discusses",
        "The preceding paragraph demonstrated",
        "The previous section analyzed",
    ]

    return existence_check(text, metadiscourse, err, msg)
