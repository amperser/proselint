"""-ance vs. -ence."""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "appearence": "appearance",
            "occurrance": "occurrence",
            "resistence": "resistance",
        }
    ),
    path="spelling.ance_ence",
    message="-ance vs. -ence. '{}' is the correct spelling.",
)

__register__ = (check,)
