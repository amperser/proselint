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

def check_emotion(text: str) -> list[ResultCheck]:
    """avoid the following words"""
    # src = https://www.sciencewrites.org/dos-and-donts
    err = "scientific.misc.emotion"
    msg = "Scientific writing should not contain emotionally laden terms like '{}'"
    items = ["ridiculous", "unfortunately"]
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

def check_preferred(text: str) -> list[ResultCheck]:
    # src = https://www.sciencewrites.org/dos-and-donts
    err = "scientific.misc.preference"
    msg = "In scientific writing some terms are less preferred like '{}' - use '{}' instead"
    items = [
        ["not significant", ["insignificant"]],
        ["although", ["though"]],
        ["they are", ["they're"]],
        ["is not", ["isn't"]],
        ["cannot", ["can't"]],
    ]
    return existence_check(text, items, err, msg)