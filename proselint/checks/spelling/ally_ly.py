"""-ally vs. -ly."""

from __future__ import annotations

from proselint.checks import CheckSpec, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "She was accidently fired.",
]

check = CheckSpec(
    PreferredFormsSimple({
        "academicly": "academically",
        "accidently": "accidentally",
        "automaticly": "automatically",
        "basicly": "basically",
        "dramaticly": "dramatically",
        "emotionly": "emotionally",
        "incidently": "incidentally",
        "optimisticly": "optimistically",
    }),
    "spelling.ally_ly",
    "-ally vs. -ly. '{}' is the correct spelling.",
)

__register__ = (check,)
