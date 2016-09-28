"""Tests for misc.but check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import but as chk


class TestCheck(Check):
    """The test class for misc.but."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.but."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""But I never start with the word "but".""")
