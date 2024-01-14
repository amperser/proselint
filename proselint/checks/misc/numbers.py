"""numbers at the beginning of a sentence and also number 1-9 should be spelled out

---
layout:     post
source:
source_url: https://www.sciencewrites.org/dos-and-donts
title:      number_spell
date:       2024-01-14
categories: writing
---


"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import simple_existence_check

# TODO: test the checks below


def check_sentence(text: str) -> list[ResultCheck]:
    """can have false positives after abbreviations"""
    # src = https://www.sciencewrites.org/dos-and-donts
    err = "misc.numbers.sentence"
    msg = "It is untidy to open sentences with a number-digit like '{}' -> spell it out or reword if with unit or decimal places)."
    regex = r"[\.!\?]\s[0-9]+[\.\s]"
    # will find numbers with or without a decimal point at the start of a new sentence
    return simple_existence_check(text, regex, err, msg)


def check_single_digit(text: str) -> list[ResultCheck]:
    """can have false positives after abbreviations"""
    # src = https://www.sciencewrites.org/dos-and-donts
    err = "misc.numbers.single_digit"
    msg = "It is bad style to use single digit numbers as numerals like '{}' -> spell it out if without unit."
    regex = r"\s[0-9]\s"
    # TODO: reduce false positives from numbers without decimal point but with unit
    return simple_existence_check(text, regex, err, msg)