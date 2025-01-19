"""in- vs. un-."""

from __future__ import annotations

from proselint.checks import CheckSpec, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The plan was unfeasible.",
]


check = CheckSpec(
    PreferredFormsSimple({
        "unadvisable": "inadvisable",
        "unalienable": "inalienable",
        "unexpressive": "inexpressive",
        "unfeasible": "infeasible",
    }),
    "spelling.in_un",
    "in- vs. un-. '{}' is the preferred spelling.",
)

__register__ = (check,)
