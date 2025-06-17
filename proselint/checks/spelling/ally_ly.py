"""-ally vs. -ly."""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "academicly": "academically",
            "accidently": "accidentally",
            "automaticly": "automatically",
            "basicly": "basically",
            "dramaticly": "dramatically",
            "emotionly": "emotionally",
            "incidently": "incidentally",
            "optimisticly": "optimistically",
        }
    ),
    path="spelling.ally_ly",
    message="-ally vs. -ly. '{}' is the correct spelling.",
)

__register__ = (check,)
