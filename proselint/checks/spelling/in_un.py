"""in- vs. un-."""

from __future__ import annotations

from ...lint_cache import memoize
from ...lint_checks import ResultCheck, preferred_forms_check


@memoize
def check(text: str) -> list[ResultCheck]:
    """in- vs un-."""
    err = "spelling.in_un"
    msg = "in- vs. un-. '{}' is the preferred spelling."

    preferences = [
        ["inadvisable", ["unadvisable"]],
        ["inalienable", ["unalienable"]],
        ["inexpressive", ["unexpressive"]],
        ["infeasible", ["unfeasible"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
