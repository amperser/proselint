"""a.m. / p.m.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      a.m. & p.m.
date:       2014-06-10 12:31:19
categories: writing
---

"""
from __future__ import annotations

from proselint.checks import Pd
from proselint.checks import ResultCheck
from proselint.checks import existence_check


def check_lowercase_periods(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "dates_times.am_pm.lowercase_periods"
    msg = "With lowercase letters, the periods are standard."

    return existence_check(
        text, [r"\d{1,2} ?[ap]m"], err, msg, ignore_case=False
    )


def check_spacing(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "dates_times.am_pm.spacing"
    msg = "It's standard to put a space before 'a.m.' or 'p.m.'."

    return existence_check(text, [r"\d{1,2}[ap]\.?m\.?"], err, msg)


def check_midnight_noon(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "dates_times.am_pm.midnight_noon"

    msg = (
        "12 a.m. and 12 p.m. are wrong and confusing. Use 'midnight' or 'noon'."
    )

    return existence_check(text, [r"12 ?[ap]\.?m\.?"], err, msg)


def check_redundancy(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "dates_times.am_pm.midnight_noon"
    msg = "'a.m.' is always morning; 'p.m.' is always night."

    items = [
        r"\d{1,2} ?a\.?m\.? in the morning",
        r"\d{1,2} ?p\.?m\.? in the evening",
        r"\d{1,2} ?p\.?m\.? at night",
        r"\d{1,2} ?p\.?m\.? in the afternoon",
    ]

    return existence_check(text, items, err, msg, padding=Pd.disabled)
