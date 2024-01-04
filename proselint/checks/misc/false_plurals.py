"""False plurals.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      False plurals.
date:       2014-06-10 12:31:19
categories: writing
---

Using the incorrect form of the plural.

"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import existence_check
from proselint.checks import preferred_forms_check


def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.false_plurals.examples"
    msg = "The plural is {}"

    preferences = [
        ["talismans", ["talismen"]],
        ["phenomena", ["phenomenons"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)


def check_kudos(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "misc.false_plurals.kudos"
    msg = "Kudos is singular."

    return existence_check(text, ["many kudos"], err, msg)
