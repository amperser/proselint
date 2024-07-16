"""Spelling."""

from proselint.checks import CheckRegistry
from proselint.checks.spelling.able_atable import (
    register_with as register_able_atable,
)
from proselint.checks.spelling.able_ible import (
    register_with as register_able_ible,
)
from proselint.checks.spelling.ally_ly import register_with as register_ally_ly
from proselint.checks.spelling.ance_ence import (
    register_with as register_ance_ence,
)
from proselint.checks.spelling.athletes import (
    register_with as register_athletes,
)
from proselint.checks.spelling.ely_ly import register_with as register_ely_ly
from proselint.checks.spelling.em_im_en_in import (
    register_with as register_em_im_en_in,
)
from proselint.checks.spelling.er_or import register_with as register_er_or
from proselint.checks.spelling.in_un import register_with as register_in_un
from proselint.checks.spelling.misc import register_with as register_misc
from proselint.checks.spelling.ve_of import register_with as register_ve_of


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    register_able_atable(registry)
    register_able_ible(registry)
    register_ally_ly(registry)
    register_ance_ence(registry)
    register_athletes(registry)
    register_ely_ly(registry)
    register_em_im_en_in(registry)
    register_er_or(registry)
    register_in_un(registry)
    register_misc(registry)
    register_ve_of(registry)
