# -*- coding: utf-8 -*-
"""Phrasal adjectives.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      Phrasal adjectives
date:       2014-06-10 12:31:19
categories: writing
---

Phrasal adjectives.

"""
from tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "garner.phrasal_adjectives"
    msg = u"""No hyphen is necessary in phrasal adjectives with an adverb
              ending in -ly."""

    return existence_check(text, ["ly-"], err, msg,
                           require_padding=False, offset=-1)
