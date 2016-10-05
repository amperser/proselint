"""Tests for misc.currency check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import currency as chk


class TestCheck(Check):
    """The test class for misc.currency."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.currency."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""It cost $10 dollars.""")
