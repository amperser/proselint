"""-ely vs. -ly."""

from __future__ import annotations

from proselint.checks import CheckSpec, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "She was completly unprepared.",
]

check = CheckSpec(
    PreferredFormsSimple({
        "completly": "completely",
        "immediatly": "immediately",
        "unfortunatly": "unfortunately",
    }),
    "spelling.ely_ly",
    "-ely vs. -ly. '{}' is the correct spelling.",
)

__register__ = (check,)
