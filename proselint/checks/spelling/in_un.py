"""in- vs. un-."""

from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The plan was unfeasible.",
]


def check(text: str) -> list[ResultCheck]:
    """in- vs un-."""
    err = "spelling.in_un"
    msg = "in- vs. un-. '{}' is the preferred spelling."

    items: dict[str, str] = {
        "unadvisable": "inadvisable",
        "unalienable": "inalienable",
        "unexpressive": "inexpressive",
        "unfeasible": "infeasible",
    }

    return preferred_forms_check_opti(text, items, err, msg)
