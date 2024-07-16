"""Mixed metaphors."""

from __future__ import annotations

from proselint.checks import (
    CheckRegistry,
    CheckSpec,
    Existence,
    PreferredForms,
    PreferredFormsSimple,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The project produced a huge bottleneck.",
    "Writing tests is not rocket surgery.",
]

# TODO: reimplement limit_results
"""
source:     Sir Ernest Gowers
source_url: http://bit.ly/1CQPH61
"""
check_bottleneck = CheckSpec(
    Existence([
        "biggest bottleneck",
        "big bottleneck",
        "large bottleneck",
        "largest bottleneck",
        "world-wide bottleneck",
        "huge bottleneck",
        "massive bottleneck",
    ]),
    "mixed_metaphors.misc.bottleneck",
    "Mixed metaphor — bottles with big necks are easy to pass through.",
)

misc_name = "mixed_metaphors.misc"
misc_msg = "Mixed metaphor. Try '{}'."
"""
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
"""
check_misc = CheckSpec(
    PreferredFormsSimple({
        "cream rises to the crop": "cream rises to the top",
        "button your seatbelts": "fasten your seatbelts",
        "a minute to decompose": "a minute to decompress",
        "not rocket surgery": "not rocket science",
    }),
    misc_name,
    misc_msg,
)

check_misc_2 = CheckSpec(
    PreferredForms({
        r"sharpest marble in the (shed|box)": "sharpest tool in the shed",
    }),
    misc_name,
    misc_msg,
)


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    registry.register_many((
        check_bottleneck,
        check_misc,
        check_misc_2,
    ))
