"""Tests for misc.inferior_superior check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import inferior_superior as chk


class TestCheck(Check):
    """The test class for misc.inferior_superior."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.inferior_superior."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes(
            """It was more inferior than the alternative.""")
