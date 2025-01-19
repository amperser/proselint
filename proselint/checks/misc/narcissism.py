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

from proselint.checks import CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "In recent years, an increasing number of scientists "
    "have studied the problem in detail.",
]

check = CheckSpec(
    Existence([
        "In recent years, an increasing number of [a-zA-Z]{3,}sts have"
    ]),
    "misc.narcissism",
    "Professional narcissism. Talk about the subject, not its study.",
)

__register__ = (check,)
