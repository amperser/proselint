"""
Finds unmatched braces.

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
from typing import Optional

from proselint.checks import CheckResult

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "Let me (I mean you) help her.",
    "Counting is easy (for me).",
    """Is everything fine (I mean
in a general way)?""",
    "a) heading",
]

examples_fail = [
    "This is the famous first line.",
    "Counting (to two) is hard (for me.",
    "there might be an error).",
]


def trace_braces(
    text: str, rex: str, char1: str, char2: str, err: str
) -> Optional[CheckResult]:
    """Check that braces match."""
    # TODO: same check for quotes?
    _count = 0
    for _m in re.finditer(rex, text):
        if _m.group(0) == char1:
            _count += 1
        elif _m.group(0) == char2:
            _count -= 1
        if _count < 0:
            # TODO: this could trigger false positives for lists like 1), 2), a)
            _msg = (
                "Don't fail to match / close opened braces -> "
                f"more {char1}{char2}-braces closed than opened"
            )
            return CheckResult(
                start_pos=_m.start(),
                end_pos=_m.end(),
                check=err,
                message=_msg,
                replacements=None,
            )
    if _count > 0:
        _msg = (
            "Don't fail to match / close opened braces -> "
            f"at least one '{char1}' is left open"
        )
        return CheckResult(
            start_pos=0,
            end_pos=len(text),
            check=err,
            message=_msg,
            replacements=None,
        )
    return None


def check_unmatched(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "misc.braces.unmatched"
    # msg = "Don't fail to match / close opened braces '{}'."

    results: list[CheckResult] = []
    if any(re.finditer(r"[()]", text)):
        _res = trace_braces(text, r"[()]", "(", ")", err)
        if _res:
            results.append(_res)

    if any(re.finditer(r"[\[\]]", text)):
        _res = trace_braces(text, r"[\[\]]", "[", "]", err)
        if _res:
            results.append(_res)

    if any(re.finditer(r"[{}]", text)):
        _res = trace_braces(text, r"[{}]", "{", "}", err)
        if _res:
            results.append(_res)

    return results
