"""Tests for ableism.terms check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.ableism import offensive_terms as chk


class TestCheck(Check):
    """The test class for ableism.offensive_terms."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for lgbtq.offensive_terms."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""The bulb's light was dim.""")
        assert not self.passes("""That's absolutely insane.""")
