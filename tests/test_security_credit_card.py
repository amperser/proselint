"""Tests for security.credit_card check."""

from proselint.checks.security import credit_card as chk

from .check import Check


class TestCheck(Check):
    """The test class for security.credit_card."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for security.credit_card.

        This makes use of a test MasterCard number.
        """
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes(
            """My credit card number is 5555555555554444.""")
