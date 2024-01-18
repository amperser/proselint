"""Commercialese.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      commercialese
date:       2014-06-10
categories: writing
---

Commercialese.

"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import existence_check
from proselint.checks import preferred_forms_check


examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "We regret to inform you of this.",
    "the C.i.F. is free.",
]

def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "misc.commercialese"
    msg = "'{}' is commercialese."

    commercialese = [
        "acknowledging yours of",
        "beg to advise",
        "enclosed herewith",
        "enclosed please find",
        "further to yours of",
        "further to your letter",
        "in regard to",
        "in the amount of",
        "of even date",
        "pending receipt of",
        "please be advised that",
        "please return same",
        "pleasure of a reply",
        "pursuant to your request",
        "regarding the matter",
        "regret to inform",
        "thanking you in advance",
        "the undersigned",
        "this acknowledges your letter",
        "we are pleased to note",
        "with regard to",
        "your favor has come to hand",
        "yours of even date",
    ]

    return existence_check(text, commercialese, err, msg)


def check_apprev(text: str) -> list[ResultCheck]:
    """
    source: https://www.ourcivilisation.com/smartboard/shop/gowerse/abc/cmmrcls.htm
    """
    err = "misc.commercialese.abbreviations"
    msg = "'{}' is commercialese. Depending on audience switch to {}"

    items = [
        ["this month", [r"inst\."]],
        ["next month", [r"prox\."]],
        ["last month", [r"ult\."]],
        ["cost, insurance, freight", [r"c\.i\.f\."]],
        ["Free On Board", [r"f\.o\.b\."]],
    ]

    return preferred_forms_check(text, items, err, msg)
