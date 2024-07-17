"""
Too much yelling.

---
layout:     post
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10
categories: writing
---

Too much yelling.

"""

from __future__ import annotations

from proselint.checks import (
    CheckFlags,
    CheckSpec,
    Existence,
    Pd,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "The QUICK BROWN fox juMPED over the lazy cat.",
    "Sally sells seashells and they were too expensive!",
]

examples_fail = [
    "Sally sells seashells and they were too expensive!!!!",
    "Sally sells seashells and they were too expensive! They were not!",
    "I'm really excited!!",
    "I'm really excited! Really!",
]


# FIXME: this is duplicated by hyperbole.misc
check_repeated_exclamations = CheckSpec(
    Existence([r"[\!]\s*?[\!]{1,}"], padding=Pd.disabled, dotall=True),
    "typography.exclamation.leonard.repeated",
    "Stop yelling. Keep your exclamation points under control.",
    flags=CheckFlags(limit_results=1),
    ignore_case=False,
)

check_exclamations_ppm = CheckSpec(
    Existence(
        [r"\w!"],
        padding=Pd.disabled,
    ),
    "typography.exclamation.leonard.30ppm",
    "More than 30 ppm of exclamations. Keep them under control.",
    flags=CheckFlags(ppm_threshold=30),
)

__register__ = (
    check_repeated_exclamations,
    check_exclamations_ppm,
)
