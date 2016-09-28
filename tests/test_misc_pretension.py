"""Tests for misc.pretension check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import pretension as chk


class TestCheck(Check):
    """The test class for misc.pretension."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.pretension."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""We need to reconceptualize the project.""")
