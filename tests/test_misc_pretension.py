"""Tests for misc.pretension check."""

from proselint.checks.misc.pretension import check

from .conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.pretension."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "We need to reconceptualize the project.")
