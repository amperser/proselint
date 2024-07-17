"""
Commercialese.

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

from proselint.checks import (
    CheckSpec,
    Existence,
    Pd,
    PreferredForms,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "We regret to inform you of this.",
    "the C.i.F. is free.",
]

check = CheckSpec(
    Existence([
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
    ]),
    "misc.commercialese",
    "'{}' is commercialese.",
)

# src = "https://www.ourcivilisation.com/smartboard/shop/gowerse/abc/cmmrcls.htm"
check_abbrev = CheckSpec(
    PreferredForms(
        {
            r"inst\.": "this month",
            r"prox\.": "next month",
            r"ult\.": "last month",
            r"c\.i\.f\.": "cost, insurance, freight",
            r"f\.o\.b\.": "Free On Board",
        },
        padding=Pd.sep_in_txt,
    ),
    "misc.commercialese.abbreviations",
    "'{}' is commercialese. Depending on audience switch to {}.",
)


__register__ = (
    check,
    check_abbrev,
)
