"""GLAAD."""

from proselint.checks.lgbtq import offensive_terms, terms

__register__ = (
    *offensive_terms.__register__,
    *terms.__register__,
)
