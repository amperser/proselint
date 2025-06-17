"""-ely vs. -ly."""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "completly": "completely",
            "immediatly": "immediately",
            "unfortunatly": "unfortunately",
        }
    ),
    path="spelling.ely_ly",
    message="-ely vs. -ly. '{}' is the correct spelling.",
)

__register__ = (check,)
