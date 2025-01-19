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

from proselint.checks import CheckResult, CheckSpec

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "Let me (I mean you) help her.",
    "Counting is easy (for me).",
    """Is everything fine (I mean
in a general way)?""",
    "a) heading",
]

examples_fail = [
    "Counting (to two) is hard (for me.",
    "there might be an error).",
]

BRACES = (
    (r"[()]", ("(", ")")),
    (r"[{}]", ("{", "}")),
    (r"[\[\]]", ("[", "]")),
)


def trace_braces(
    text: str, rex: str, chars: tuple[str, str], spec: CheckSpec
) -> Optional[CheckResult]:
    """Check that braces match."""
    # TODO: same check for quotes?
    _count = 0
    for _m in re.finditer(rex, text):
        _count += (-1) ** chars.index(_m.group(0))
        if _count < 0:
            # TODO: this could trigger false positives for lists like 1), 2), a)
            _msg = f"{spec.msg} more '{chars[1]}' were closed than opened."
            return CheckResult(
                start_pos=_m.start(),
                end_pos=_m.end(),
                check=spec.path,
                message=_msg,
                replacements=None,
            )
    if _count > 0:
        # TODO: add a correct span for this case
        return CheckResult(
            start_pos=0,
            end_pos=len(text),
            check=spec.path,
            message=f"{spec.msg} at least one '{chars[0]}' is left open.",
            replacements=None,
        )
    return None


def _check_unmatched(text: str, spec: CheckSpec) -> list[CheckResult]:
    """Check the text."""
    results: list[Optional[CheckResult]] = [
        trace_braces(text, regex, chars, spec)
        for regex, chars in BRACES
        if re.search(regex, text)
    ]

    return [result for result in results if result]


check_unmatched = CheckSpec(
    _check_unmatched,
    "misc.braces.unmatched",
    "Match braces:",
)

__register__ = (check_unmatched,)
