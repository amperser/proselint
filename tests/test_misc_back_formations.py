"""Tests for misc.back_formations check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import back_formations as chk


class TestCheck(Check):
    """The test class for misc.back_formations."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.back_formations."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""It is an improprietous use.""")
