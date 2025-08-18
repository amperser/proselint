"""
Check if the text contains only words in top 1000 most popular words.

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

from importlib.resources import files

from proselint.checks import restricted
from proselint.registry.checks import Check, types

TOP1000_TERMS = (files(restricted) / "top1000").read_text().splitlines()

check = Check(
    check_type=types.ReverseExistence(allowed=set(TOP1000_TERMS)),
    path="restricted.top1000",
    message="'{}' is not in the top 1000 most common words.",
)

__register__ = (check,)
