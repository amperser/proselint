"""Tests for misc.currency check."""

from proselint.checks.misc.currency import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.currency."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "It cost $10 dollars.")
