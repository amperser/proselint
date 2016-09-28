"""Tests for misc.waxed check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import waxed as chk


class TestCheck(Check):
    """The test class for misc.waxed."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.waxed."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""They really could wax poetically.""")
