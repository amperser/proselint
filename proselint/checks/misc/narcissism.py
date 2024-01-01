"""Professional narcissism.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      professional narcissism
date:       2014-06-10 12:31:19
categories: writing
---

Points out academic narcissism.

"""
from __future__ import annotations

from ...lint_cache import memoize
from ...lint_checks import ResultCheck, existence_check


@memoize
def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "pinker.narcissism"
    msg = "Professional narcissism. Talk about the subject, not its study."

    narcissism = [
        "In recent years, an increasing number of [a-zA-Z]{3,}sts have",
    ]

    return existence_check(text, narcissism, err, msg)
