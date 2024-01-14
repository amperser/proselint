"""Mixed metaphors."""

from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import existence_check
from proselint.checks import limit_results
from proselint.checks import preferred_forms_check


@limit_results(1)
def check_bottleneck(text: str) -> list[ResultCheck]:
    """Avoid mixing metaphors about bottles and their necks.

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


def check_misc(text: str) -> list[ResultCheck]:
    """Avoid mixing metaphors.

    source:     Garner's Modern American Usage
    source_url: http://bit.ly/1T4alrY
    """
    err = "mixed_metaphors.misc"
    msg = "Mixed metaphor. Try '{}'."

    preferences = [
        ["cream rises to the top", ["cream rises to the crop"]],
        ["fasten your seatbelts", ["button your seatbelts"]],
        ["a minute to decompress", ["a minute to decompose"]],
        ["sharpest tool in the shed", ["sharpest marble in the (shed|box)"]],
        ["not rocket science", ["not rocket surgery"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
