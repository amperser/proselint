"""Tests for misc.punctuation check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import punctuation as chk


class TestCheck(Check):
    """The test class for misc.punctuation."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.punctuation."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""See Smith et. al.""")
