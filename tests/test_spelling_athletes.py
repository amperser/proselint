"""Tests for spelling.athletes check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.spelling import athletes as chk


class TestCheck(Check):
    """The test class for spelling.athletes."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for spelling.athletes."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""One of the greats: Cal Ripkin.""")
