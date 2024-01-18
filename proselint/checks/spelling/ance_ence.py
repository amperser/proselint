"""-ance vs. -ence."""

from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The resistence was futile.",
]


def check(text: str) -> list[ResultCheck]:
    """-ance vs. -ence."""
    err = "spelling.ance_ence"
    msg = "-ance vs. -ence. '{}' is the correct spelling."

    preferences = [
        ["appearance", ["appearence"]],
        ["occurrence", ["occurrance"]],
        ["resistance", ["resistence"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
