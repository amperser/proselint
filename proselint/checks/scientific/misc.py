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

import re

from proselint.checks import Pd
from proselint.checks import ResultCheck
from proselint.checks import consistency_check
from proselint.checks import existence_check
from proselint.checks import preferred_forms_check_opti
from proselint.checks import preferred_forms_check_regex
from proselint.checks import simple_existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "ignore /30m of this.",
    "this 5\xa0km is fine.",
    "this 5 km is also fine - will be flagged by check.numbers",
]

examples_fail = [
    "I walked 30km to get there.",
    "I walked .9km to get there.",
    "I walked 7.9km to get there.",
    "that statement is ridiculous.",
    "Attempts were made to get there.",
    "This works not very well.",
    "this is a low doped region.",
    "The progress is huge.",
    "This shows a systematical error.",
    "We present you something I built.",
]


def check_num_unit(text: str) -> list[ResultCheck]:
    """Check numbers with units"""
    # TODO: add more than the SI-Units
    # src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L325
    err = "scientific.misc.num_unit"
    msg = (
        "In scientific writings there is a non-breaking space (U+00A0, ~ in latex) "
        "between number and its unit, here '{}'."
    )
    regex = (
        r"\s\d*\.?\d+(?:k|M|G|T|E|m|u|µ|n|p|f)?"
        r"(?:s|m|g|A|K|mol|cd|Hz|dB|%|N|cal|C|F|V)+\b"
    )
    # - start with a space and a number that may contain a decimal.point
    # - no space afterward, optional exponent, common units
    return simple_existence_check(text, regex, err, msg, ignore_case=False)


def check_emotion(text: str) -> list[ResultCheck]:
    """avoid the following words"""
    # src = https://www.sciencewrites.org/dos-and-donts
    err = "scientific.misc.emotion"
    msg = "Scientific writing should not contain emotionally laden terms like '{}'"
    items = [
        "ridiculous",
        "unfortunately",
        "obvious",
        "obviously",
    ]
    return existence_check(text, items, err, msg)


def check_weasel(text: str) -> list[ResultCheck]:
    """avoid the following words"""
    # src = https://www.sciencewrites.org/dos-and-donts
    err = "scientific.misc.weasel"
    msg = "Scientific writing should not build on uncertainty like '{}'"
    items = ["attempts"]
    return existence_check(text, items, err, msg)


def check_conversation(text: str) -> list[ResultCheck]:
    """avoid the following words"""
    # src = https://www2.spsc.tugraz.at/www-archive/downloads/DoesandDonts%20in%20scientific%20writing%20reisenhofer%20tumfart.pdf
    err = "scientific.misc.conversation"
    msg = "Scientific writing should not chatter / converse like '{}'"
    items = ["Well", "you see", "yes", "let's move on"]
    return existence_check(text, items, err, msg)


def check_wrong(text: str) -> list[ResultCheck]:
    """avoid the following words"""
    # src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L522
    err = "scientific.misc.wrong"
    msg = "Avoid technically wrong terms like '{}'"
    items = ["lowly doped", "low doped"]
    return existence_check(text, items, err, msg)


def check_avoid_misc(text: str) -> list[ResultCheck]:
    """avoid the following words"""
    # src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L522
    err = "scientific.misc.avoid"
    msg = "Scientific writing should avoid terms like '{}'"
    items = ["becomes", "gets", "huge", "very"]
    return existence_check(text, items, err, msg)


def check_preferred(text: str) -> list[ResultCheck]:
    # src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L522
    err = "scientific.misc.preference"
    msg = (
        "In scientific writing some terms are less preferred or wrong. "
        "Consider using '{}' instead of '{}'."
    )

    items: dict[str, str] = {
        "insignificant": "not significant",
        "though": "although",
        "they're": "they are",
        "isn't": "is not",
        "can't": "cannot",
        "can not": "cannot",
        "a bit": "somewhat",
        "fair agreement": "reasonable agreement",
        "well agreement": "good agreement",
        "low till": "low to",
        "two times": "twice",
        "can be attributed": "is attributed",
        "large conductivity": "high conductivity",
        "air-volatile": "air-sensitive",
        "in the case of": "in case of",
        "agreement to": "agreement with",
        "automatization": "automation",
        "beside": "besides",
        "consistent to": "consistent with",
        "contra-intuitive": "counter-intuitive",
        "data is": "data are",
        "fullfill": "fulfill",
        "informations": "information",
        "in to": "into",
        "let to": "led to",
        "little affect": "little effect",
        "orientated": "oriented",
        "persons": "people",
        "possible, that": "possible that",
        "rises the": "raises the",
        "semi conductor(|s)": "semiconductor(s)",
        "spacial": "spatial",
        "systematical error": "systematic",
        "temperature dependency": "temperature dependence",
        "the ones": "those",
        "this data": "these data",
        "where shown": "were shown",
        "where derived": "were derived",
        "where observed": "were observed",
        "where used": "were used",
        "where removed": "were removed",
        "where introduced": "were introduced",
        "uppon": "upon",
        # https://www.sciencewrites.org/dos-and-donts
        "utilize": "use",
        "substantiate": "support",
        "in accordance with": "agree",
    }

    return preferred_forms_check_opti(text, items, err, msg)


def check_preferred_regex(text: str) -> list[ResultCheck]:
    # src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L522
    err = "scientific.misc.preference"
    msg = (
        "In scientific writing some terms are less preferred or wrong. "
        "Consider using '{}' instead of '{}'."
    )

    items = [
        ["photovoltaic", ["solar cell(|s)"]],
        ["increases", ["(is|are) increasing"]],
        ["decreases", ["(is|are) decreasing"]],
        ["***(p|n)-dop(ing|ed)***", ["(p|n) dop(ing|ed)"]],
        # TODO: active regex or no clean replacement
        # ["too ***", ["to strong", "to weak\w*", "to strong\w*"]],
        # TODO: except 'due to *'
    ]
    return preferred_forms_check_regex(text, items, err, msg)


def check_this_vs_those(text: str) -> list[ResultCheck]:
    # src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L812
    # TODO: magnet for false positives -> remove? seems niche
    err = "scientific.misc.this_vs_those"
    msg = "(Maybe) wrong plural for '{}' -> use 'those *'"
    exceptions = [
        "this results in",
        r"this \w+ss\b",
        r"this is\b",
        r"this (agrees|allows|cancels|corresponds|enables|ensures|explains|has)",
        r"this (hypothesis|involves|indicates|leads|reduces|shows|suggests|thesis)",
    ]
    expt_regex = "(" + "|".join(exceptions) + ")"
    results = []
    for _m in re.finditer(r"\b(this +\w+s(\s\w+)?)\b", text, flags=re.IGNORECASE):
        _res = _m.group(0).strip().lower()
        if any(re.finditer(expt_regex, _res)):
            continue
        results.append((_m.start(), _m.end(), err, msg.format(_res), None))
    return results


def check_we_or_i(text: str) -> list[ResultCheck]:
    # src = https://www.sciencewrites.org/dos-and-donts
    err = "scientific.misc.we_or_i"
    msg = "Decide if you alone ('{}') or a team ('{}') has written the report"

    word_pairs = [
        [Pd.words_in_txt.value.format("we"), Pd.words_in_txt.value.format("i")]
    ]
    return consistency_check(text, word_pairs, err, msg, ignore_case=True)


# TODO: skipped in TNT:
#       - L812 this vs those
#     - deg C or deg K is old, deg not used anymore
