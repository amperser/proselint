"""Tests for security.credit_card check."""

from proselint.checks.security.credit_card import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for security.credit_card.

    This makes use of a test MasterCard number.
    """
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "My credit card number is 5555555555554444.")
