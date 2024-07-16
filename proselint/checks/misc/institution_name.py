"""
Common errors with institution names.

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

from proselint.checks import CheckRegistry, CheckSpec, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "I went to the Virginia Polytechnic and State University.",
]

check_vtech = CheckSpec(
    PreferredFormsSimple({
        "Virginia Polytechnic and State University": "Virginia Polytechnic "
        "Institute and State University",
    }),
    "misc.institution.vtech",
    "Incorrect name. Use '{}' instead of '{}'.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check_vtech)
