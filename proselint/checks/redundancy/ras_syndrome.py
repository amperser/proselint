"""Redundant Acronym Syndrome (RAS) syndrome."""

from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check


def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "garner.redundancy.ras"
    msg = "RAS syndrome. Use '{}' instead of '{}'."

    redundancies = [
        ["ABM", ["ABM missile"]],
        ["ACT", ["ACT test"]],
        ["ABMs", ["ABM missiles"]],
        ["ABS", ["ABS braking system"]],
        ["ATM", ["ATM machine"]],
        ["CD", ["CD disc"]],
        ["CPI", ["CPI Index"]],
        ["GPS", ["GPS system"]],
        ["GUI", ["GUI interface"]],
        ["HIV", ["HIV virus"]],
        ["ISBN", ["ISBN number"]],
        ["LCD", ["LCD display"]],
        ["PDF", ["PDF format"]],
        ["PIN", ["PIN number"]],
        ["RAS", ["RAS syndrome"]],
        ["RIP", ["RIP in peace"]],
        ["RSVP", ["please RSVP"]],
        ["SALT", ["SALT talks"]],
        ["SAT", ["SAT test"]],
        ["UPC", ["UPC codes"]],
    ]

    return preferred_forms_check(text, redundancies, err, msg)
