"""Tests for annotations.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.annotations import misc as chk


class TestCheck(Check):
    """The test class for annotations.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for annotations.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""Add it to the to do list.""")
        assert not self.passes("""Add it to the TODO list.""")
