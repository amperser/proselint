"""
Incorrect capitalization.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      incorrect captalization
date:       2014-06-10 12:31:19
categories: writing
---

Incorrect capitalization.

"""

from proselint.registry.checks import Check, engine, types

check_terms = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "mother nature": "Mother Nature",
            "Space Age": "space age",
            "stone age": "Stone Age",
            "the American west": "the American West",
        }
    ),
    path="misc.capitalization.terms",
    message="Incorrect capitalization. '{}' is the preferred form.",
    engine=engine.Fast(opts=engine.RegexOptions(case_insensitive=False)),
)

check_seasons = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "Winter": "winter",
            "Summer": "summer",
            # "Fall": "fall",
            # "Spring": "spring",
        }
    ),
    path="misc.capitalization.seasons",
    message="Seasons shouldn't be capitalized. '{}' is the preferred form.",
    engine=engine.Fast(opts=engine.RegexOptions(case_insensitive=False)),
)

check_months = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "january": "January",
            "february": "February",
            "april": "April",
            "june": "June",
            "july": "July",
            "august": "August",
            "september": "September",
            "october": "October",
            "november": "November",
            "december": "December",
            # "march": "March",
            # "may": "May",
        }
    ),
    path="misc.capitalization.months",
    message="Months should be capitalized. '{}' is the preferred form.",
    engine=engine.Fast(opts=engine.RegexOptions(case_insensitive=False)),
)

check_days = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "monday": "Monday",
            "tuesday": "Tuesday",
            "wednesday": "Wednesday",
            "thursday": "Thursday",
            "friday": "Friday",
            "saturday": "Saturday",
            "sunday": "Sunday",
        }
    ),
    path="misc.capitalization.days",
    message=(
        "Days of the week should be capitalized. '{}' is the preferred form."
    ),
    engine=engine.Fast(opts=engine.RegexOptions(case_insensitive=False)),
)

__register__ = (
    check_terms,
    check_seasons,
    check_months,
    check_days,
)
