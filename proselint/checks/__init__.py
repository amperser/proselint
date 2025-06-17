"""All the checks are organized into modules and places here."""

from proselint.registry import build_modules_register

__register__ = build_modules_register(
    (
        ".annotations",
        ".archaism",
        ".cliches",
        ".dates_times",
        ".hedging",
        ".industrial_language",
        ".lexical_illusions",
        ".malapropisms",
        ".misc",
        ".mixed_metaphors",
        ".mondegreens",
        ".needless_variants",
        ".nonwords",
        ".oxymorons",
        ".psychology",
        ".redundancy",
        ".restricted",
        ".skunked_terms",
        ".social_awareness",
        ".spelling",
        ".terms",
        ".typography",
        ".uncomparables",
        ".weasel_words",
    ),
    "proselint.checks",
)
