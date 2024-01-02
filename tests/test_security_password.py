"""Tests for security.password check."""

from proselint.checks.security.password import check
from tests.conftest import _fail, _pass


def test_security_password():
    """Basic smoke test for security.password."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "The password is 123456.")
    assert _fail(check, "My password is PASSWORD.")
