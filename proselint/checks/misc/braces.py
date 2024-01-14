"""Finds unmatched braces.

---
layout:     post
source:     TNT
source_url: https://github.com/entorb/typonuketool/blob/main/subs.pl#L458
title:      braces
date:       2024-01-14
categories: writing
---

"""
from __future__ import annotations

import re

from proselint.checks import ResultCheck

# TODO: test the checks below


def check_unmatched(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "misc.braces.unmatched"
    # msg = "Don't fail to match / close opened braces '{}'."

    def runner(_text: str, char1: str, char2: str) -> ResultCheck:
        _count = 0
        for _m in re.finditer(f"[\\{char1}\\{char2}]", text):
            if _m.group(0) == char1:
                _count += 1
            elif _m.group(0) == char2:
                _count -= 1
            if _count < 0:
                # TODO: this could trigger false positives for counting like 1), 2), a)
                _msg = (
                    "Don't fail to match / close opened braces -> "
                    f"more {char1}{char2}-braces closed than opened"
                )
                return _m.start(), _m.end(), err, _msg, None
        if _count > 0:
            _msg = f"Don't fail to match / close opened braces -> at least one '{char1}' is left open"
            return 0, len(text), err, _msg, None

    results = []
    if any(re.finditer(r"[\(\)]", text)):
        results.append(runner(text, "(", ")"))

    if any(re.finditer(r"[\[\]]", text)):
        results.append(runner(text, "[", "]"))

    if any(re.finditer(r"[\{\}]", text)):
        results.append(runner(text, "{", "}"))

    return results
