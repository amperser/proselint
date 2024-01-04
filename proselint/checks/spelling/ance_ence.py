"""-ance vs. -ence."""

from __future__ import annotations

from proselint.checks import ResultCheck, preferred_forms_check


def check(text: str) -> list[ResultCheck]:
    """-ance vs. -ence."""
    err = "spelling.ance_ence"
    msg = "-ance vs. -ence. '{}' is the correct spelling."

    preferences = [
        ["appearance", ["appearence"]],
        ["occurrence", ["occurrance"]],
        ["resistance", ["resistence"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
