"""Tests for social_awareness.nword check."""

from proselint.checks.social_awareness import nword as chk

from .check import Check


class TestCheck(Check):
    """The test class for social_awareness.nword."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for social_awareness.nword."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The n-word.""")
