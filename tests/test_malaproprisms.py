"""Tests for malaproprisms.misc check."""

from proselint.checks.malapropisms.misc import check

from .conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for malaproprisms.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "Found in the Infinitesimal Universe.")
