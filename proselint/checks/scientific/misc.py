"""Scientific writing.

---
layout:     post
source:     div
source_url:
title:      scientific
date:       2024-01-14
categories: writing
---

Dates.

"""
from __future__ import annotations

from proselint.checks import ResultCheck, simple_existence_check, Pd
from proselint.checks import existence_check


def check_num_unit(text: str) -> list[ResultCheck]:
    """Check numbers"""
    # TODO: add more than the SI-Units: N,
    # src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L325
    err = "scientific.misc.num_unit"
    msg = "In scientific writings there is a whitespace between number and its unit, here '{}'."
    regex = Pd.sep_in_txt.value.format("(\d+(k|M|G|T|E|m|u|n|p|f)?(s|m|g|A|K|mol|cd|n))")
    return simple_existence_check(text, regex, err, msg, ignore_case=False)
