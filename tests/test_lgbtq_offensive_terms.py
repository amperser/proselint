"""Tests for lgbtq.terms check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.lgbtq import offensive_terms as chk


class TestCheck(Check):
    """The test class for lgbtq.offensive_terms."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for lgbtq.offensive_terms."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""I once met a gay man.""")
        assert not self.passes("""I once met a fag.""")
