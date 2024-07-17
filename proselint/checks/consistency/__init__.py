"""Various consistency checks."""

from proselint.checks.consistency.spacing import (
    __register__ as register_spacing,
)
from proselint.checks.consistency.spelling import (
    __register__ as register_spelling,
)

__register__ = (*register_spacing, *register_spelling)
