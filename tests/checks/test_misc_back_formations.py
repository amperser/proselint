"""Tests for misc.back_formations check."""

from proselint.checks.misc.back_formations import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.back_formations."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "It is an improprietous use.")
