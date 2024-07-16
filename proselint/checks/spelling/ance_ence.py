"""-ance vs. -ence."""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, PreferredFormsSimple

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


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
