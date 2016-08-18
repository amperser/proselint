"""Tests for cursing.filth check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.cursing import filth as chk


class TestCheck(Check):
    """The test class for cursing.filth."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for cursing.filth."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""Bad shit in this phrase.""")
