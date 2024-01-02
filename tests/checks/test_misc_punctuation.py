"""Tests for misc.punctuation check."""

from proselint.checks.misc.punctuation import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.punctuation."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "See Smith et. al.")
