"""Use of greylisted words.

---
layout:     post
source:     Strunk & White
source_url: ???
title:      Use of greylisted words
date:       2014-06-10 12:31:19
categories: writing
---

Strunk & White say:


"""
from __future__ import annotations

import re

from ...lint_cache import memoize
from ...lint_checks import ResultCheck


@memoize
def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "strunk_white.greylist"
    msg = "Use of '{}'. {}"

    bad_words = {
        "obviously": "This is obviously an inadvisable word to use.",
        "utilize": r"Do you know anyone who *needs* to utilize the word utilize?",
    }

    return [
        (occ.start(), occ.end(), err, msg.format(word, bad_words[word]), None)
        for word in bad_words
        for occ in list(re.finditer(word, text.lower()))
    ]
