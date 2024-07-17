"""-ance vs. -ence."""

from __future__ import annotations

from proselint.checks import CheckSpec, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The resistence was futile.",
]

check = CheckSpec(
    PreferredFormsSimple({
        "appearence": "appearance",
        "occurrance": "occurrence",
        "resistence": "resistance",
    }),
    "spelling.ance_ence",
    "-ance vs. -ence. '{}' is the correct spelling.",
)

__register__ = (check,)
