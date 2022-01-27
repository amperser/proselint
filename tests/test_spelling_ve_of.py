"""Tests for spelling.ve_of check."""

from proselint.checks.spelling import ve_of as chk

from .check import Check


class TestCheck(Check):
    """The test class for spelling.ve_of."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for spelling.ve_of."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""This could of been the third test.""")
