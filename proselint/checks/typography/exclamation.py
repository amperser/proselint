"""Too much yelling.

---
layout:     post
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10 12:31:19
categories: writing
---

Too much yelling.

"""
from __future__ import annotations

from proselint.checks import Pd
from proselint.checks import ResultCheck
from proselint.checks import existence_check
from proselint.checks import limit_results
from proselint.checks import ppm_threshold


@limit_results(1)
def check_repeated_exclamations(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "leonard.exclamation.multiple"
    msg = "Stop yelling. Keep your exclamation points under control."

    items = [r"[\!]\s*?[\!]{1,}"]

    return existence_check(
        text,
        items,
        err,
        msg,
        padding=Pd.disabled,
        ignore_case=False,
        dotall=True,
    )


@ppm_threshold(30)  # TODO: isn't that way too low?
def check_exclamations_ppm(text: str) -> list[ResultCheck]:
    """Make sure that the exclamation ppm is under 30."""
    err = "leonard.exclamation.30ppm"
    msg = "More than 30 ppm of exclamations. Keep them under control."

    items = [r"\w!"]

    return existence_check(text, items, err, msg, padding=Pd.disabled)
