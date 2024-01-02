"""Tests for misc.latin check."""

from proselint.checks.misc.latin import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.latin."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "And ceteris paribus, it was good.")
