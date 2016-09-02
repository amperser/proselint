"""Tests for weasel_words.very check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.weasel_words import very as chk


class TestCheck(Check):
    """The test class for weasel_words.very."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for weasel_words.very."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The book was very interesting.""")
