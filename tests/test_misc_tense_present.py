"""Tests for misc.tense_present check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import tense_present as chk


class TestCheck(Check):
    """The test class for misc.tense_present."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.tense_present."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""I did it on accident honestly.""")
