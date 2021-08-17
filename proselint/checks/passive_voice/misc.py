# -*- coding: utf-8 -*-
"""Check for constructs that may signal passive voice.

Resources:
https://writingcenter.unc.edu/tips-and-tools/passive-voice/
https://owl.english.purdue.edu/owl/owlprint/539/

---
layout:     post
source:     Purdue OWL
source_url: https://owl.english.purdue.edu/owl/owlprint/539/
title:      Passive voice
date:       2018-06-12 21:35:00
categories: writing
---

"""

from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check for constructs that may signal passive voice."""
    err = "passive_voice.misc"
    msg = u"This seems to be in passive voice. Consider using active voice."
    list = [(r"\b(?:be|is|am|are|was|were|have|has|had|get|got)"
             r"\b[\w\s]{0,28}(?:d|(?<!whe)|ne?|left|being|made)"
             r"\b(?:by)\b"),
            r"let(\b[\w\s]+\b){4,}?be"]

    return existence_check(text, list, err, msg)
