"""
Corporate speak.

---
layout:     post
source:     Travis Bradberry for Inc.com
source_url: http://bit.ly/1IxWnto
title:      corporate speak
date:       2014-06-10
categories: writing
---

Avoid these cases of business jargon.

"""

from __future__ import annotations

from proselint.checks import CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "We will discuss it later.",
]

examples_fail = [
    "We will circle back around to it.",
]

check = CheckSpec(
    Existence([
        "at the end of the day",
        "back to the drawing board",
        "hit the ground running",
        "get the ball rolling",
        "low-hanging fruit",
        "thrown under the bus",
        "think outside the box",
        "let's touch base",
        "get my manager's blessing",
        "it's on my radar",
        "ping me",
        "i don't have the bandwidth",
        "no brainer",
        "par for the course",
        "bang for your buck",
        "synergy",
        "move the goal post",
        "apples to apples",
        "win-win",
        "circle back around",
        "all hands on deck",
        "take this offline",
        "drill-down",
        "elephant in the room",
        "on my plate",
    ]),
    "industrial_language.corporate_speak",
    "Minimize your use of corporate catchphrases like this one.",
)

__register__ = (check,)
