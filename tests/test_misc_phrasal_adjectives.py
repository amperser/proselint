"""Tests for misc.phrasal_adjectives check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import phrasal_adjectives as chk


class TestCheck(Check):
    """The test class for misc.phrasal_adjectives."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.phrasal_adjectives."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""There were across the board discounts.""")

    def test_smoke_ly(self):
        """Basic smoke test for misc.phrasal_adjectives.check_ly."""
        assert chk.check_ly("""Smoke phrase with nothing flagged.""") == []
        assert chk.check_ly("""He ran swiftly-fast.""")
        assert chk.check_ly("""The not-so-hotly-contested
                             result was fine.""") == []

    def test_ly_position(self):
        """Tests the start and ending position of check_ly"""
        error = chk.check_ly("""He ran swiftly-fast""")[0]
        assert error[0] == 6 and error[1] == 14

    def test_ly_multiple_dashes(self):
        """Tests that multiple dashes are not considered regular hyphens"""
        assert chk.check_ly("""This is handled internally---at least""") == []
