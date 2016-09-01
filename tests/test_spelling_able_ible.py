"""Tests for spelling.able_ible check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.spelling import able_ible as chk


class TestCheck(Check):
    """The test class for spelling.able_ible."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for spelling.able_ible."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""It was a sensable decision.""")
