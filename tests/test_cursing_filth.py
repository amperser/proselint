"""Tests for cursing.filth check."""

from proselint.checks.cursing import filth as chk

from .check import Check


class TestCheck(Check):
    """The test class for cursing.filth."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for cursing.filth."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""Bad shit in this phrase.""")
