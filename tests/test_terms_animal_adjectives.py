"""Tests for terms.animal_adjectives check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.terms import animal_adjectives as chk


class TestCheck(Check):
    """The test class for terms.animal_adjectives."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for terms.animal_adjectives."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""It was some bird-like creature.""")
