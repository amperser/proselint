"""
Use of greylisted words.

---
layout:     post
source:     Strunk & White
source_url: ???
title:      Use of greylisted words
date:       2014-06-10 12:31:19
categories: writing
---

Use of greylisted words.

"""

from itertools import chain

from proselint.registry.checks import Check, CheckResult, types

GREYLISTED_TERMS = {
    "obviously": "This is obviously an inadvisable word to use.",
    "utilize": "Do you know anyone who needs to utilize the word utilize?",
}


def _check_greylist(text: str, check: Check) -> list[CheckResult]:
    """Check the text."""
    return list(
        chain.from_iterable(
            types.ExistenceSimple(pattern=term).check(
                text,
                Check(
                    check_type=check.check_type,
                    path=check.path,
                    message=check.message.format(term, explanation),
                ),
            )
            for term, explanation in GREYLISTED_TERMS.items()
        )
    )


check_greylist = Check(
    check_type=_check_greylist,
    path="misc.greylist",
    message="Use of '{}'. {}",
)

__register__ = (check_greylist,)
