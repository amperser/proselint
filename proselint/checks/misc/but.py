"""
Don't start a paragraph with 'But'.

---
layout:
source: Justin Jungé
source_url:
title:
date:       2016-03-10 12:31:19
categories: writing
---

Paragraphs should not start with certain bad words.

"""

import re
from collections.abc import Iterator

from proselint.registry.checks import Check, CheckResult

PATTERN = re.compile(r"(^|^\n|\n\n)But\b")


def _check_but_paragraphs(text: str, check: Check) -> Iterator[CheckResult]:
    return (
        CheckResult(
            start_pos=(
                m.start() + m.group(0).count("\n", 0, 2) + check.offset[0]
            ),
            end_pos=m.end(),
            check_path=check.path,
            message=check.message,
            replacements=None,
        )
        for m in re.finditer(PATTERN, text)
    )


check = Check(
    check_type=_check_but_paragraphs,
    path="misc.but",
    message="No paragraph should start with a 'But'.",
    ignore_case=False,
)

__register__ = (check,)
