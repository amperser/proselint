"""Social awareness."""

from proselint.registry import build_modules_register

__register__ = build_modules_register(
    (".lgbtq", ".nword", ".sexism", ".speciesism"),
    "proselint.checks.social_awareness",
)
