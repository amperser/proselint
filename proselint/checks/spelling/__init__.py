"""Spelling."""

from proselint.registry import build_modules_register

__register__ = build_modules_register(
    (
        ".able_atable",
        ".able_ible",
        ".ally_ly",
        ".ance_ence",
        ".athletes",
        ".consistency",
        ".ely_ly",
        ".em_im_en_in",
        ".er_or",
        ".in_un",
        ".misc",
        ".ve_of",
    ),
    "proselint.checks.spelling",
)
