"""Template for new checks

---
layout:     post
source:     Nobody
source_url: ???
title:      First line is always wrong.
date:       2014-06-10 12:31:19
categories: writing
---

Note:
    - this is just a small example
    - there are more lint-checks available
    - check-fn must at least begin with "check" to be found,
      so check() & check_xyz() are fine
    - don't forget to add unittests and an entry in the base-config

"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import existence_check


def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    error_code = "inprogress.template"
    msg = "First line always has an error."

    items = ["first line"]

    # note:
    return existence_check(text, items, error_code, msg, ignore_case=False)
