"""Tests for misc.punctuation check."""

from proselint.checks.misc import punctuation as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.punctuation."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.punctuation."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""See Smith et. al.""")
