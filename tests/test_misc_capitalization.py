"""Tests for misc.capitalization check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import capitalization as chk


class TestCheck(Check):
    """The test class for misc.capitalization."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.capitalization."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The QB is named ball licker.""")
