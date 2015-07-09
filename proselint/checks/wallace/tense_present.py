# -*- coding: utf-8 -*-
"""Tense present.

---
layout:     post
source:     DFW's Tense Present
source_url: http://bit.ly/1c85lgR
title:      Tense present
date:       2014-06-10 12:31:19
categories: writing
---

Archaism.

"""
from tools import memoize
import re


@memoize
def check(text):
    """Check the text."""
    err = "wallace.tense_present"
    msg = u"'{}'."

    illogics = [
        u"up to \d{1,3}% ?[-\u2014\u2013]{0,3} ?(?:or|and) more\W?",
        "between you and I",
        "on accident",
        "somewhat of a",
        "all it's own",
        "reason is because",
        "audible to the ear",
        "in regards to",
        "would of",
        # "and so",
        "i ?(?:feel|am feeling|am|'m|'m feeling) nauseous",
    ]

    errors = []
    for i in illogics:
        for m in re.finditer(u"\s{}\s".format(i), text, flags=re.U | re.I):
            txt = m.group(0).strip()
            errors.append((m.start() + 1, m.end(), err, msg.format(txt)))

    return errors
