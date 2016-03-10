# -*- coding: utf-8 -*-
"""Actually, this checks for the overuse of actually.

---
layout:     post
source:     unknown
source_url: http://bit.ly/1FANcFh
title:      actually
date:       2014-06-10 12:31:19
categories: writing
---

Actually, this checks for the overuse of actually.

"""
import re

from proselint.tools import memoize


@memoize
def check(text):
    """Check the text."""
    err = "misc.actually"
    msg = u"Actually, you should be careful about overuse of \"actually.\""

    regex = r"[Aa]ctually"

    count = len(re.findall(regex, text))
    num_words = len(text.split(" "))

    ppm = (count*1.0 / num_words) * 1e6

    if ppm > 5040:
        loc = re.search(regex, text).start() + 1
        return [(loc, loc+1, err, msg)]
    else:
        return []
