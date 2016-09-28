"""Tests for misc.latin check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import latin as chk


class TestCheck(Check):
    """The test class for misc.latin."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.latin."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""And ceteris paribus, it was good.""")
