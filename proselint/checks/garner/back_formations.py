# -*- coding: utf-8 -*-
"""MAU102: Back-formations.

---
layout:     post
error_code: MAU102
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      back-formations
date:       2014-06-10 12:31:19
categories: writing
---

Back-formations.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(blob):
    """Suggest the preferred forms."""
    err = "MAU102"
    msg = "Back-formation. '{}' is the preferred form."

    list = [
        ["improper",       ["improprietous"]],
    ]

    return preferred_forms_check(blob, list, err, msg)
