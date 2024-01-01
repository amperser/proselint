"""Back-formations.

---
layout:     post
source:     The sense of style
source_url: http://amzn.to/1EOUZ5g
title:      back-formations
date:       2014-06-10 12:31:19
categories: writing
---

Back-formations.

"""
from __future__ import annotations

from ...lint_cache import memoize
from ...lint_checks import ResultCheck, preferred_forms_check


@memoize
def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "pinker.latin"
    msg = "Use English. '{}' is the preferred form."

    items = [
        ["other things being equal", ["ceteris paribus"]],
        ["among other things", ["inter alia"]],
        ["in and of itself", ["simpliciter"]],
        ["having made the necessary changes", ["mutatis mutandis"]],
    ]

    return preferred_forms_check(text, items, err, msg)
