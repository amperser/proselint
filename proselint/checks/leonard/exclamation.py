# -*- coding: utf-8 -*-
"""EES: Too much yelling.

---
layout:     post
error_code: SCH
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10 12:31:19
categories: writing
---

Too much yelling.

"""
from tools import existence_check, memoize, line_and_column


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
    num_words = text.count(" ")

    ppm = (count*1.0 / num_words) * 1e6

    if ppm > 30:
        (line, column) = line_and_column(text, text.find('!'))
        return [(line, column, err, msg)]
    else:
        return []
