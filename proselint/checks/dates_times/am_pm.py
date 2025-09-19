"""
a.m. / p.m.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      a.m. & p.m.
date:       2014-06-10 12:31:19
categories: writing
---

"""

from proselint.registry.checks import Check, engine, types

check_lowercase_periods = Check(
    check_type=types.ExistenceSimple(pattern=r"\d{1,2} ?[ap]m"),
    path="dates_times.am_pm.lowercase_periods",
    message="It's standard to use periods for lowercase 'a.m.' or 'p.m.'.",
    engine=engine.Fast(opts=engine.RegexOptions(case_insensitive=False)),
)

check_spacing = Check(
    check_type=types.ExistenceSimple(pattern=r"\d{1,2}[ap]\.?m\.?"),
    path="dates_times.am_pm.spacing",
    message="It's standard to put a space before 'a.m.' or 'p.m.'.",
)

check_midnight_noon = Check(
    check_type=types.ExistenceSimple(pattern=r"12 ?[ap]\.?m\.?"),
    path="dates_times.am_pm.midnight_noon",
    message="'12 a.m.' and '12 p.m.' are ambiguous. Use 'midnight' or 'noon'.",
)

check_redundancy = Check(
    check_type=types.Existence(
        items=(
            r"\d{1,2} ?a\.?m\.? in the morning",
            r"\d{1,2} ?p\.?m\.? in the evening",
            r"\d{1,2} ?p\.?m\.? at night",
            r"\d{1,2} ?p\.?m\.? in the afternoon",
        )
    ),
    path="dates_times.am_pm.midnight_noon",
    message="'a.m.' is always morning; 'p.m.' is always night.",
)

__register__ = (
    check_lowercase_periods,
    check_spacing,
    check_midnight_noon,
    check_redundancy,
)
