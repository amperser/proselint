"""Terms."""

from proselint.checks import CheckRegistry
from proselint.checks.terms.animal_adjectives import (
    register_with as register_animal_adjectives,
)
from proselint.checks.terms.denizen_labels import (
    register_with as register_denizen_labels,
)
from proselint.checks.terms.eponymous_adjectives import (
    register_with as register_eponymous_adjectives,
)
from proselint.checks.terms.venery import register_with as register_venery


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    register_animal_adjectives(registry)
    register_denizen_labels(registry)
    register_eponymous_adjectives(registry)
    register_venery(registry)
