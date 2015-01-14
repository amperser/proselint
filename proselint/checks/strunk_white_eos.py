"""STW100: Use of greylisted words.

---
layout:     post
error_code: STW100
source:     Strunk & White
source_url: ???
title:      STW100&#58; Use of greylisted words
date:       2014-06-10 12:31:19
categories: writing
---

Strunk & White say:


"""

import re


def check(text):
    error_code = "STW100"
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
        occurrences = [
            m.start() for m in re.finditer(word, text.lower())
        ]
        for o in occurrences:
            errors.append((1, o, error_code, msg.format(word, explanations[word])))
    return errors
