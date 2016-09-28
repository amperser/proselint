"""Tests for misc.metaconcepts check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import metaconcepts as chk


class TestCheck(Check):
    """The test class for misc.metaconcepts."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.metaconcepts."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The QB is named ball licker.""")
