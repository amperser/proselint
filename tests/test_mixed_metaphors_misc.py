"""Tests for mixed_metaphors.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.mixed_metaphors import misc as chk


class TestCheck(Check):
    """The test class for mixed_metaphors.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""Writing tests is not rocket surgery.""")
