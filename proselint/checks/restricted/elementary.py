"""Check if the text contains only words that elementary kids would know.

---
layout:     Website
source:     The Basic Spelling Vocabulary List
source_url: https://tinyurl.com/5n6nczv2
title:      elementary
date:       2023-04-20 11:53:00
categories: writing
---

Elementary

"""
try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files

import proselint
from proselint.tools import memoize, reverse_existence_check

_CSV_PATH = 'checks/restricted/elementary.csv'
with files(proselint).joinpath(_CSV_PATH).open('r') as data:
    ELEMENTARY_WORDS = data.read().split()


@memoize
def check(text):
    """Check the text."""
    err = "restricted.elementary"
    msg = "'{}' is not a word kids learn in elementary school."

    return reverse_existence_check(text, ELEMENTARY_WORDS, err, msg)
