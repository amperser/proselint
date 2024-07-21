"""Scientific writing."""

from proselint.checks.scientific import misc, psychology

__register__ = (
    *misc.__register__,
    *psychology.__register__,
)
