"""Tests for misc.whence check."""

from proselint.checks.misc.whence import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.whence."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "Go back from whence you came!")
