# -*- coding: utf-8 -*-
"""Style checks for the existence of certain words.

---
layout:     post
source:     Ryan McCarl
source_url: http://ryanmccarl.com
title:      McCarl StyleChecks - Preferred Forms
date:       2019-03-12
categories: style, usage
---

Points out preferred form.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "mccarl.stylecheck"
    msg = "Consider '{}' instead."

    list = [
        ["judicial resources", [r"the Court(')?s time( and resources)?"]],
        ["each", ["each also"]],
        ["straightforward", ["plain and straightforward"]],
        ["pretending not to understand", ["deliberately misconstruing"]],
        ["prior to", ["before"]],
        ["agree", ["reach agreement"]],
        ["use", ["utilize"]],
    ]

    return preferred_forms_check(text, list, err, msg)
