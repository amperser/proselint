"""Tests for misc.apologizing check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import apologizing as chk


class TestCheck(Check):
    """The test class for misc.apologizing."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.apologizing."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""More research is needed.""")
