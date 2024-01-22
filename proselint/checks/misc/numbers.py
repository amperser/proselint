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
    "It can vary by 9\xa0dB between locations.",
    "With a 1\xa0s duration.",
    "In a lake at a 5\xa0m distance.",
    "A Google Pixel\xa04, a OnePlus\xa08\xa0Pro, "
    "and a Samsung Galaxy Watch\xa04.",  # uses non-break space
    "Subjects distanced by 2\xa0m.",
    "There is a high noise amplitude below 1\xa0kHz,",
    "as observed variation of 9\xa0dB can be attributed",
    "because (1) smaller spacing and (2) something else",
    "In Fig. 3 we see the frequency response of the chirp.",
    "In Fig.\xa03 we see the frequency response of the chirp.",
    "1 INTRODUCTION",
    "2 Foreground: CHARACTERISTICS OF MOBILE DEVICES IN WATER",
    """3 BACKGROUND: CHARACTERISTICS OF MOBILE DEVICES IN WATER\n
this is a new sentence.""",
    "The preamble is composed of eight OFDM symbols from 1 to 4 kHz.",
]

examples_fail = [
    "remainder of only 7 symbol",
    "A Google Pixel 4, a OnePlus 8 Pro, and a Samsung Galaxy Watch 4.",  # regular space
]


def check_section(text: str) -> list[ResultCheck]:
    """can have false positives after abbreviations"""
    # src = https://www.sciencewrites.org/dos-and-donts
    err = "misc.numbers.newline"
    msg = (
        "It is untidy to open sentences with a number-digit, "
        "here '{}' -> spell it out or reword (num with unit or decimal places)."
    )
    regex = r"^\d+(?:\.\d+)?\s[^\v\r\n\.!\?]{7,}[\.!\?]"
    # - starts with newline
    # - look for number, can have punctuation
    # - must be also a sentence (7 chars & end with punctuation) in same line
    # - \v\r\n is a fix, as python does not seem to honor vertical whitespace \v
    return simple_existence_check(text, regex, err, msg)


def check_sentence(text: str) -> list[ResultCheck]:
    """can have false positives after abbreviations"""
    # src = https://www.sciencewrites.org/dos-and-donts
    err = "misc.numbers.sentence"
    msg = (
        "It is untidy to open sentences with a number-digit, "
        "here '{}' -> spell it out or reword (num with unit or decimal places)."
    )
    # regex = r"[\.!\?]\s[0-9]+[\.\s]"  # too many false positive
    regex = r"\b\w+[\.!\?] \d+(?:\.\d+)?\s[^\v\.!\?]{7,}[\.!\?]"
    # - start at end of last sentence
    # - look for number, can have punctuation
    # - must be also a sentence (7 chars & end with punctuation) in same line
    exceptions = (
        r"al\.",
        r"lat\.",
        r"vs\.",
        r"etc\.",
        r"Prof\.",
        r"Dr\.",
        r"[vV]ol\.",
        r"[fF]ig\.",
    )
    # TODO: sync the exceptions with punctuation/misc
    return simple_existence_check(text, regex, err, msg, exceptions=exceptions)


def check_single_digit(text: str) -> list[ResultCheck]:
    """can have false positives after abbreviations"""
    # src = https://www.sciencewrites.org/dos-and-donts
    err = "misc.numbers.single_digit"
    msg = (
        "It is bad style to use single digit numbers as numerals, "
        "here '{}' -> spell it out or "
        "use non-break space (U+00A0) if its part of a name."
    )
    regex = r"(?<![\.!\?]) [0-9][ \.!\?](?!to \d+)"
    # looks for single digit in separate in text (not at beginning of sentence)
    # but not part of "x to y"
    # TODO: reduce false positives from numbers without decimal point but with unit
    return simple_existence_check(text, regex, err, msg)
