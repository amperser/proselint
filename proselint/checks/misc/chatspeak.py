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

from proselint.checks import CheckRegistry, CheckSpec, Existence

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
        "roftl",
        "sum1",
        "SWAK",
        "THNX",
        "THX",
        "TTYL",
        "XOXO",
    ]),
    "misc.chatspeak",
    "'{}' is chatspeak. Write it out.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
