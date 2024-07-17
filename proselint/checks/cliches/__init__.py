"""Avoid cliches."""

from proselint.checks.cliches.hell import __register__ as register_hell
from proselint.checks.cliches.misc import __register__ as register_misc

__register__ = (*register_hell, *register_misc)
