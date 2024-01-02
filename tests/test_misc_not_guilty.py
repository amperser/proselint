"""Tests for misc.not_guilty check."""

from proselint.checks.misc.not_guilty import check

from .conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.not_guilty."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "She is not guilty beyond a reasonable doubt.")
