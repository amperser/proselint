"""
Hyperbolic punctuation.

---
layout:     post
source:     ???
source_url: ???
title:      hyperbolic punctuation
date:       2014-06-10
categories: writing
---

Hyperbolic punctuation.

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
    "Sally sells seashells and they were too expensive!",
    "Why does Sally sell such expensive seashells?",
]

examples_fail = [
    "So exaggerated!!!",
    "Really??",
    "What is going on?!",
    "What is going on!?",
    "I'm really excited!!",
    "I'm really excited! Really!",
    "Sally sells seashells and they were too expensive!!!!",
    "Sally sells seashells and they were too expensive! They were not!",
    "Why does Sally sell such expensive seashells??",
    "Why does Sally sell such expensive seashells????",
]

check_repeated = CheckSpec(
    Existence(
        [r"[!?]\s*?[!?]{1,}"],
        padding=Pd.disabled,
        unicode=True,
        dotall=True,
    ),
    "punctuation.hyperbole.repeated",
    "'{}' is hyperbolic.",
    ignore_case=False,
)

check_exclamations_ppm = CheckSpec(
    Existence(
        [r"\w!"],
        padding=Pd.disabled,
    ),
    "punctuation.hyperbole.30ppm",
    "More than 30 ppm of exclamations. Keep them under control.",
    flags=CheckFlags(ppm_threshold=30),
)

__register__ = (
    check_repeated,
    check_exclamations_ppm,
)
