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

from __future__ import annotations

try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files

import proselint
from proselint.checks import CheckSpec, ReverseExistence

examples_pass = [
    "I am blonde.",
    "I'm gonna listen to music tonight.",
    "I will go to sleep because I have school.",
]

examples_fail = [
    "I am tired.",
    "I hate broccoli.",
    "I am tired and hate broccoli.",
]

_CSV_PATH = "checks/restricted/top1000.csv"

with files(proselint).joinpath(_CSV_PATH).open("r") as data:
    TOP1000_WORDS = data.read().split()

check_top1000 = CheckSpec(
    ReverseExistence(TOP1000_WORDS),
    "restricted.top1000",
    "'{}' is not in the top 1000 most common words.",
)

__register__ = (check_top1000,)
