"""Tests for consistency.spacing check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.consistency import spacing as chk


class TestCheck(Check):
    """The test class for consistency.spacing."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for consistency.spacing."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes(
            """This is good. Only one space each time. Every time.""")
        assert not self.passes("""This is bad.  Not consistent. At all.""")
