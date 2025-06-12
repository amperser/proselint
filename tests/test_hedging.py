"""Tests for hedging check."""

from proselint.checks import hedging as chk

from .check import Check


class TestCheck(Check):
    """The test class for hedging."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for hedging."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""I would argue that this is a good test.""")
