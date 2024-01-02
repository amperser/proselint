"""Tests for cursing.filth check."""

from proselint.checks.cursing.filth import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for cursing.filth."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "Bad shit in this phrase.")
