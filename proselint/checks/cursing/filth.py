"""Filthy words.

---
layout:     post
source:     George Carlin
source_url: https://youtu.be/kyBH5oNQOS0
title:      filthy words
date:       2014-06-10 12:31:19
categories: writing
---

Filthy words.

"""
from __future__ import annotations

from proselint.tools import ResultCheck, existence_check, memoize


@memoize
def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "cursing.filth"
    msg = """Nobody ever tells you this as a kid, but you're supposed to avoid
        this word."""

    items = [
        "shit",
        "piss",
        "fuck",
        "cunt",
        "cocksucker",
        "motherfucker",
        "tits",
        "fart",
        "turd",
        "twat",
    ]

    return existence_check(text, items, err, msg)
