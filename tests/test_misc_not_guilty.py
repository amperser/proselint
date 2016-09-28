"""Tests for misc.not_guilty check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import not_guilty as chk


class TestCheck(Check):
    """The test class for misc.not_guilty."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.not_guilty."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes(
            """She is not guilty beyond a reasonable doubt.""")
