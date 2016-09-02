"""Tests for spelling.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.spelling import misc as chk


class TestCheck(Check):
    """The test class for spelling.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for spelling.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""I like this alot.""")
