"""Don't start a paragraph with 'But'.

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
from __future__ import annotations

from proselint.checks import ResultCheck, existence_check


def check(text: str) -> list[ResultCheck]:
    """Do not start a paragraph with a 'But'."""
    err = "misc.but"
    msg = "No paragraph should start with a 'But'."
    regex = r"(^|([\n\r]+))(\s*)But"

    return existence_check(text, [regex], err, msg, ignore_case=False)
