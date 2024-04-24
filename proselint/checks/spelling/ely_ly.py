"""-ely vs. -ly."""

from __future__ import annotations

from proselint.checks import CheckResult, preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "She was completly unprepared.",
]


def check(text: str) -> list[CheckResult]:
    """-ely vs. -ly."""
    err = "spelling.ely_ly"
    msg = "-ely vs. -ly. '{}' is the correct spelling."

    items: dict[str, str] = {
        "completly": "completely",
        "immediatly": "immediately",
        "unfortunatly": "unfortunately",
    }

    return preferred_forms_check_opti(text, items, err, msg)
