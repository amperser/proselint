# -*- coding: utf-8 -*-
"""Back-formations.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
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
    err = "misc.back_formations"
    msg = "Back-formation. '{}' is the preferred form."

    list = [
        ["improper",       ["improprietous"]],
    ]

    return preferred_forms_check(text, list, err, msg)
