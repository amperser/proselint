"""Weasel words.

---
layout:     post
source:     write-good
source_url: https://github.com/btford/write-good
title:      Weasel words.
date:       2014-06-10
categories: writing
---

Weasel words clearly weaken various aspects of a number of your sentences.

"""
from __future__ import annotations

from typing import TYPE_CHECKING

from proselint.checks import existence_check

if TYPE_CHECKING:
    from proselint.checks import ResultCheck


def check(text: str) -> list[ResultCheck]:
    """
    source: https://en.wikipedia.org/wiki/Weasel_word
    """
    error_code = "weasel_words.misc"
    msg = "Weasel words aka. anonymous authority present ({})."

    items = [
        # vague
        "evidence suggests",
        "in most respects",
        "some people",
        "somewhat",
        # false authority
        "it has been decided",
        "it is said",
        "it is thought",
        "mistakes were made",
        "researchers believe",
        "some people say",
    ]

    return existence_check(text, items, error_code, msg)
