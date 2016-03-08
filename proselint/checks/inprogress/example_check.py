# -*- coding: utf-8 -*-
"""First line is always wrong.

---
layout:     post
source:     Nobody
source_url: ???
title:      Firse line is always wrong.
date:       2014-06-10 12:31:19
categories: writing
---

The first line always is always wrong.

"""
from proselint.tools import reverse


def check(text):
    """Check the text."""
    error_code = "example.first"
    msg = "First line always has an error."

    reverse(text)

    return [(1, 1, error_code, msg)]
