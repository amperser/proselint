"""Incorrect capitalization.

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
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check


def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.capitalization"
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
    err = "MAU102"
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
    err = "MAU102"
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
    ]
    # TODO: deal better with collisions / false positives
    #       i.e. "(you|he|...) may proceed" follows a pattern

    return preferred_forms_check(text, items, err, msg, ignore_case=False)


def check_days(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "MAU102"
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
