"""Redundant Acronym Syndrome (RAS) syndrome."""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "Please enter your PIN number.",
]

check = CheckSpec(
    PreferredFormsSimple({
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
    }),
    "redundancy.ras_syndrome.garner",
    "RAS syndrome. Use '{}' instead of '{}'.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
