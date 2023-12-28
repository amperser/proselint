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

from proselint.tools import ResultCheck, memoize


@memoize
def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "strunk_white.greylist"
    msg = "Use of '{}'. {}"

    bad_words = [
        "obviously",
        "utilize",
    ]

    explanations = {
        "obviously":
        "This is obviously an inadvisable word to use.",
        "utilize":
        r"Do you know anyone who *needs* to utilize the word utilize?",
    }

    results = []
    for word in bad_words:
        occ = list(re.finditer(word, text.lower()))
# TODO: faster replacement
#        results += [(
#                o.start(),
#                o.end(),
#                err,
#                msg.format(word, explanations[word]),
#                None) for o in occ]
        for o in occ:
            results.append((
                o.start(),
                o.end(),
                err,
                msg.format(word, explanations[word]),
                None))

    return results
