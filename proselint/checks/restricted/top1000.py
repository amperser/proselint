"""Check if the text contains only words in top 1000 most popular words.

---
layout:     Website
source:     THE UP-GOER FIVE TEXT EDITOR
source_url: https://splasho.com/upgoer5/
title:      ?
date:       2023-04-16 16:32:01
categories: writing/app
---

Top 1000.

"""
try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files

import proselint
from proselint.tools import reverse_existence_check

_CSV_PATH = 'checks/restricted/top1000.csv'

with files(proselint).joinpath(_CSV_PATH).open('r') as data:
    TOP1000_WORDS = data.read().split()



def check(text):
    """Check the text."""
    err = "restricted.top1000"
    msg = "'{}' is not in the top 1000 most common words."

    return reverse_existence_check(text, TOP1000_WORDS, err, msg)
