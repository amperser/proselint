"""
Psychological and psychiatric terms to avoid.

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

from proselint.registry.checks import Check, types

check_lie_detector_test = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "lie detector test": "polygraph test",
            "lie detector machine": "polygraph machine",
        }
    ),
    path="psychology.lie_detector",
    message="Polygraph machines measure arousal, not lying per se. Try '{}'.",
)

check_p_equals_zero = Check(
    check_type=types.ExistenceSimple(pattern=r"p = 0.0{2,4}"),
    path="psychology.p_equals_zero",
    message="Unless p really equals zero, you should use more decimal places.",
)

check_mental_telepathy = Check(
    check_type=types.ExistenceSimple(pattern="mental telepathy"),
    path="psychology.mental_telepathy",
    message="This is redundant because all purported telepathy is mental.",
)

__register__ = (
    check_lie_detector_test,
    check_p_equals_zero,
    check_mental_telepathy,
)
