"""Mixed metaphors."""

from proselint.registry.checks import Check, types

"""
source:     Sir Ernest Gowers
source_url: http://bit.ly/1CQPH61
"""
check_bottleneck = Check(
    check_type=types.Existence(
        items=(
            "biggest bottleneck",
            "big bottleneck",
            "large bottleneck",
            "largest bottleneck",
            "world-wide bottleneck",
            "huge bottleneck",
            "massive bottleneck",
        )
    ),
    path="mixed_metaphors.bottleneck",
    message="Mixed metaphor — bottles with big necks are easy to pass through.",
)

"""
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
"""
check_misc = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "cream rises to the crop": "cream rises to the top",
            "button your seatbelts": "fasten your seatbelts",
            "a minute to decompose": "a minute to decompress",
            "sharpest marble in the (shed|box)": "sharpest tool in the shed",
            "not rocket surgery": "not rocket science",
        }
    ),
    path="mixed_metaphors.misc",
    message="Mixed metaphor. Try '{}'.",
)

__register__ = (check_bottleneck, check_misc)
