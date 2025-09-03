"""Redundant Acronym Syndrome (RAS) syndrome."""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "abm missile": "ABM",
            "act test": "ACT",
            "abm missiles": "ABMs",
            "abs braking system": "ABS",
            "atm machine": "ATM",
            "cd disc": "CD",
            "cpi Index": "CPI",
            "gps system": "GPS",
            "gui interface": "GUI",
            "hiv virus": "HIV",
            "isbn number": "ISBN",
            "lcd display": "LCD",
            "pdf format": "PDF",
            "pin number": "PIN",
            "ras syndrome": "RAS",
            "rip in peace": "RIP",
            "please RSVP": "RSVP",
            "salT talks": "SALT",
            "sat test": "SAT",
            "upc codes": "UPC",
        }
    ),
    path="redundancy.ras_syndrome",
    message="RAS syndrome. Use '{}' instead of '{}'.",
)

__register__ = (check,)
