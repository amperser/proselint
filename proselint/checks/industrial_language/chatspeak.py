"""
Chatspeak.

---
layout:     post
source:     ???
source_url: ???
title:      textese
date:       2014-06-10
categories: writing
---

Chatspeak.

"""

from __future__ import annotations

from proselint.checks import CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "BRB getting coffee.",
]

check = CheckSpec(
    Existence([
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
        "rotfl",
        "sum1",
        "SWAK",
        "THNX",
        "THX",
        "TTYL",
        "XOXO",
    ]),
    "industrial_language.chatspeak",
    "'{}' is chatspeak. Write it out.",
)

__register__ = (check,)
