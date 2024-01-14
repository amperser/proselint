"""find repeated beginnings of sections, sentences,

---
layout:     post
source:     TypoNukeTool
source_url: https://github.com/entorb/typonuketool/blob/main/subs.pl#L284C12-L284C65
title:      monotonic writing
date:       2013-01-14
categories: writing
---


"""
from __future__ import annotations

from proselint.checks import ResultCheck, simple_existence_check
from proselint.checks import existence_check

# TODO: test the checks below

def check_sentence(text: str) -> list[ResultCheck]:
    """can have false positives after abbreviations"""
    err = "misc.monotonic.sentence"
    msg = "It is bad style to open sentences with the same word, here '{}'."

    regex = r"(([\.!?]\s+|^)([A-Z][a-z]*\b)[^\.!?]+[\.!?]\s+\3\b(\s+[a-z]*))"
    # explanation: matches identical words starting uppercase after either newline or .!?
    return simple_existence_check(text, regex, err, msg, ignore_case=False)

