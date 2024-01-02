"""Tests for cursing.nfl check."""

from proselint.checks.cursing.nfl import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for cursing.nfl."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "The QB is named ball licker.")
