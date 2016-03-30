# -*- coding: utf-8 -*-
"""Psychological and psychiatric terms to avoid.

---
layout:     post
source:     Scott O. Lilienfeld, et al.
source_url: http://dx.doi.org/10.3389/fpsyg.2015.01100
title:      psychological and psychiatric terms to avoid
date:       2014-06-10 12:31:19
categories: writing
---

Psychological and psychiatric terms to avoid.

"""
from proselint.tools import preferred_forms_check, existence_check, memoize


@memoize
def check_lie_detector_test(text):
    """Suggest the preferred forms."""
    err = "psychology.lie_detector"
    msg = "Polygraph machines measure arousal, not lying per se. Try {}."

    list = [
        ["polygraph test",      ["lie detector test"]],
        ["polygraph machine",   ["lie detector machine"]],
    ]

    return preferred_forms_check(text, list, err, msg)


@memoize
def check_p_equals_zero(text):
    """Check for p = 0.000."""
    err = "psychology.p_equals_zero"
    msg = "Unless p really equals zero, you should use more decimal places."

    list = [
        "p = 0.00",
        "p = 0.000",
        "p = 0.0000",
    ]

    return existence_check(text, list, err, msg, join=True)


@memoize
def check_mental_telepathy(text):
    """Check for 'mental telepathy'."""
    err = "psychology.mental_telepathy"
    msg = "This is redundant because all purported telepathy is mental."

    return existence_check(text, ["mental telepathy"], err, msg)
