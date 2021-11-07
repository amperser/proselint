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
from proselint.tools import existence_check, max_errors, memoize, ppm_threshold


@max_errors(1)
@memoize
def check_repeated_exclamations(text):
    """Check the text."""
    err = "leonard.exclamation.multiple"
    msg = "Stop yelling. Keep your exclamation points under control."

    regex = r"[\!]\s*?[\!]{1,}"

    return existence_check(text, [regex], err, msg, require_padding=False,
                           ignore_case=False, dotall=True)


@ppm_threshold(30)
@memoize
def check_exclamations_ppm(text):
    """Make sure that the exclamation ppm is under 30."""
    err = "leonard.exclamation.30ppm"
    msg = "More than 30 ppm of exclamations. Keep them under control."

    regex = r"\w!"

    return existence_check(text, [regex], err, msg, require_padding=False)
