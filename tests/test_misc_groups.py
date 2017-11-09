"""Tests for misc.groups check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import groups as chk


class TestCheck(Check):
    """The test class for misc.phrasal_adjectives."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.groups."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The group of geese flew away.""")
        assert not self.passes("""A bunch of geese flew away.""")
