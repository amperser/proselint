# -*- coding: utf-8 -*-
"""Words not fit for print.

---
layout:     post
source:     The NY Times
source_url: http://arnoldzwicky.org/2012/04/16/the-gray-lady-avoids/
title:      words not fit for print
date:       2014-06-10 12:31:19
categories: writing
---

Words not fit for print in the NY Times.

"""
from tools import existence_check, memoize


@memoize
def check_debased_language(text):
    """Check the text."""
    err = "nytimes.banned_words"
    msg = u"This word is not fit for print."

    list = [
        "fuck",
    ]

    return existence_check(text, list, err, msg)
