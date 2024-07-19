"""Spelling."""

from proselint.checks.spelling import (
    able_atable,
    able_ible,
    ally_ly,
    ance_ence,
    athletes,
    ely_ly,
    em_im_en_in,
    er_or,
    in_un,
    misc,
    ve_of,
)

__register__ = (
    *able_atable.__register__,
    *able_ible.__register__,
    *ally_ly.__register__,
    *ance_ence.__register__,
    *athletes.__register__,
    *ely_ly.__register__,
    *em_im_en_in.__register__,
    *er_or.__register__,
    *in_un.__register__,
    *misc.__register__,
    *ve_of.__register__,
)
