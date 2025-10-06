"""Test the registry module."""

from proselint.config import (
    _sort_by_specificity,  # pyright: ignore[reportPrivateUsage]
)
from proselint.registry import CheckRegistry


def test_specific_overrides_general() -> None:
    """Test that specific config keys override general ones."""
    checks = _sort_by_specificity(
        {
            "typography": True,
            "typography.symbols": False,
            "typography.symbols.curly_quotes": True,
            "typography.punctuation.hyperbole": False,
        }
    )

    registry = CheckRegistry()
    enabled = registry.get_all_enabled(checks)

    paths = {check.path for check in enabled}

    assert "typography.symbols.curly_quotes" in paths
    assert "typography.punctuation.hyperbole" not in paths

    assert all(
        path == "typography.symbols.curly_quotes"
        or not path.startswith("typography.symbols.")
        for path in paths
    )

    assert any(
        path.startswith("typography.")
        and not path.startswith("typography.symbols.")
        and path != "typography.punctuation.hyperbole"
        for path in paths
    )
