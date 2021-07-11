"""Tests for jargon.misc check."""

from proselint.checks.jargon import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for jargon.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for jargon.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""I agree it's in the affirmative.""")
