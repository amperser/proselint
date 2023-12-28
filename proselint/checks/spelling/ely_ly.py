"""-ely vs. -ly."""

from __future__ import annotations

from proselint.tools import ResultCheck, memoize, preferred_forms_check


@memoize
def check(text: str) -> list[ResultCheck]:
    """-ely vs. -ly."""
    err = "spelling.ely_ly"
    msg = "-ely vs. -ly. '{}' is the correct spelling."

    preferences = [

        ["completely", ["completly"]],
        ["immediately", ["immediatly"]],
        ["unfortunately", ["unfortunatly"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
