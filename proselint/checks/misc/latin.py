"""
Back-formations.

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

from proselint.checks import CheckRegistry, CheckSpec, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "And ceteris paribus, it was good.",
]

check = CheckSpec(
    PreferredFormsSimple({
        "ceteris paribus": "other things being equal",
        "inter alia": "among other things",
        "simpliciter": "in and of itself",
        "mutatis mutandis": "having made the necessary changes",
    }),
    "misc.latin.pinker",
    "Use English. '{}' is the preferred form.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
