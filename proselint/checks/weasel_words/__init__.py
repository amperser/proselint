"""Weasel words."""

from proselint.checks.weasel_words import misc, very

__register__ = (
    *misc.__register__,
    *very.__register__,
)
