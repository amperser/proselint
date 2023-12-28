"""Profession.

---
layout:     post
source:
source_url:
title:      Professions
date:       2014-06-10 12:31:19
categories: writing
---

Professions.

"""
from __future__ import annotations

from proselint.tools import ResultCheck, memoize, preferred_forms_check


@memoize
def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.professions"
    msg = "'{}' is the name of that job."

    preferences = [

        ["cobbler",    ["shoe repair guy"]],
        ["geometer",   ["geometrist"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
