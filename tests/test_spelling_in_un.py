"""Tests for spelling.in_un check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.spelling import in_un as chk


class TestCheck(Check):
    """The test class for spelling.in_un."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for spelling.in_un."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The plan was unfeasible.""")
