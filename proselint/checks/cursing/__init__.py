"""Cursing."""

from proselint.checks.cursing.filth import __register__ as register_filth
from proselint.checks.cursing.nfl import __register__ as register_nfl
from proselint.checks.cursing.nword import __register__ as register_nword

__register__ = (
    *register_filth,
    *register_nfl,
    *register_nword,
)
