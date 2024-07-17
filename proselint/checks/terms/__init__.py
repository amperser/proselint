"""Terms."""

from proselint.checks.terms.animal_adjectives import (
    __register__ as register_animal_adjectives,
)
from proselint.checks.terms.denizen_labels import (
    __register__ as register_denizen_labels,
)
from proselint.checks.terms.eponymous_adjectives import (
    __register__ as register_eponymous_adjectives,
)
from proselint.checks.terms.venery import __register__ as register_venery

__register__ = (
    *register_animal_adjectives,
    *register_denizen_labels,
    *register_eponymous_adjectives,
    *register_venery,
)
