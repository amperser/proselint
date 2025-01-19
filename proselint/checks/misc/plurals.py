"""
False plurals.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      False plurals.
date:       2014-06-10
categories: writing
---

Using the incorrect form of the plural.

"""

from __future__ import annotations

from proselint.checks import (
    CheckSpec,
    Existence,
    PreferredFormsSimple,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "There were several phenomenons.",
    "I give you many kudos.",
]

check = CheckSpec(
    PreferredFormsSimple({
        "talismen": "talismans",
        "phenomenons": "phenomena",
    }),
    "misc.plurals.misc",
    "The plural is {} and not {}",
)

check_kudos = CheckSpec(
    Existence(["many kudos"]),
    "misc.plurals.kudos",
    "Kudos is singular.",
)

__register__ = (
    check,
    check_kudos,
)
