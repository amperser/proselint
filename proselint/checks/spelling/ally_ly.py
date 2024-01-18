"""-ally vs. -ly."""

from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check


examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
"She was accidently fired.",
]

def check(text: str) -> list[ResultCheck]:
    """-ally vs. -ly."""
    err = "spelling.ally_ly"
    msg = "-ally vs. -ly. '{}' is the correct spelling."

    preferences = [
        ["academically", ["academicly"]],
        ["accidentally", ["accidently"]],
        ["automatically", ["automaticly"]],
        ["basically", ["basicly"]],
        ["dramatically", ["dramaticly"]],
        ["emotionally", ["emotionly"]],
        ["incidentally", ["incidently"]],
        ["optimistically", ["optimisticly"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
