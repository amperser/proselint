"""Redundant Acronym Syndrome (RAS) syndrome."""

from __future__ import annotations

from proselint.checks import CheckResult, preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "Please enter your PIN number.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "redundancy.ras.garner"
    msg = "RAS syndrome. Use '{}' instead of '{}'."

    items: dict[str, str] = {
        "ABM missile": "ABM",
        "ACT test": "ACT",
        "ABM missiles": "ABMs",
        "ABS braking system": "ABS",
        "ATM machine": "ATM",
        "CD disc": "CD",
        "CPI Index": "CPI",
        "GPS system": "GPS",
        "GUI interface": "GUI",
        "HIV virus": "HIV",
        "ISBN number": "ISBN",
        "LCD display": "LCD",
        "LED diode": "LED",
        "PDF format": "PDF",
        "PIN number": "PIN",
        "RAS syndrome": "RAS",
        "RIP in peace": "RIP",
        "please RSVP": "RSVP",
        "SALT talks": "SALT",
        "SAT test": "SAT",
        "UPC codes": "UPC",
    }

    return preferred_forms_check_opti(text, items, err, msg)
