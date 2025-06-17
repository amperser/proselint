"""-ve vs. -of."""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "could of": "could've",
            "should of": "should've",
            "would of": "would've",
        }
    ),
    path="spelling.ve_of",
    message="-ve vs. -of. '{}' is the preferred spelling.",
)

__register__ = (check,)
