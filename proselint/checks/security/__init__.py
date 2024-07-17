"""Security."""

from proselint.checks.security.credit_card import (
    __register__ as register_credit_card,
)
from proselint.checks.security.password import (
    __register__ as register_password,
)

__register__ = (
    *register_credit_card,
    *register_password,
)
