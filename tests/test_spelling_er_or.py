"""Tests for spelling.er_or check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.spelling import er_or as chk


class TestCheck(Check):
    """The test class for spelling.er_or."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for spelling.er_or."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""She met with the invester.""")
