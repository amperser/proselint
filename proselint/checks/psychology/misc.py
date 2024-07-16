"""
Psychological and psychiatric terms to avoid.

---
layout:     post
source:     Scott O. Lilienfeld, et al.
source_url: http://dx.doi.org/10.3389/fpsyg.2015.01100
title:      psychological and psychiatric terms to avoid
date:       2014-06-10
categories: writing
---

Psychological and psychiatric terms to avoid.

"""

from __future__ import annotations

from proselint.checks import (
    CheckRegistry,
    CheckSpec,
    Existence,
    PreferredFormsSimple,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The defendant took a lie detector test.",
    "The effect was highly signficant at p = 0.00.",
    "I've been practicing mental telepathy.",
]

check_lie_detector_test = CheckSpec(
    PreferredFormsSimple({
        "lie detector test": "polygraph test",
        "lie detector machine": "polygraph machine",
    }),
    "psychology.lie_detector",
    "Polygraph machines measure arousal, not lying per se. Try {}.",
)

check_p_equals_zero = CheckSpec(
    Existence([
        "p = 0.00",
        "p = 0.000",
        "p = 0.0000",
    ]),
    "psychology.p_equals_zero",
    "Unless p really equals zero, you should use more decimal places.",
)

check_mental_telepathy = CheckSpec(
    Existence(["mental telepathy"]),
    "psychology.mental_telepathy",
    "This is redundant because all purported telepathy is mental.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    registry.register_many((
        check_lie_detector_test,
        check_p_equals_zero,
        check_mental_telepathy,
    ))
