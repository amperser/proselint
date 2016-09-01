"""Tests for weasel_words.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.weasel_words import misc as chk
from nose import SkipTest


class TestCheck(Check):
    """The test class for weasel_words.misc."""

    raise SkipTest

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for weasel_words.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        # FIXME add test when check is implemented
