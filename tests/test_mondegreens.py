"""Tests for mondegreens.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.mondegreens import misc as chk


class TestCheck(Check):
    """The test class for mondegreens.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for mondegreens.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""... and laid him on the green.""")
        assert not self.passes("""..and Lady Mondegreen.""")
