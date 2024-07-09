"""
Professional narcissism.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      professional narcissism
date:       2014-06-10
categories: writing
---

Points out academic narcissism.

"""
from __future__ import annotations

from proselint.checks import CheckResult, existence_check, registry

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "In recent years, an increasing number of scientists "
    "have studied the problem in detail.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "misc.narcissism"
    msg = "Professional narcissism. Talk about the subject, not its study."

    narcissism = [
        "In recent years, an increasing number of [a-zA-Z]{3,}sts have",
    ]

    return existence_check(text, narcissism, err, msg)


registry.register("misc.narcissism", check)
