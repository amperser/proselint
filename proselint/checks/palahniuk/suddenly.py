# -*- coding: utf-8 -*-
u"""Suddenly.

---
layout:     post
source:     Reference for Writers
source_url: http://bit.ly/1E94vyD
title:      suddenly
date:       2014-06-10 12:31:19
categories: writing
---

“Sudden” means quickly and without warning, but using the word “suddenly” both
slows down the action and warns your reader. Do you know what’s more effective
for creating the sense of the sudden? Just saying what happens.

When using “suddenly,” you communicate through the narrator that the action
seemed sudden. By jumping directly into the action, you allow the reader to
experience that suddenness first hand. “Suddenly” also suffers from being
nondescript, failing to communicate the nature of the action itself; providing
no sensory experience or concrete fact to hold on to. Just … suddenly.

Feel free to employ “suddenly” in situations where the suddenness is not
apparent in the action itself. For example, in “Suddenly, I don’t hate you
anymore,” the “suddenly” substantially changes the way we think about the
shift in emotional calibration.
"""
from tools import memoize, existence_check


@memoize
def check_ellipsis(text):
    """Use an ellipsis instead of three dots."""
    err = "palahniuk.suddenly"
    msg = u"Suddenly is nondescript, slows the action, and warns your reader."
    regex = "Suddenly,"

    return existence_check(text, [regex], err, msg, max_errors=3,
                           require_padding=False, offset=-1, ignore_case=False)
