"""Tests for terms.eponymous_adjectives check."""

from proselint.checks.terms import eponymous_adjectives as chk

from .check import Check


class TestCheck(Check):
    """The test class for terms.eponymous_adjectives."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for terms.eponymous_adjectives."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The writing wasn't Shakespearian.""")
