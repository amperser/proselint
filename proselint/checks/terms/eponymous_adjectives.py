"""Eponymous adjectives.

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

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check


def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "terms.eponymous_adjective.garner"
    msg = "'{}' is the preferred eponymous adjective."

    preferences = [
        ["Mephistophelean", ["Mephistophelian"]],
        ["Shakespearean", ["Shakespearian"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
