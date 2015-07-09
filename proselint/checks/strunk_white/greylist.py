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
from tools import memoize
import re


@memoize
def check(text):
    """Check the text."""
    err = "strunk_white.greylist"
    msg = "Use of '{}'. {}"

    bad_words = [
        "obviously",
        "utilize"
    ]

    explanations = {
        "obviously":
        "This is obviously an inadvisable word to use.",
        "utilize":
        r"Do you know anyone who *needs* to utilize the word utilize?"
    }

    errors = []
    for word in bad_words:
        occ = [m for m in re.finditer(word, text.lower())]
        for o in occ:
            errors.append((o.start(), o.end(), err,
                          msg.format(word, explanations[word])))

    return errors
