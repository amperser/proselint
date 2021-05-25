# -*- coding: utf-8 -*-
"""Style checks for the existence of certain words.

---
layout:     post
source:     Ryan McCarl
source_url: http://ryanmccarl.com
title:      McCarl StyleChecks - Existence
date:       2019-03-12
categories: style, usage
---


"""
from proselint.tools import memoize, existence_check


@memoize
def check(text):
    """Check the text."""
    err = "mccarl.stylecheck"
    msg = u"Consider deleting or replacing: '{}'."

    deletethese = [
        "all of",
        "any of",
        "at all",
        "fortunately",
        "great deal",
        "greatly",
        "in any way",
        "plainly",
        "really",
        "seriously",
        "utterly",
        "wholly",
        r"\w+ly\b"
        "extremely"
    ]

    return existence_check(text, deletethese, err, msg)
