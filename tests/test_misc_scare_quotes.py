"""Tests for misc.scare_quotes check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import scare_quotes as chk


class TestCheck(Check):
    """The test class for misc.scare_quotes."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.scare_quotes."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""What was the 'take-home message'?""")
