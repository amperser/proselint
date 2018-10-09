"""Tests for hedges.just_say_no check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.hedges import just_say_no as chk


class TestCheck(Check):
    """The test class for hedges.just_say_no."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for hedges.just_say_no."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""I want to sleep, perchance to dream.""")
