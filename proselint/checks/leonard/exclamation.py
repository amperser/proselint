# -*- coding: utf-8 -*-
"""Too much yelling.

---
layout:     post
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10 12:31:19
categories: writing
---

Too much yelling.

"""
from tools import existence_check, memoize


@memoize
def check_repeated_exclamations(text):
    """Check the text."""
    err = "leonard.exclamation.multiple"
    msg = u"Stop yelling. Keep your exclamation points under control."

    regex = r"[^A-Z]\b((\s[A-Z]+){3,})"

    return existence_check(
        text, [regex], err, msg, require_padding=False, ignore_case=False,
        max_errors=1, dotall=True)


@memoize
def check_exclamations_ppm(text):
    """Make sure that the exclamatiion ppm is under 30."""
    err = "leonard.exclamation.30ppm"
    msg = u"More than 30 ppm of exclamations. Keep them under control."

    count = text.count("!")
    num_words = len(text.split(" "))

    ppm = (count*1.0 / num_words) * 1e6

    if ppm > 30:
        loc = text.find('!')
        return [(loc, loc+1, err, msg)]
    else:
        return []
