"""Tests for misc.false_plurals check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import false_plurals as chk


class TestCheck(Check):
    """The test class for misc.false_plurals."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.false_plurals."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""There were several phenomenons.""")

    def test_smoke_kudos(self):
        """Basic smoke test for misc.false_plurals.kudos."""
        assert chk.check_kudos("""Smoke phrase with nothing flagged.""") == []
        assert chk.check_kudos("""I give you many kudos.""") != []
