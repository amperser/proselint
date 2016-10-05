"""Tests for misc.metadiscourse check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import metadiscourse as chk


class TestCheck(Check):
    """The test class for misc.metadiscourse."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.metadiscourse."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""It's based on the rest of this article.""")
