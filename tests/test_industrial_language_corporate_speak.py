"""Tests for industrial_language.corporate_speak check."""

from proselint.checks.industrial_language import corporate_speak as chk

from .check import Check


class TestCheck(Check):
    """The test class for industrial_language.corporate_speak."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for industrial_language.corporate_speak."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""We will discuss it later.""")
        assert not self.passes("""We will circle back around to it.""")
