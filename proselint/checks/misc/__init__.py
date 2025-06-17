"""Miscellaneous advice not otherwise categorized."""

from proselint.registry import build_modules_register

__register__ = build_modules_register(
    (
        ".apologizing",
        ".back_formations",
        ".but",
        ".capitalization",
        ".composition",
        ".currency",
        ".debased",
        ".false_plurals",
        ".greylist",
        ".illogic",
        ".inferior_superior",
        ".institution_name",
        ".latin",
        ".many_a",
        ".metadiscourse",
        ".narcissism",
        ".not_guilty",
        ".phrasal_adjectives",
        ".preferred_forms",
        ".pretension",
        ".professions",
        ".scare_quotes",
        ".suddenly",
        ".tense_present",
        ".waxed",
        ".whence",
    ),
    "proselint.checks.misc",
)
