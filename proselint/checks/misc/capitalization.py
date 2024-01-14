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
from proselint.checks import existence_check
from proselint.checks import preferred_forms_check
from proselint.checks import simple_existence_check


def check_terms(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.capitalization.terms"
    msg = "Incorrect capitalization. '{}' is the preferred form."

    items = [
        ["Stone Age", ["stone age"]],
        ["space age", ["Space Age"]],
        ["the American West", ["the American west"]],
        ["Mother Nature", ["mother nature"]],
    ]

    return preferred_forms_check(text, items, err, msg, ignore_case=False)


def check_seasons(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.capitalization.seasons"
    msg = "Seasons shouldn't be capitalized. '{}' is the preferred form."
    items = [
        ["winter", ["Winter"]],
        # ["fall",          ["Fall"]],
        ["summer", ["Summer"]],
        ["spring", ["Spring"]],
    ]

    return preferred_forms_check(text, items, err, msg, ignore_case=False)


def check_months(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.capitalization.months"
    msg = "Months should be capitalized. '{}' is the preferred form."

    items = [
        ["January", ["january"]],
        ["February", ["february"]],
        # ["March",           ["march"]],
        ["April", ["april"]],
        # ["May",             ["may"]],
        ["June", ["june"]],
        ["July", ["july"]],
        ["August", ["august"]],
        ["September", ["september"]],
        ["October", ["october"]],
        ["November", ["november"]],
        ["December", ["december"]],
    ]  # TODO: deal better with collisions / false positives

    return preferred_forms_check(text, items, err, msg, ignore_case=False)


def check_days(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.capitalization.days"
    msg = "Days of the week should be capitalized. '{}' is the preferred form."

    items = [
        ["Monday", ["monday"]],
        ["Tuesday", ["tuesday"]],
        ["Wednesday", ["wednesday"]],
        ["Thursday", ["thursday"]],
        ["Friday", ["friday"]],
        ["Saturday", ["saturday"]],
        ["Sunday", ["sunday"]],
    ]

    return preferred_forms_check(text, items, err, msg, ignore_case=False)


# TODO: test the checks below


def check_roman_war(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "misc.capitalization.roman_num.ww"
    msg = "Don't fail to capitalize roman numeral abbreviation in '{}'."

    numerals_regex = " (I(i*)|i*)"

    items = [
        f"World War{numerals_regex}",
    ]

    return existence_check(text, items, err, msg, ignore_case=False)


def check_roman_numerals(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "misc.capitalization.roman_num"
    msg = "Don't fail to capitalize roman numeral abbreviation '{}'."

    numerals_regex = Pd.sep_in_txt.value.format(
        r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})"
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
        if any(_letter in _item for _letter in "MDCLXVI"):
            results_valid.append((_start, _end, _err, _msg, _))
    return results_valid
