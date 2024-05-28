"""Mixed metaphors."""

from __future__ import annotations

from proselint.checks import (
    CheckResult,
    existence_check,
    limit_results,
    preferred_forms_check_opti,
    preferred_forms_check_regex,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The project produced a huge bottleneck.",
    "Writing tests is not rocket surgery.",
]


@limit_results(1)
def check_bottleneck(text: str) -> list[CheckResult]:
    """
    Avoid mixing metaphors about bottles and their necks.

    source:     Sir Ernest Gowers
    source_url: http://bit.ly/1CQPH61
    """
    err = "mixed_metaphors.misc.bottleneck"
    msg = "Mixed metaphor — bottles with big necks are easy to pass through."
    items = [
        "biggest bottleneck",
        "big bottleneck",
        "large bottleneck",
        "largest bottleneck",
        "world-wide bottleneck",
        "huge bottleneck",
        "massive bottleneck",
    ]

    return existence_check(text, items, err, msg)


def check_misc(text: str) -> list[CheckResult]:
    """
    Avoid mixing metaphors.

    source:     Garner's Modern American Usage
    source_url: http://bit.ly/1T4alrY
    """
    err = "mixed_metaphors.misc"
    msg = "Mixed metaphor. Try '{}'."

    items: dict[str, str] = {
        "cream rises to the crop": "cream rises to the top",
        "button your seatbelts": "fasten your seatbelts",
        "a minute to decompose": "a minute to decompress",
        "not rocket surgery": "not rocket science",
    }
    ret1 = preferred_forms_check_opti(text, items, err, msg)

    items_regex: dict[str, str] = {
        r"sharpest marble in the (shed|box)": "sharpest tool in the shed",
    }
    ret2 = preferred_forms_check_regex(text, items_regex, err, msg)

    return ret1 + ret2
