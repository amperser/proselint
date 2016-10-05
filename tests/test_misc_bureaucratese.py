"""Tests for misc.bureaucratese check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import bureaucratese as chk


class TestCheck(Check):
    """The test class for misc.bureaucratese."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.bureaucratese."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes(
            """I hope the report meets with your approval.""")
