"""Template for new checks

---
layout:     post
source:     Nobody
source_url: ???
title:      First line is always wrong.
date:       2014-06-10
categories: writing
---

Note:

- this is just a small example / template
- there are more lint-checks available in the parent-dir/__init__.py
- check-fn must at least begin with "check" to be found & used
    - so check() & check_xyz() are fine
- the _pass and _fail examples at the start are part of the unittests and get checked
    - this mixed approach is unconventional, but maintaining much easier
    - they are now mandatory for each check-file

"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "This is the famous first line.",
]


def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    error_code = "inprogress.template"
    msg = "First line always has an error."

    items = ["first line"]

    return existence_check(text, items, error_code, msg, ignore_case=False)
