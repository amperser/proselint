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

from proselint.checks import CheckSpec, Existence, Pd

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

check_lowercase_periods = CheckSpec(
    Existence([r"\d{1,2} ?[ap]m"]),
    "dates_times.am_pm.lowercase_periods",
    "With lowercase letters, periods are standard.",
    ignore_case=False,
)

check_spacing = CheckSpec(
    Existence(
        [r"\b\d{1,2}[ap]\.?m\.?"],
        padding=Pd.disabled,
    ),
    "dates_times.am_pm.spacing",
    "It's standard to put a space before 'a.m.' or 'p.m.'.",
)

check_midnight_noon = CheckSpec(
    Existence(
        [r"\b12 ?[ap]\.?m\.?"],
        padding=Pd.disabled,
    ),
    "dates_times.am_pm.midnight_noon",
    "12 a.m. and 12 p.m. are wrong and confusing. Use 'midnight' or 'noon'.",
)

check_redundancy = CheckSpec(
    Existence(
        [
            r"\b\d{1,2} ?a\.?m\.? in the morning",
            r"\b\d{1,2} ?p\.?m\.? in the evening",
            r"\b\d{1,2} ?p\.?m\.? at night",
            r"\b\d{1,2} ?p\.?m\.? in the afternoon",
        ],
        padding=Pd.disabled,
    ),
    "dates_times.am_pm.redundancy",
    "'a.m.' is always morning; 'p.m.' is always night.",
)

__register__ = (
    check_lowercase_periods,
    check_spacing,
    check_midnight_noon,
    check_redundancy,
)
