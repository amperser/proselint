"""Excessive apologizing.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      excessive apologizing
date:       2014-06-10
categories: writing
---

Points out excessive apologizing.

"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import existence_check


def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.apologizing.pinker"
    msg = "Excessive apologizing."

    narcissism = [
        "More research is needed",
    ]

    return existence_check(text, narcissism, err, msg)
