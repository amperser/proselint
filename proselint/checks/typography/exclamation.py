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
import re

from proselint.tools import existence_check, memoize


@memoize
def check_repeated_exclamations(text):
    """Check the text."""
    err = "leonard.exclamation.multiple"
    msg = u"Stop yelling. Keep your exclamation points under control."

    regex = r"[\!]\s*?[\!]{1,}"

    return existence_check(
        text, [regex], err, msg, require_padding=False, ignore_case=False,
        max_errors=1, dotall=True)


@memoize
def check_exclamations_ppm(text):
    """Make sure that the exclamation ppm is under 30."""
    err = "leonard.exclamation.30ppm"
    msg = u"More than 30 ppm of exclamations. Keep them under control."

    regex = r"\w!"

    count = len(re.findall(regex, text))
    num_words = len(text.split(" "))

    ppm = (count*1.0 / num_words) * 1e6

    if ppm > 30 and count > 1:
        loc = re.search(regex, text).start() + 1
        return [(loc, loc+1, err, msg, ".")]
    else:
        return []
