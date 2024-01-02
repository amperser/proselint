"""Tests for misc.suddenly check."""

from proselint.checks.misc.suddenly import check

from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.suddenly."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "Suddenly, it all made sense.")
