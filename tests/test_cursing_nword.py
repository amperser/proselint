"""Tests for cursing.nword check."""

from proselint.checks.cursing.nword import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for cursing.nword."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "The n-word.")
