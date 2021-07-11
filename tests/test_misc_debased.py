"""Tests for misc.debased check."""

from proselint.checks.misc import debased as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.debased."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.debased."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""This leaves much to be desired.""")
