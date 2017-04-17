"""Tests for airlinese.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.airlinese import misc as chk


class TestCheck(Check):
    """The test class for airlinese.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for airlinese.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""I got off the plane.""")
        assert not self.passes("""I deplaned.""")
