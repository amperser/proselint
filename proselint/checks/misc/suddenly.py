"""
Suddenly.

---
layout:     post
source:     Reference for Writers
source_url: http://bit.ly/1E94vyD
title:      suddenly
date:       2014-06-10
categories: writing
---

“Sudden” means quickly and without warning, but using the word “suddenly” both
slows down the action and warns your reader. Do you know what's more effective
for creating the sense of the sudden? Just saying what happens.

When using “suddenly,” you communicate through the narrator that the action
seemed sudden. By jumping directly into the action, you allow the reader to
experience that suddenness first hand. “Suddenly” also suffers from being
nondescript, failing to communicate the nature of the action itself; providing
no sensory experience or concrete fact to hold on to. Just … suddenly.

Feel free to employ “suddenly” in situations where the suddenness is not
apparent in the action itself. For example, in “Suddenly, I don't hate you
anymore,” the “suddenly” substantially changes the way we think about the
shift in emotional calibration.
"""
from __future__ import annotations

from proselint.checks import CheckResult, Pd, existence_check, limit_results

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "Suddenly, it all made sense.",
]


@limit_results(3)
def check(text: str) -> list[CheckResult]:
    """Advice on sudden vs suddenly."""
    err = "misc.suddenly"
    msg = "Suddenly is nondescript, slows the action, and warns your reader."
    regex = "Suddenly,"

    return existence_check(
        text,
        [regex],
        err,
        msg,
        padding=Pd.disabled,
        ignore_case=False,
    )
