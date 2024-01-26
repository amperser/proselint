"""-ally vs. -ly."""

from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "She was accidently fired.",
]


def check(text: str) -> list[ResultCheck]:
    """-ally vs. -ly."""
    err = "spelling.ally_ly"
    msg = "-ally vs. -ly. '{}' is the correct spelling."

    items: dict[str, str] = {
        "academicly": "academically",
        "accidently": "accidentally",
        "automaticly": "automatically",
        "basicly": "basically",
        "dramaticly": "dramatically",
        "emotionly": "emotionally",
        "incidently": "incidentally",
        "optimisticly": "optimistically",
    }

    return preferred_forms_check_opti(text, items, err, msg)
