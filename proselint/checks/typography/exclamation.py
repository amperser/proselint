"""
Too much yelling.

---
layout:     post
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10
categories: writing
---

Too much yelling.

"""

from __future__ import annotations

from proselint.checks import (
    CheckRegistry,
    CheckSpec,
    Existence,
    Pd,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "The QUICK BROWN fox juMPED over the lazy cat.",
    "Sally sells seashells and they were too expensive!",
]

examples_fail = [
    "Sally sells seashells and they were too expensive!!!!",
    "Sally sells seashells and they were too expensive! They were not!",
    "I'm really excited!!",
    "I'm really excited! Really!",
]


# TODO: reimplement limit_results
# FIXME: this is duplicated by hyperbole.misc
check_repeated_exclamations = CheckSpec(
    Existence([r"[\!]\s*?[\!]{1,}"], padding=Pd.disabled, dotall=True),
    "typography.exclamation.leonard.repeated",
    "Stop yelling. Keep your exclamation points under control.",
    ignore_case=False,
)

# TODO: reimplement ppm_threshold, evaluate whether 30 ppm is too low
check_exclamations_ppm = CheckSpec(
    Existence(
        [r"\w!"],
        padding=Pd.disabled,
    ),
    "typography.exclamation.leonard.30ppm",
    "More than 30 ppm of exclamations. Keep them under control.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    registry.register_many((
        check_repeated_exclamations,
        check_exclamations_ppm,
    ))
