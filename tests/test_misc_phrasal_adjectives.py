"""Tests for misc.phrasal_adjectives check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import phrasal_adjectives as chk


class TestCheck(Check):
    """The test class for misc.phrasal_adjectives."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.phrasal_adjectives."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The QB is named ball licker.""")
