# -*- coding: utf-8 -*-
"""Corporate speak.

---
layout:     post
source:     Travis Bradberry for Inc.com
source_url: http://bit.ly/1IxWnto
title:      corporate speak
date:       2014-06-10 12:31:19
categories: writing
---

Avoid these cases of business jargon.

"""
from tools import existence_check, memoize


@memoize
def check_repeated_exclamations(text):
    """Check the text."""
    err = "inc.corporate_speak"
    msg = u"Minimize your use of corporate catchphrases like this one."

    list = [
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
    ]

    return existence_check(text, list, err, msg, ignore_case=True)
