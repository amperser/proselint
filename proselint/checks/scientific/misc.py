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
from proselint.checks import preferred_forms_check
from proselint.checks import simple_existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "I walked 30km to get there.",
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
    # TODO: add more than the SI-Units: N,
    # src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L325
    err = "scientific.misc.num_unit"
    msg = (
        "In scientific writings there is a whitespace between number and its unit, "
        "here '{}'."
    )
    regex = Pd.sep_in_txt.value.format(
        r"\d+(k|M|G|T|E|m|u|µ|n|p|f)?(s|m|g|A|K|mol|cd|n|Hz|dB|%)"
    )
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
    items = [
        ["not significant", ["insignificant"]],
        ["although", ["though"]],
        ["they are", ["they're"]],
        ["is not", ["isn't"]],
        ["cannot", ["can't"]],
        ["cannot", ["can not"]],
        ["somewhat", ["a bit"]],
        ["reasonable agreement", ["fair agreement"]],
        ["good agreement", ["well agreement"]],
        ["low to", ["low till"]],
        ["twice", ["two times"]],
        ["increases", ["(is|are) increasing"]],
        ["decreases", ["(is|are) decreasing"]],
        ["is attributed", ["can be attributed"]],
        ["high conductivity", ["large conductivity"]],
        ["air-sensitive", ["air-volatile"]],
        ["in case of", ["in the case of"]],
        ["photovoltaic", ["solar cell(|s)"]],
        # ["whether", ["weather"]],
        ["agreement with", ["agreement to"]],
        ["automation", ["automatization"]],
        ["besides", ["beside"]],
        ["consistent with", ["consistent to"]],
        ["counter-intuitive", ["contra-intuitive"]],
        ["data are", ["data is"]],
        ["fulfill", ["fullfill"]],
        ["information", ["informations"]],
        ["into", ["in to"]],
        ["led to", ["let to"]],
        ["little effect", ["little affect"]],
        ["oriented", ["orientated"]],
        ["people", ["persons"]],
        ["possible that", ["possible, that"]],
        [
            "***(p|n)-dop(ing|ed)***",
            ["(p|n) dop(ing|ed)"],
        ],  # todo: no clean replacement, more below
        ["raises the", ["rises the"]],
        ["semiconductor(s)", ["semi conductor(|s)"]],
        ["spatial", ["spacial"]],
        ["systematic", ["systematical error"]],
        ["temperature dependence", ["temperature dependency"]],
        ["those", ["the ones"]],
        ["these data", ["this data"]],
        # ["too ***", ["to strong", "to weak\w*", "to strong\w*"]],
        # todo: except 'due to *'
        [
            "were ***",
            [
                "where shown",
                "where derived",
                "where observed",
                "where used",
                "where removed",
                "where introduced",
            ],
        ],
        ["upon", ["uppon"]],
        # https://www.sciencewrites.org/dos-and-donts
        ["use", ["utilize"]],
        ["support", ["substantiate"]],
        ["agree", ["in accordance with"]],
    ]
    return preferred_forms_check(text, items, err, msg)


def check_this_vs_those(text: str) -> list[ResultCheck]:
    # src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L812
    # TODO: magnet for false positives -> remove? seems niche
    err = "scientific.misc.this_vs_those"
    msg = "(Maybe) wrong plural for '{}' -> use 'those *'"
    exceptions = [
        "this results in",
        r"this \w+ss\b",
        r"this is\b",
        r"this (agrees|allows|cancels|corresponds|enables|explains|has)",
        r"this (hypothesis|involves|leads|reduces|shows|suggests|thesis)",
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

    word_pairs = [[Pd.sep_in_txt.value.format("we"), Pd.sep_in_txt.value.format("i")]]
    return consistency_check(text, word_pairs, err, msg, ignore_case=True)


# TODO: skipped in TNT:
#       - L812 this vs those
