"""Tests for misc.waxed check."""

from proselint.checks.misc.waxed import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.waxed."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "They really could wax poetically.")
