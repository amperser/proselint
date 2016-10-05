"""Tests for misc.whence check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import whence as chk


class TestCheck(Check):
    """The test class for misc.whence."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.whence."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""Go back from whence you came!""")
