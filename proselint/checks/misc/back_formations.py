"""Back-formations.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      back-formations
date:       2014-06-10 12:31:19
categories: writing
---

Back-formations.

"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check


def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.back_formations"
    msg = "Back-formation. '{}' is the preferred form."

    items = [
        ["improper", ["improprietous"]],
    ]

    return preferred_forms_check(text, items, err, msg)
