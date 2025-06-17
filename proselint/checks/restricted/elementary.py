"""
Check if the text contains only words that elementary kids would know.

---
layout:     Website
source:     The Basic Spelling Vocabulary List
source_url: https://tinyurl.com/5n6nczv2
title:      elementary
date:       2023-04-20 11:53:00
categories: writing
---

Elementary.

"""

from importlib.resources import files

from proselint.checks import restricted
from proselint.registry.checks import Check, types

ELEMENTARY_TERMS = (files(restricted) / "elementary").read_text().splitlines()

check = Check(
    check_type=types.ReverseExistence(allowed=set(ELEMENTARY_TERMS)),
    path="restricted.elementary",
    message="'{}' is not a word kids learn in elementary school.",
)

__register__ = (check,)
