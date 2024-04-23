"""Psychological and psychiatric terms to avoid.

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

from proselint.checks import CheckResult
from proselint.checks import existence_check
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The defendant took a lie detector test.",
    "The effect was highly signficant at p = 0.00.",
    "I've been practicing mental telepathy.",
]


def check_lie_detector_test(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "psychology.lie_detector"
    msg = "Polygraph machines measure arousal, not lying per se. Try {}."

    items: dict[str, str] = {
        "lie detector test": "polygraph test",
        "lie detector machine": "polygraph machine",
    }

    return preferred_forms_check_opti(text, items, err, msg)


def check_p_equals_zero(text: str) -> list[CheckResult]:
    """Check for p = 0.000."""
    err = "psychology.p_equals_zero"
    msg = "Unless p really equals zero, you should use more decimal places."

    items = [
        "p = 0.00",
        "p = 0.000",
        "p = 0.0000",
    ]

    return existence_check(text, items, err, msg)


def check_mental_telepathy(text: str) -> list[CheckResult]:
    """Check for 'mental telepathy'."""
    err = "psychology.mental_telepathy"
    msg = "This is redundant because all purported telepathy is mental."

    return existence_check(text, ["mental telepathy"], err, msg)
