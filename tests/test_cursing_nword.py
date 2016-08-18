"""Tests for cursing.nword check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.cursing import nword as chk


class TestCheck(Check):
    """The test class for cursing.nword."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for cursing.nword."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The n-word.""")
