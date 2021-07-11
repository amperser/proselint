"""Tests for redundancy.ras_syndrome check."""

from proselint.checks.redundancy import ras_syndrome as chk

from .check import Check


class TestCheck(Check):
    """The test class for redundancy.ras_syndrome."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for redundancy.ras_syndrome."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""Please enter your PIN number.""")
