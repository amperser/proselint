"""False plurals.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      False plurals.
date:       2014-06-10
categories: writing
---

Using the incorrect form of the plural.

"""
from __future__ import annotations

from proselint.checks import CheckResult
from proselint.checks import existence_check
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "There were several phenomenons.",
    "I give you many kudos.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "misc.plurals.misc"
    msg = "The plural is {} and not {}"

    items: dict[str, str] = {
        "talismen": "talismans",
        "phenomenons": "phenomena",
    }

    return preferred_forms_check_opti(text, items, err, msg)


def check_kudos(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "misc.plurals.kudos"
    msg = "Kudos is singular."

    return existence_check(text, ["many kudos"], err, msg)
