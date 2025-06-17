"""Industrial language."""

from proselint.registry import build_modules_register

__register__ = build_modules_register(
    (
        ".airlinese",
        ".bureaucratese",
        ".chatspeak",
        ".commercialese",
        ".corporate_speak",
        ".jargon",
    ),
    "proselint.checks.industrial_language",
)
