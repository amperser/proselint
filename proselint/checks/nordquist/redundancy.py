# -*- coding: utf-8 -*-
"""MAU103: Redundancy.

---
layout:     post
error_code: MAU103
source:     Richard Nordquist
source_url: http://amzn.to/15wF76r
title:      abbetor
date:       2014-06-10 12:31:19
categories: writing
---

Points out use redundant phrases.

"""
from tools import memoize, preferred_forms_check


@memoize
def check(blob):
    """Suggest the preferred forms."""
    err = "nordquist.redundancy"
    msg = "Redundancy. Use '{}' instead of '{}'."

    redundancies = [
        ["essential",          ["absolutely essential"]],
        ["necessary",          ["absolutely necessary"]],
        ["a.m.",               ["a.m. in the morning"]],
        ["p.m.",               ["p.m. at night"]],
    ]
    return preferred_forms_check(blob, redundancies, err, msg)
