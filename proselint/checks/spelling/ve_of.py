"""-ve vs. -of."""

from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "This could of been the third test.",
]


def check(text: str) -> list[ResultCheck]:
    """-ve vs. -of."""
    err = "spelling.ve_of"
    msg = "-ve vs. -of. '{}' is the preferred spelling."

    preferences = [
        ["could've", ["could of"]],
        ["should've", ["should of"]],
        ["would've", ["would of"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
