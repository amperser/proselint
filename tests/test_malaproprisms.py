"""Tests for malaproprisms.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.malapropisms import misc as chk


class TestCheck(Check):
    """The test class for malaproprisms.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for malaproprisms.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""Found in the Infinitesimal Universe.""")
