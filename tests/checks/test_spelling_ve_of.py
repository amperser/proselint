"""Tests for spelling.ve_of check."""

from proselint.checks.spelling.ve_of import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for spelling.ve_of."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "This could of been the third test.")
