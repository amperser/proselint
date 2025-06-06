"""Tests for industrial_language.jargon check."""

from proselint.checks.industrial_language import jargon as chk

from .check import Check


class TestCheck(Check):
    """The test class for industrial_language.jargon."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for industrial_language.jargon."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""I agree it's in the affirmative.""")
