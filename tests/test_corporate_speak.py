"""Tests for corporate_speak.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.corporate_speak import misc as chk


class TestCheck(Check):
    """The test class for corporate_speak.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for corporate_speak.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""We will discuss it later.""")
        assert not self.passes("""We will circle back around to it.""")
