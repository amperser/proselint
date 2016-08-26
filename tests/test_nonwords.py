"""Tests for nonwords.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.nonwords import misc as chk


class TestCheck(Check):
    """The test class for nonwords.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for nonwords.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The test was good irregardless.""")
