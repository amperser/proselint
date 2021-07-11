"""Tests for hedging.misc check."""

from proselint.checks.hedging import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for hedging.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for hedging.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""I would argue that this is a good test.""")
