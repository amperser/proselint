"""Tests for misc.greylist check."""

from proselint.checks.misc.greylist import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.greylist."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "She should utilize her knowledge.")


def test_utilized():
    """Don't produce an error when 'use' is used correctly."""
    assert_pass(check, "I use a hammer to drive nails into wood.")
    assert_fail(check, "I utilize a hammer to drive nails into wood.")
