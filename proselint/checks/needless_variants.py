"""
Needless variants.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      needless variants
date:       2014-06-10 12:31:19
categories: writing
---

Points out use of needless variants.

"""

from importlib.resources import files

from proselint import checks
from proselint.backports import batched
from proselint.registry.checks import BATCH_COUNT, Check, types

NEEDLESS_VARIANTS_RAW = (
    (files(checks) / "needless-variants").read_text().splitlines()
)

checks_needless_variants = tuple(
    Check(
        check_type=types.PreferredFormsSimple(
            items=dict(line.split(",", maxsplit=1) for line in lines)
        ),
        path="needless_variants",
        message="Needless variant. '{}' is the preferred form.",
    )
    for lines in batched(NEEDLESS_VARIANTS_RAW, BATCH_COUNT)
)

__register__ = checks_needless_variants
