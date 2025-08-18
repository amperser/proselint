"""Terms."""

from proselint.registry import build_modules_register

__register__ = build_modules_register(
    (
        ".animal_adjectives",
        ".denizen_labels",
        ".eponymous_adjectives",
        ".venery",
    ),
    "proselint.checks.terms",
)
