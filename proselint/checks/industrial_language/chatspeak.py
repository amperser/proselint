"""
Chatspeak.

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

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.Existence(
        items=(
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
        )
    ),
    path="industrial_language.chatspeak",
    message="'{}' is chatspeak. Write it out.",
)

__register__ = (check,)
