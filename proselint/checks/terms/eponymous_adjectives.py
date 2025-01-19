"""
Eponymous adjectives.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Eponymous adjectives
date:       2014-06-10
categories: writing
---

Eponymous adjectives.

"""

from __future__ import annotations

from proselint.checks import CheckSpec, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The writing wasn't Shakespearian.",
]

check = CheckSpec(
    PreferredFormsSimple({
        "Mephistophelian": "Mephistophelean",
        "Shakespearian": "Shakespearean",
    }),
    "terms.eponymous_adjectives.garner",
    "'{}' is the preferred eponymous adjective.",
)

__register__ = (check,)
