"""Tests for weasel_words.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.weasel_words import misc as chk


class TestCheck(Check):
    """The test class for weasel_words.misc."""
    __test__ = False

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for weasel_words.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        # TODO: add test when check is implemented
