"""-ally vs. -ly."""

from __future__ import annotations

from proselint.tools import ResultCheck, memoize, preferred_forms_check


@memoize
def check(text: str) -> list[ResultCheck]:
    """-ally vs. -ly."""
    err = "spelling.ally_ly"
    msg = "-ally vs. -ly. '{}' is the correct spelling."

    preferences = [
        ["academically", ["academicly"]],
        ["accidentally", ["accidently"]],
        ["automatically", ["automaticly"]],
        ["basically", ["basicly"]],
        ["dramatically", ["dramaticly"]],
        ["emotionally", ["emotionly"]],
        ["incidentally", ["incidently"]],
        ["optimistically", ["optimisticly"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
