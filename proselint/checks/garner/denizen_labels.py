# -*- coding: utf-8 -*-
"""MAU109: Denizen labels.

---
layout:     post
error_code: MAU109
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      denizen labels
date:       2014-06-10 12:31:19
categories: writing
---

Denizen labels.

"""
import re
from proselint.tools import memoize


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "MAU109"
    msg = "'{}' is the preferred denizen label."

    preferences = [

        ["Michigander",       ["Michiganite"]],
        ["Indianan",          ["Indianian"]],

    ]
    errors = []
    for p in preferences:
        for r in p[1]:
            for m in re.finditer("\s{}\s".format(r), text, flags=re.IGNORECASE):
                errors.append((m.start()+1, m.end(), err, msg.format(p[0])))

    return errors
