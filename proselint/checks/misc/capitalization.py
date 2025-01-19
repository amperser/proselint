"""
Incorrect capitalization.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      incorrect captalization
date:       2014-06-10
categories: writing
---

Incorrect capitalization.

"""

from __future__ import annotations

from proselint.checks import (
    CheckResult,
    CheckSpec,
    ExistenceSimple,
    Pd,
    PreferredFormsSimple,
    existence_check_simple,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "Smoke Stone Age with nothing flagged.",
    "Smoke winter with nothing flagged",
    "world war II",
    "XVII",
]

examples_fail = [
    "It goes back to the stone age.",
    "A nice day during Winter.",
    "A nice day in Spring.",
    "A nice day in june.",
    "It happened on friday.",
    "World War ii",
    "World War i",
    "world War Ii",  # not covered by war-check
    "MCVi",
    "CLx",
    "mCv",
]


check_terms = CheckSpec(
    PreferredFormsSimple({
        "stone age": "Stone Age",
        "Space Age": "space age",
        "the American west": "the American West",
        "mother nature": "Mother Nature",
    }),
    "misc.capitalization.terms",
    "Incorrect capitalization. '{}' is the preferred form.",
    ignore_case=False,
)

check_seasons = CheckSpec(
    PreferredFormsSimple({
        "Winter": "winter",
        "Fall": "fall",
        "Summer": "summer",
        "Spring": "spring",
    }),
    "misc.capitalization.seasons",
    "Seasons shouldn't be capitalized. '{}' is the preferred form.",
    ignore_case=False,
)

check_months = CheckSpec(
    # too many false positives: may, march
    # TODO: deal better with collisions / false positives
    #       i.e. "(you|he|...) may proceed" follows a pattern
    PreferredFormsSimple({
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
    }),
    "misc.capitalization.months",
    "Months should be capitalized. '{}' is the preferred form.",
    ignore_case=False,
)

check_days = CheckSpec(
    PreferredFormsSimple({
        "monday": "Monday",
        "tuesday": "Tuesday",
        "wednesday": "Wednesday",
        "thursday": "Thursday",
        "friday": "Friday",
        "saturday": "Saturday",
        "sunday": "Sunday",
    }),
    "misc.capitalization.days",
    "Days of the week should be capitalized. '{}' is the preferred form.",
    ignore_case=False,
)

check_roman_war = CheckSpec(
    ExistenceSimple("World War (I(i*)|i*)"),
    "misc.capitalization.roman_num.ww",
    "Capitalize the roman numeral abbreviation in '{}'.",
    ignore_case=False,
)


def _check_roman_numerals(text: str, spec: CheckSpec) -> list[CheckResult]:
    """Check the text."""
    numerals_regex = Pd.words_in_txt.format(
        r"M{0,3}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})"
    )
    results_all = existence_check_simple(
        text, numerals_regex, spec.path, spec.msg, ignore_case=True
    )
    results_valid: list[CheckResult] = []
    for _res in results_all:
        # is it possible to bring that into the regex or check?
        _item: str = text[_res.start_pos : _res.end_pos].strip()
        if len(_item) < 2 or _item.isupper():  # TODO: could be < 1
            continue
        if any(_letter in _item for _letter in "mdclxvi"):
            results_valid.append(_res)
    return results_valid


check_roman_numerals = CheckSpec(
    _check_roman_numerals,
    "misc.capitalization.roman_num",
    "Capitalize the roman numeral abbreviation '{}'.",
)

__register__ = (
    check_terms,
    check_seasons,
    check_months,
    check_days,
    check_roman_war,
    check_roman_numerals,
)
