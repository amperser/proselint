"""
a.m. / p.m.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      a.m. & p.m.
date:       2014-06-10
categories: writing
---

"""
from __future__ import annotations

from proselint.checks import CheckResult, Pd, existence_check, registry

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "It happened at 7 a.m.",
    "On Wed, Sep 21, 2016 at 11:42 AM -0400, X wrote:",
    "It happened at 7 a.m.",
    "It happened at noon.",
    "It happened at 7 a.m.",
]

examples_fail = [
    "It happened at 7 am.",
    "It happened at 7a.m.",
    "It happened at 12 a.m.",
    "It happened at 12 p.m.",
    "It happened at 7a.m. in the morning.",
]


def check_lowercase_periods(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "dates_times.am_pm.lowercase_periods"
    msg = "With lowercase letters, the periods are standard."

    return existence_check(
        text, [r"\d{1,2} ?[ap]m"], err, msg, ignore_case=False
    )


def check_spacing(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "dates_times.am_pm.spacing"
    msg = "It's standard to put a space before 'a.m.' or 'p.m.'."

    return existence_check(
        text, [r"\b\d{1,2}[ap]\.?m\.?"], err, msg, padding=Pd.disabled
    )


def check_midnight_noon(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "dates_times.am_pm.midnight_noon"

    msg = (
        "12 a.m. and 12 p.m. are wrong and confusing. Use 'midnight' or 'noon'."
    )

    return existence_check(
        text, [r"\b12 ?[ap]\.?m\.?"], err, msg, padding=Pd.disabled
    )


def check_redundancy(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "dates_times.am_pm.redundancy"
    msg = "'a.m.' is always morning; 'p.m.' is always night."

    items = [
        r"\b\d{1,2} ?a\.?m\.? in the morning",
        r"\b\d{1,2} ?p\.?m\.? in the evening",
        r"\b\d{1,2} ?p\.?m\.? at night",
        r"\b\d{1,2} ?p\.?m\.? in the afternoon",
    ]

    return existence_check(text, items, err, msg, padding=Pd.disabled)


registry.register_many({
    "dates_times.am_pm.lowercase_periods": check_lowercase_periods,
    "dates_times.am_pm.spacing": check_spacing,
    "dates_times.am_pm.midnight_noon": check_midnight_noon,
    "dates_times.am_pm.redundancy": check_redundancy,
})
