"""Weasel words."""

from proselint.checks.weasel_words.misc import __register__ as register_misc
from proselint.checks.weasel_words.very import __register__ as register_very

__register__ = (
    *register_misc,
    *register_very,
)
