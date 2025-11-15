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

from collections.abc import Iterator

from proselint.registry.checks import Check, CheckResult, engine

PATTERN = r"(^|^\n|\n\n)But\b"


def _check_but_paragraphs(text: str, check: Check) -> Iterator[CheckResult]:
    return (
        CheckResult(
            span=(
                m.start() + m.group(0).count("\n", 0, 2) + check.offset[0],
                m.end() + check.offset[1],
            ),
            check_path=check.path,
            message=check.message,
            replacements=None,
        )
        for m in check.engine.finditer(PATTERN, text)
    )


check = Check(
    check_type=_check_but_paragraphs,
    path="misc.but",
    message="No paragraph should start with a 'But'.",
    engine=engine.Fast(opts=engine.RegexOptions(case_insensitive=False)),
)

__register__ = (check,)
