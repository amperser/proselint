"""Tests for cursing.nfl check."""

from proselint.checks.cursing import nfl as chk

from .check import Check


class TestCheck(Check):
    """The test class for cursing.nfl."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for cursing.nfl."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The QB is named ball licker.""")
