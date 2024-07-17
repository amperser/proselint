"""Spelling."""

from proselint.checks.spelling.able_atable import (
    __register__ as register_able_atable,
)
from proselint.checks.spelling.able_ible import (
    __register__ as register_able_ible,
)
from proselint.checks.spelling.ally_ly import __register__ as register_ally_ly
from proselint.checks.spelling.ance_ence import (
    __register__ as register_ance_ence,
)
from proselint.checks.spelling.athletes import (
    __register__ as register_athletes,
)
from proselint.checks.spelling.ely_ly import __register__ as register_ely_ly
from proselint.checks.spelling.em_im_en_in import (
    __register__ as register_em_im_en_in,
)
from proselint.checks.spelling.er_or import __register__ as register_er_or
from proselint.checks.spelling.in_un import __register__ as register_in_un
from proselint.checks.spelling.misc import __register__ as register_misc
from proselint.checks.spelling.ve_of import __register__ as register_ve_of

__register__ = (
    *register_able_atable,
    *register_able_ible,
    *register_ally_ly,
    *register_ance_ence,
    *register_athletes,
    *register_ely_ly,
    *register_em_im_en_in,
    *register_er_or,
    *register_in_un,
    *register_misc,
    *register_ve_of,
)
