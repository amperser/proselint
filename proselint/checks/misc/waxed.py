"""Waxed lyrical.

---
layout:     post
source:     Fowler's Modern English Usage
source_url: bit.ly/1YBG8QJ
title:      Waxed lyrical
date:       2016-03-10
categories: writing
---

Fowler's says:
Its primary meaning 'grow larger, increase' (as opposed to 'wane') leads
naturally to the sense 'pass into a specified state or mood, begin to use a
specified tone. In this meaning a following modifier must be an adj. not an
adverb ('He waxed enthusiastic [not enthusiastically] about Australia').
"""
from __future__ import annotations

import re

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "Wax me if you can.",
    "He waxed poetic.",
]

examples_fail = [
    "They really could wax poetically.",
]


def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    if not any(re.finditer("\bwax\b", text, re.IGNORECASE)):
        # early exit for a niche and costly check
        return []

    err = "misc.waxed"
    msg = "The modifier following 'waxed' must be an adj.: '{}' is correct"

    waxes = ["wax", "waxes", "waxed", "waxing"]
    modifiers = [
        ("ebullient", "ebulliently"),
        ("ecstatic", "ecstatically"),
        ("eloquent", "eloquently"),
        ("enthusiastic", "enthusiastically"),
        ("euphoric", "euphorically"),
        ("indignant", "indignantly"),
        ("lyrical", "lyrically"),
        ("melancholic", "melancholically"),
        ("metaphorical", "metaphorically"),
        ("nostalgic", "nostalgically"),
        ("patriotic", "patriotically"),
        ("philosophical", "philosophically"),
        ("poetic", "poetically"),
        ("rhapsodic", "rhapsodically"),
        ("romantic", "romantically"),
        ("sentimental", "sentimentally"),
    ]

    # NOTE: python automatically caches this calculation for reruns
    #       check with benchmark_checks.py
    items = {
        f"{word} {pair[1]}": f"{word} {pair[0]}" for pair in modifiers for word in waxes
    }

    return preferred_forms_check_opti(text, items, err, msg)
