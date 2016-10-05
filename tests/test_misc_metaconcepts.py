"""Tests for misc.metaconcepts check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import metaconcepts as chk


class TestCheck(Check):
    """The test class for misc.metaconcepts."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.metaconcepts."""
        pass
