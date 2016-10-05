"""Tests for misc.debased check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import debased as chk


class TestCheck(Check):
    """The test class for misc.debased."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.debased."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""This leaves much to be desired.""")
