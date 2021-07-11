"""Tests for malaproprisms.misc check."""

from proselint.checks.malapropisms import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for malaproprisms.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for malaproprisms.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""Found in the Infinitesimal Universe.""")
