"""find repeated beginnings of sections, sentences,

---
layout:     post
source:     TypoNukeTool
source_url: https://github.com/entorb/typonuketool/blob/main/subs.pl#L284C12-L284C65
title:      monotonic writing
date:       2024-01-14
categories: writing
---


"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import simple_existence_check

# TODO: test the checks below


def check_sentence(text: str) -> list[ResultCheck]:
    """can have false positives after abbreviations"""
    err = "misc.monotonic.sentence"
    msg = "It is bad style to open sentences with the same word, here '{}'."

    regex = r"([\.!\?]\s+|^)([A-Z][a-z]*\b)[^\.!\?]+[\.!?]\s+\2\b(\s+[a-z]*)"
    # explanation: matches identical words starting uppercase after either newline or .!?
    # note: can't be padded without mod -> because of \2
    return simple_existence_check(text, regex, err, msg, ignore_case=False)
