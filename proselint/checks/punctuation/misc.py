"""
Punctuation.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Punctuation
date:       2014-06-10
categories: writing
---

Dates.

"""

from __future__ import annotations

from proselint.checks import (
    CheckRegistry,
    CheckSpec,
    Existence,
    ExistenceSimple,
    Pd,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "A cat can sleep 20.5 hours a day.",
    "I asked the Prof. what to do",
]

examples_fail = [
    "See Smith et. al.",
    "i drive 5,5 kmh.",
    "I usually wait an hour. and then another.",
]

check_garner = CheckSpec(
    Existence(
        [
            r"et\. al",
            r"et\. al\.",
        ],
        padding=Pd.sep_in_txt,
    ),
    "punctuation.misc.garner",
    "Misplaced punctuation. It's 'et al.'",
)

# src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L325
check_lower_case_after_punctuation = CheckSpec(
    ExistenceSimple(
        # TODO: this can have false positives after abbreviations
        r"\b[a-z]+[\.!\?]\s+[a-z]+\b",
        # en, TODO: add more, sync with misc.numbers.sentence
        # exceptions_de = ["bzw.", "ca.", "cf.", "etc.", "vgl.",
        #                  "no.", "m.E", "m.a.W.", "u.U.", "s.u.", "z.B."]
        exceptions=(
            r"al\.",
            r"lat\.",
            r"vs\.",
            r"etc\.",
            r"Prof\.",
            r"Dr\.",
            r"[vV]ol\.",
            r"[fF]ig\.",
        ),
    ),
    "punctuation.misc.lower_case",
    "Is the lowercase letter correct after the punctuation here? Found '{}'.",
)

# TODO: determine validity of this
# src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L325
# NOTE: tnt also checks for German numbers, not implemented here
check_comma_digits = CheckSpec(
    # NOTE: intentional words_in_txt
    ExistenceSimple(Pd.words_in_txt.value.format(r"\d+,\d+")),
    "punctuation.misc.comma_digits",
    "In English ',' is used as a decimal separator.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    registry.register_many((
        check_garner,
        check_lower_case_after_punctuation,
        check_comma_digits,
    ))
