"""Tests for cursing.filth check."""

from proselint.checks.cursing.filth import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for cursing.filth."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "Bad shit in this phrase.")
