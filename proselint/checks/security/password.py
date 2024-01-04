"""Password in plain text.

---
layout:     post
source:     ???
source_url: ???
title:      password in plain text
date:       2014-06-10 12:31:19
categories: writing
---

Don't put pass
"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import existence_check


def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "security.password"
    msg = "Don't put passwords in plain text."

    _regex = r"[:]? [\S]{6,30}"

    items = [
        f"the password is{_regex}",
        f"my password is{_regex}",
        f"the password's{_regex}",
        f"my password's{_regex}",
        f"^[pP]assword{_regex}",
    ]

    return existence_check(text, items, err, msg)
