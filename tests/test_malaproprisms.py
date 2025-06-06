"""Tests for malaproprisms check."""

from proselint.checks import malapropisms as chk

from .check import Check


class TestCheck(Check):
    """The test class for malaproprisms."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for malaproprisms."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""Found in the Infinitesimal Universe.""")
