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

Elementary

"""

from __future__ import annotations

try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files

import proselint
from proselint.checks import CheckSpec, ReverseExistence

examples_pass = [
    "A boy and his goat went to a farm.",
    "I am tired.",
    "Your body is made of water.",
]

examples_fail = [
    "Cells make up your body.",
    "I love clowns.",
    "I hate cells and clowns.",
]

_CSV_PATH = "checks/restricted/elementary.csv"
with files(proselint).joinpath(_CSV_PATH).open("r") as data:
    ELEMENTARY_WORDS = data.read().split()

check_elementary = CheckSpec(
    ReverseExistence(ELEMENTARY_WORDS),
    "restricted.elementary",
    "'{}' is not a word kids learn in elementary school.",
)

__register__ = (check_elementary,)
