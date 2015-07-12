# -*- coding: utf-8 -*-
"""Filthy words.

---
layout:     post
source:     George Carlin
source_url: https://youtu.be/kyBH5oNQOS0
title:      filthy words
date:       2014-06-10 12:31:19
categories: writing
---

Filthy words.

"""
from tools import existence_check, memoize


@memoize
def check_debased_language(text):
    """Check the text."""
    err = "carlin.filth"
    msg = u"""Nobody ever tells you this as a kid, but you're supposed to avoid
        this word."""

    list = [
        "shit",
        "piss",
        "fuck",
        "cunt",
        "cocksucker",
        "motherfucker",
        "tits",
        "fart",
        "turd",
        "twat",
    ]

    return existence_check(text, list, err, msg)
