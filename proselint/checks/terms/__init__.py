"""Terms."""

from proselint.checks.terms import (
    animal_adjectives,
    denizen_labels,
    eponymous_adjectives,
    venery,
)

__register__ = (
    *animal_adjectives.__register__,
    *denizen_labels.__register__,
    *eponymous_adjectives.__register__,
    *venery.__register__,
)
