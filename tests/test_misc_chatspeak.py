"""Tests for misc.chatspeak check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import chatspeak as chk


class TestCheck(Check):
    """The test class for misc.chatspeak."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.chatspeak."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""BRB getting coffee.""")
