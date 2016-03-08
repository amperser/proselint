# -*- coding: utf-8 -*-
"""Back-formations.

---
layout:     post
source:     The sense of style
source_url: http://amzn.to/1EOUZ5g
title:      back-formations
date:       2014-06-10 12:31:19
categories: writing
---

Back-formations.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "pinker.latin"
    msg = "Use English. '{}' is the preferred form."

    list = [
        ["other things being equal",          ["ceteris paribus"]],
        ["among other things",                ["inter alia"]],
        ["in and of itself",                  ["simpliciter"]],
        ["having made the necessary changes", ["mutatis mutandis"]],
    ]

    return preferred_forms_check(text, list, err, msg)
