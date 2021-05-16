# -*- coding: utf-8 -*-
"""Commercialese.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      commercialese
date:       2014-06-10 12:31:19
categories: writing
---

Commercialese.

"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
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
        r"inst\.",
        "in the amount of",
        "of even date",
        "pending receipt of",
        "please be advised that",
        "please return same",
        "pleasure of a reply",
        r"prox\.",
        "pursuant to your request",
        "regarding the matter",
        "regret to inform",
        "thanking you in advance",
        "the undersigned",
        "this acknowledges your letter",
        r"ult\."
        "we are pleased to note",
        "with regard to",
        "your favor has come to hand",
        "yours of even date"
    ]

    return existence_check(text, commercialese, err, msg, join=True)
