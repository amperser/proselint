"""-ve vs. -of."""

from __future__ import annotations

from proselint.checks import CheckSpec, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "This could of been the third test.",
]

check = CheckSpec(
    PreferredFormsSimple({
        "could of": "could've",
        "should of": "should've",
        "would of": "would've",
    }),
    "spelling.ve_of",
    "-ve vs. -of. '{}' is the preferred spelling.",
)

__register__ = (check,)
