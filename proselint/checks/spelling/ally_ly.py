"""-ally vs. -ly."""

from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
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
