"""Tests for security.password check."""

from proselint.checks.security.password import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for security.password."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The password is 123456.")
    assert_fail(check, "My password is PASSWORD.")
