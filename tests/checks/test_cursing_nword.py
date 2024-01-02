"""Tests for cursing.nword check."""

from proselint.checks.cursing.nword import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for cursing.nword."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The n-word.")
