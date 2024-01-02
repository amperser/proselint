"""Tests for misc.but check."""

from proselint.checks.misc.but import check

from .check import Check
from .conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for misc.but."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, """But I never start with the word "but".""")
    assert _pass(check,
        """I never start with the word "but", but might use it after a linebreak.""",
    )
