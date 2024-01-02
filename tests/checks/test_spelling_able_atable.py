"""Tests for spelling.able_atable check."""

from proselint.checks.spelling.able_atable import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for spelling.able_atable."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "There was a demonstratable difference.")
