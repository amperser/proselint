# -*- coding: utf-8 -*-
"""Brian Garner recommendations from various sources.

Resources:
Garner, Modern American Usage
Garner, Modern Legal Usage
Garner, Lawprose Blog
http://www.lawprose.org/lawprose-blog/
https://abajournal.com/magazine/article/ax_these_terms_from_your_legal_writing/

---
layout:     post
source:     Various Brian Garner sources
source_url: http://www.lawprose.org/lawprose-blog/
title:      Brian Garner - Jargon
date:       2018-11-19 11:35:00
categories: writing
---

"""
from proselint.tools import memoize, existence_check


@memoize
def check(text):
    """Check the text."""
    err = "garner.jargon"
    msg = u"""'{}' may be jargon, legalese, or a redundancy."""

    jargon = [
        "acknowledge same",
        "aid and abet",
        "aid and comfort"
        "conclusory",
        "deem",
        "each and every",
        "for same",
        "one and only",
        "provided that",
        "such",
        "to same",
        "witnesseth",
    ]

    return existence_check(text, jargon, err, msg, join=True)
