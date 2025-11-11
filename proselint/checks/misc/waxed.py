"""
Waxed lyrical.

---
layout:     post
source:     Fowler's Modern English Usage
source_url: bit.ly/1YBG8QJ
title:      Waxed lyrical
date:       2016-03-10 14:48:42
categories: writing
---

Fowler's says:
Its primary meaning 'grow larger, increase' (as opposed to 'wane') leads
naturally to the sense 'pass into a specified state or mood, begin to use a
specified tone. In this meaning a following modifier must be an adj. not an
adverb ('He waxed enthusiastic [not enthusiastically] about Australia').

"""

from collections.abc import Iterator

from proselint.registry.checks import Check, CheckResult, Padding, types

WAXES = ("wax", "waxes", "waxed", "waxing")
MODIFIERS = {
    "ebulliently": "ebullient",
    "ecstatically": "ecstatic",
    "eloquently": "eloquent",
    "enthusiastically": "enthusiastic",
    "euphorically": "euphoric",
    "indignantly": "indignant",
    "lyrically": "lyrical",
    "melancholically": "melancholic",
    "metaphorically": "metaphorical",
    "nostalgically": "nostalgic",
    "patriotically": "patriotic",
    "philosophically": "philosophical",
    "poetically": "poetic",
    "rhapsodically": "rhapsodic",
    "romantically": "romantic",
    "sentimentally": "sentimental",
}


def _check_waxed(text: str, check: Check) -> Iterator[CheckResult]:
    """Suggest the preferred forms."""
    if not check.engine.make_set(Padding.RAW, WAXES).exists_in(text):
        return iter(())

    return types.PreferredFormsSimple(
        items={
            f"{wax} {original}": f"{wax} {replacement}"
            for original, replacement in MODIFIERS.items()
            for wax in WAXES
        }
    ).check(text, check)


check_waxed = Check(
    check_type=_check_waxed,
    path="misc.waxed",
    message="The modifier following 'waxed' must be an adj.: '{}' is correct.",
)

__register__ = (check_waxed,)
