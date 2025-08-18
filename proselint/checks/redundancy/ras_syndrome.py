"""Redundant Acronym Syndrome (RAS) syndrome."""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
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
            "PDF format": "PDF",
            "PIN number": "PIN",
            "RAS syndrome": "RAS",
            "RIP in peace": "RIP",
            "please RSVP": "RSVP",
            "SALT talks": "SALT",
            "SAT test": "SAT",
            "UPC codes": "UPC",
        }
    ),
    path="redundancy.ras_syndrome",
    message="RAS syndrome. Use '{}' instead of '{}'.",
)

__register__ = (check,)
