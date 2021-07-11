"""Tests for corporate_speak.misc check."""

from proselint.checks.corporate_speak import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for corporate_speak.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for corporate_speak.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""We will discuss it later.""")
        assert not self.passes("""We will circle back around to it.""")
