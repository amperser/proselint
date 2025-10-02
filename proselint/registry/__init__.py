"""Check registry for proselint."""

from __future__ import annotations

from collections.abc import Mapping
from importlib import import_module
from itertools import chain
from typing import TYPE_CHECKING, ClassVar, TypeAlias

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


Config: TypeAlias = Mapping[str, "bool | Config"]


def _prune(checks: list[str], key: str) -> list[str]:
    return [k for k in checks if not (key.startswith(k + ".") or k == key)]


def _flatten_config(config: Config, prefix: str = "") -> dict[str, bool]:
    return dict(
        chain.from_iterable(
            _flatten_config(value, full_key).items()
            if isinstance(value, Mapping)
            else [(full_key, bool(value))]
            for key, value in config.items()
            for full_key in [f"{prefix}.{key}" if prefix else key]

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
        """Filter registered checks by config values based on their keys."""
        self.enabled_checks = dict(sorted(
            _flatten_config(enabled).items(), key=lambda x: x[0].count('.')
        ))

        enabled_checks: list[str] = []
        skipped_checks: list[str] = []

        for key, key_enabled in self.enabled_checks.items():
            if key_enabled:
                skipped_checks = _prune(skipped_checks, key)
                enabled_checks.append(key)
            else:
                enabled_checks = _prune(enabled_checks, key)
                skipped_checks.append(key)

        return [
            check
            for check in self.checks
            if not any(check.matches_partial(key) for key in skipped_checks)
            and any(
                check.path == key or check.matches_partial(key)
                for key in enabled_checks
            )
        ]
