"""Tests for misc.greylist check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import greylist as chk


class TestCheck(Check):
    """The test class for misc.greylist."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.greylist."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""She should utilize her knowledge.""")
