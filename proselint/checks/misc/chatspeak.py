"""Chatspeak.

---
layout:     post
source:     ???
source_url: ???
title:      textese
date:       2014-06-10 12:31:19
categories: writing
---

Chatspeak.

"""
from __future__ import annotations

from proselint.tools import ResultCheck, existence_check, memoize


@memoize
def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "misc.chatspeak"
    msg = "'{}' is chatspeak. Write it out."

    words = [
        "2day",
        "4U",
        "AFAIK",
        "AFK",
        "AFK",
        "ASAP",
        "B4",
        "brb",
        "btw",
        "cya",
        "GR8",
        "lol",
        "LOL",
        "LUV",
        "OMG",
        "rofl",
        "roftl",
        "sum1",
        "SWAK",
        "THNX",
        "THX",
        "TTYL",
        "XOXO",
    ]

    return existence_check(text, words, err, msg)
