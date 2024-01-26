"""Incorrect capitalization.

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

from proselint.checks import Pd
from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check_opti
from proselint.checks import simple_existence_check

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


def check_terms(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.capitalization.terms"
    msg = "Incorrect capitalization. '{}' is the preferred form."

    items: dict[str, str] = {
        "stone age": "Stone Age",
        "Space Age": "space age",
        "the American west": "the American West",
        "mother nature": "Mother Nature",
    }

    return preferred_forms_check_opti(text, items, err, msg, ignore_case=False)


def check_seasons(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.capitalization.seasons"
    msg = "Seasons shouldn't be capitalized. '{}' is the preferred form."
    items: dict[str, str] = {
        "Winter": "winter",
        "Fall": "fall",
        "Summer": "summer",
        "Spring": "spring",
    }
    return preferred_forms_check_opti(text, items, err, msg, ignore_case=False)


def check_months(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.capitalization.months"
    msg = "Months should be capitalized. '{}' is the preferred form."

    items: dict[str, str] = {
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
    }
    # too many false positives: may, march
    # TODO: deal better with collisions / false positives
    #       i.e. "(you|he|...) may proceed" follows a pattern
    return preferred_forms_check_opti(text, items, err, msg, ignore_case=False)


def check_days(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.capitalization.days"
    msg = "Days of the week should be capitalized. '{}' is the preferred form."

    items: dict[str, str] = {
        "monday": "Monday",
        "tuesday": "Tuesday",
        "wednesday": "Wednesday",
        "thursday": "Thursday",
        "friday": "Friday",
        "saturday": "Saturday",
        "sunday": "Sunday",
    }

    return preferred_forms_check_opti(text, items, err, msg, ignore_case=False)


def check_roman_war(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "misc.capitalization.roman_num.ww"
    msg = "Don't fail to capitalize roman numeral abbreviation in '{}'."

    regex = "World War (I(i*)|i*)"
    return simple_existence_check(text, regex, err, msg, ignore_case=False)


def check_roman_numerals(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "misc.capitalization.roman_num"
    msg = "Don't fail to capitalize roman numeral abbreviation '{}'."

    numerals_regex = Pd.words_in_txt.value.format(
        r"M{0,3}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})"
    )
    results_all = simple_existence_check(
        text, numerals_regex, err, msg, ignore_case=True
    )
    results_valid = []
    for _start, _end, _err, _msg, _ in results_all:
        # is it possible to bring that into the regex or check?
        _item: str = text[_start:_end].strip()
        if len(_item) < 2 or _item.isupper():  # TODO: could be < 1
            continue
        if any(_letter in _item for _letter in "mdclxvi"):
            results_valid.append((_start, _end, _err, _msg, _))
    return results_valid
