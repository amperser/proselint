"""Tests for mondegreens.misc check."""

from proselint.checks.mondegreens.misc import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for mondegreens.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _pass(check, "... and laid him on the green.")
    assert _fail(check, "..and Lady Mondegreen.")
