"""Lexical illusions.

---
layout:     post
source:     write-good
source_url: https://github.com/btford/write-good
title:      Lexical illusion present
date:       2014-06-10 12:31:19
categories: writing
---

A lexical illusion is when a word word is unintentionally repeated twice, and
and this happens most often between line breaks.

"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import simple_existence_check


def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "lexical_illusions.misc"
    msg = "There's a lexical illusion here: a word is repeated."
    item = r"\b(?<!\-)(\w+)(\b\s\1)+\b"
    exceptions = [r"^had had$", r"^that that$"]

    return simple_existence_check(
        text,
        item,
        err,
        msg,
        exceptions=exceptions,
    )
