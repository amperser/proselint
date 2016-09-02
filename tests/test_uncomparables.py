"""Tests for uncomparables.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.uncomparables import misc as chk


class TestCheck(Check):
    """The test class for uncomparables.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for uncomparables.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The item was more unique.""")
