"""Tests for typography.diacritical_marks check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.typography import diacritical_marks as chk


class TestCheck(Check):
    """The test class for typography.diacritical_marks."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for typography.diacritical_marks."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""He saw the performance by Beyonce.""")
