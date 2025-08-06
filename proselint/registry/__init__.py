"""Check registry for proselint."""

from __future__ import annotations

from importlib import import_module
from itertools import chain
from typing import TYPE_CHECKING, ClassVar, Optional

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
    enabled_checks: Optional[dict[str, bool]] = None
    _instance: Optional[CheckRegistry] = None

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
        """Filter registered checks by config values based on their keys."""
        self.enabled_checks = enabled

        enabled_checks: list[str] = []
        skipped_checks: list[str] = []
        for key, key_enabled in self.enabled_checks.items():
            (skipped_checks, enabled_checks)[key_enabled].append(key)

        return [
            check
            for check in self.checks
            if not any(check.matches_partial(key) for key in skipped_checks)
            and any(
                check.path == key or check.matches_partial(key)
                for key in enabled_checks
            )
        ]
