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

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "The preamble is composed of eight OFDM symbols from 1 to 4 kHz.",
    "It can vary by 9 dB between locations.",
    "With a 1 s duration.",
    "In a lake at a 5 m distance.",
    "A Google Pixel 4, a OnePlus 8 Pro, and a Samsung Galaxy Watch 4.",
    "Subjects distanced by 2 m.",
    "There is a high noise amplitude below 1 kHz,",
    "as observed variation of 9 dB can be attributed",
    "because (1) smaller spacing and (2) something else",
    "In Fig. 3 we see the frequency response of the chirp.",
    "1 INTRODUCTION",
    """2 BACKGROUND: CHARACTERISTICS OF MOBILE DEVICES IN WATER
this is a new sentence.""",
]

examples_fail = [
    "remainder of only 7 symbol",
]


def check_sentence(text: str) -> list[ResultCheck]:
    """can have false positives after abbreviations"""
    # src = https://www.sciencewrites.org/dos-and-donts
    err = "misc.numbers.sentence"
    msg = (
        "It is untidy to open sentences with a number-digit, "
        "here '{}' -> spell it out or reword if with unit or decimal places)."
    )
    regex = r"[\.!\?]\s[0-9]+[\.\s]"
    # will find numbers with or without a decimal point at the start of a new sentence
    return simple_existence_check(text, regex, err, msg)


def check_single_digit(text: str) -> list[ResultCheck]:
    """can have false positives after abbreviations"""
    # src = https://www.sciencewrites.org/dos-and-donts
    err = "misc.numbers.single_digit"
    msg = (
        "It is bad style to use single digit numbers as numerals, "
        "here '{}' -> spell it out if without unit."
    )
    regex = r"\s[0-9]\s"
    # TODO: reduce false positives from numbers without decimal point but with unit
    return simple_existence_check(text, regex, err, msg)
