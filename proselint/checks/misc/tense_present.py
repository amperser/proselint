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
from proselint.tools import memoize
import re


@memoize
def check(text):
    """Check the text."""
    err = "misc.tense_present"
    msg = r"'{}'."

    illogics = [
        r"up to \d{1,3}% ?[-\u2014\u2013]{0,3} ?(?:or|and) more\W?",
        "between you and I",
        "on accident",
        "somewhat of a",
        "all it's own",
        "reason is because",
        "audible to the ear",
        "in regards to",
        "would of",
        # "and so",
        r"i ?(?:feel|am feeling|am|'m|'m feeling) nauseous",
    ]

    errors = []
    for i in illogics:
        for m in re.finditer(r"\s{}\s".format(i), text, flags=re.U | re.I):
            txt = m.group(0).strip()
            errors.append((
                m.start() + 1,
                m.end(),
                err,
                msg.format(txt),
                None))

    return errors
