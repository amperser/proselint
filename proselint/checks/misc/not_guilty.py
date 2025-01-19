"""
Not guilty beyond a reasonable doubt.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Not guilty beyond a reasonable doubt.
date:       2016-03-09
categories: writing
---

This phrasing is ambiguous. The standard by which a jury decides criminal
charges is this: a defendant is guilty only if the evidence shows, beyond a
reasonable doubt, that he or she committed the crime. Otherwise, the defendant
is not guilty. Thus, we say that a defendant was not found "guilty beyond a
reasonable doubt."

If somebody is found not guilty, say "not guilty." Omit the standard
("beyond a reasonable doubt") to prevent a miscue.

Not guilty beyond a reasonable doubt
"""

from __future__ import annotations

from proselint.checks import CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "She is not guilty beyond a reasonable doubt.",
]

check = CheckSpec(
    Existence([r"not guilty beyond (a |any )?reasonable doubt"]),
    "misc.not_guilty",
    "'not guilty beyond a reasonable doubt' is an ambiguous phrasing.",
)

__register__ = (check,)
