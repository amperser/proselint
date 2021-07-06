"""Tests for misc.commercialese check."""
from __future__ import absolute_import

from proselint.checks.misc import commercialese as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.commercialese."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.commercialese."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""We regret to inform you of this.""")
