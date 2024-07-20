"""
Scientific writing.

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

from proselint.checks import (
    CheckResult,
    CheckSpec,
    Consistency,
    Existence,
    ExistenceSimple,
    Pd,
    PreferredForms,
    PreferredFormsSimple,
)

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

# src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L325
check_num_unit = CheckSpec(
    # TODO: add more than the SI-Units
    # - start with a space and a number that may contain a decimal.point
    # - no space afterward, optional exponent, common units
    ExistenceSimple(
        r"\s\d*\.?\d+(?:k|M|G|T|E|m|u|µ|n|p|f)?"
        r"(?:s|m|g|A|K|mol|cd|Hz|dB|%|N|cal|C|F|V)+\b"
    ),
    "scientific.misc.num_unit",
    (
        "In scientific writing there is a non-breaking space "
        "(U+00A0, ~ in latex) between a number and its unit, here '{}'."
    ),
    ignore_case=False,
)

# src = https://www.sciencewrites.org/dos-and-donts
check_emotion = CheckSpec(
    Existence([
        "ridiculous",
        "unfortunately",
        "obvious",
        "obviously",
    ]),
    "scientific.misc.emotion",
    "Scientific writing should not use emotionally laden terms like '{}'.",
)

# src = https://www.sciencewrites.org/dos-and-donts
check_weasel = CheckSpec(
    Existence(["attempts"]),
    "scientific.misc.weasel",
    "Scientific writing should not build on uncertainty like '{}'.",
)

# src = https://www2.spsc.tugraz.at/www-archive/downloads/DoesandDonts%20in%20scientific%20writing%20reisenhofer%20tumfart.pdf
check_conversation = CheckSpec(
    Existence(["Well", "you see", "yes", "let's move on"]),
    "scientific.misc.conversation",
    "Scientific writing should not chatter or converse, like in '{}'.",
)

# src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L522
check_wrong = CheckSpec(
    Existence(["lowly doped", "low doped"]),
    "scientific.misc.wrong",
    "Avoid technically incorrect terms like '{}'.",
)

# src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L522
check_avoid_misc = CheckSpec(
    Existence(["becomes", "gets", "huge", "very"]),
    "scientific.misc.avoid",
    "Scientific writing should avoid terms like '{}'.",
)

# src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L522
check_preferred = CheckSpec(
    PreferredFormsSimple({
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
    }),
    "scientific.misc.preference",
    "In scientific writing some terms are avoided or incorrect. "
    "Consider using '{}' instead of '{}'.",
)

check_preferred_regex = CheckSpec(
    PreferredForms({
        r"solar cell(|s)": "photovoltaic",
        r"(is|are) increasing": "increases",
        r"(is|are) decreasing": "decreases",
        r"(p|n) dop(ing|ed)": "***(p|n)-dop(ing|ed)***",
        r"semi conductor(|s)": "semiconductor(s)",
        # TODO: active regex or no clean replacement
        # ["too ***", ["to strong", "to weak\w*", "to strong\w*"]],
        # TODO: except 'due to *'
    }),
    "scientific.misc.preference",
    "In scientific writing some terms are avoided or incorrect. "
    "Consider using '{}' instead of '{}'.",
)


def _check_this_vs_those(text: str, spec: CheckSpec) -> list[CheckResult]:
    """Check the usage of "this" and "those"."""
    # src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L812
    # TODO: magnet for false positives -> remove? seems niche
    exceptions = [
        "this results in",
        r"this \w+ss\b",
        r"this is\b",
        (
            r"this (agrees|allows|cancels|corresponds|enables|ensures|explains"
            r"|has|hypothesis|involves|indicates|leads|reduces|shows|suggests"
            r"|thesis)"
        ),
    ]
    expt_regex = "(" + "|".join(exceptions) + ")"
    results: list[CheckResult] = []
    for _m in re.finditer(
        r"\b(this +\w+s(\s\w+)?)\b", text, flags=re.IGNORECASE
    ):
        _res = _m.group(0).strip().lower()
        if any(re.finditer(expt_regex, _res)):
            continue
        results.append(
            CheckResult(
                start_pos=_m.start(),
                end_pos=_m.end(),
                check=spec.path,
                message=spec.msg.format(_res),
                replacements=None,
            )
        )
    return results


check_this_vs_those = CheckSpec(
    _check_this_vs_those,
    "scientific.misc.this_vs_those",
    "(Maybe) wrong plural for '{}' -> use 'those *'",
)

check_we_or_i = CheckSpec(
    Consistency([
        (
            Pd.words_in_txt.value.format("we"),
            Pd.words_in_txt.value.format("i"),
        )
    ]),
    "scientific.misc.we_or_i",
    "Decide if you alone ('{}') or a team ('{}') has written the report",
)

# TODO: skipped in TNT:
#       - L812 this vs those
#     - deg C or deg K is old, deg not used anymore

__register__ = (
    check_num_unit,
    check_emotion,
    check_weasel,
    check_conversation,
    check_wrong,
    check_avoid_misc,
    check_preferred,
    check_preferred_regex,
    check_this_vs_those,
    check_we_or_i,
)
