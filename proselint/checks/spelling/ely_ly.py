"""-ely vs. -ly."""

from proselint.tools import preferred_forms_check



def check(text):
    """-ely vs. -ly."""
    err = "spelling.ely_ly"
    msg = "-ely vs. -ly. '{}' is the correct spelling."

    preferences = [

        ["completely", ["completly"]],
        ["immediately", ["immediatly"]],
        ["unfortunately", ["unfortunatly"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
