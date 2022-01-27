"""-ve vs. -of."""

from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """-ve vs. -of."""
    err = "spelling.ve_of"
    msg = "-ve vs. -of. '{}' is the preferred spelling."

    preferences = [

        ["could've", ["could of"]],
        ["should've", ["should of"]],
        ["would've", ["would of"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
