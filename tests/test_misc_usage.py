"""Tests for misc.usage check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import usage as chk


class TestCheck(Check):
    """The test class for misc.usage."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.usage."""
        pass
