"""-ance vs. -ence."""

from __future__ import annotations

from proselint.checks import CheckResult, preferred_forms_check_opti, registry

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The resistence was futile.",
]


def check(text: str) -> list[CheckResult]:
    """-ance vs. -ence."""
    err = "spelling.ance_ence"
    msg = "-ance vs. -ence. '{}' is the correct spelling."

    items: dict[str, str] = {
        "appearence": "appearance",
        "occurrance": "occurrence",
        "resistence": "resistance",
    }

    return preferred_forms_check_opti(text, items, err, msg)


registry.register("spelling.ance_ence", check)
