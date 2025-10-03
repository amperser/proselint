"""Check registry for proselint."""

from __future__ import annotations

from importlib import import_module
from itertools import chain
from typing import TYPE_CHECKING, ClassVar

from proselint.config import DEFAULT

if TYPE_CHECKING:
    from proselint.registry.checks import Check


def build_modules_register(
    modules: tuple[str, ...], package: str
) -> tuple[Check, ...]:
    """Build a register tuple over `modules`."""
    return tuple(
        chain.from_iterable(
            import_module(module, package).__register__  # pyright: ignore[reportAny]
            for module in modules
        )
    )


class CheckRegistry:
    """A global registry for lint checks."""

    _checks: ClassVar[list[Check]] = []
    enabled_checks: dict[str, bool] | None = None
    _instance: CheckRegistry | None = None

    def __new__(cls) -> CheckRegistry:  # noqa: PYI034
        """Create a singleton registry."""
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def register(self, check: Check) -> None:
        """Register one check."""
        self._checks.append(check)

    def register_many(self, checks: tuple[Check, ...]) -> None:
        """Register multiple checks."""
        self._checks.extend(checks)

    @property
    def checks(self) -> list[Check]:
        """All registered checks."""
        return self._checks

    def get_all_enabled(
        self, enabled: dict[str, bool] = DEFAULT["checks"]
    ) -> list[Check]:
        """
        Filter registered checks by config values based on their keys.

        This assumes that keys are not nested, and sorted in descending order
        of depth (specificity). For example, all keys should look like
        `a.b.c`, and `a.b.c` should come before `a.b`.
        """
        self.enabled_checks = enabled

        return [
            check
            for check in self.checks
            if next(
                (
                    value
                    for prefix, value in self.enabled_checks.items()
                    if check.matches_partial(prefix)
                ),
                False,
            )
        ]
