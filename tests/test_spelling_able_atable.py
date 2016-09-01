"""Tests for spelling.able_atable check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.spelling import able_atable as chk


class TestCheck(Check):
    """The test class for spelling.able_atable."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for spelling.able_atable."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""There was a demonstratable difference.""")
