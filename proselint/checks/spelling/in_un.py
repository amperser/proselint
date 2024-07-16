"""in- vs. un-."""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, PreferredFormsSimple

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


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
