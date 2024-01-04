"""Tests for security.credit_card check."""

from proselint.checks.security.credit_card import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for security.credit_card.

    This makes use of a test MasterCard number.
    """
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "My credit card number is 5555555555554444.")
