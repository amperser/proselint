"""Tests for cursing.nfl check."""

from proselint.checks.cursing.nfl import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for cursing.nfl."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The QB is named ball licker.")
