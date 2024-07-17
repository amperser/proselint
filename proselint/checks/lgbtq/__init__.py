"""GLAAD."""

from proselint.checks.lgbtq.offensive_terms import (
    __register__ as register_offensive_terms,
)
from proselint.checks.lgbtq.terms import __register__ as register_terms

__register__ = (
    *register_offensive_terms,
    *register_terms,
)
