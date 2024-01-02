"""Tests for misc.preferred_forms check."""

from proselint.checks.misc.preferred_forms import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.preferred_forms."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "It was almost haloween.")
