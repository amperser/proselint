"""Tests for oxymorons.misc check."""
from __future__ import absolute_import

from proselint.checks.oxymorons import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for oxymorons.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for oxymorons.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""He needed an exact estimate.""")
