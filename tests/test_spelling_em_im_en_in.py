"""Tests for spelling.em_im_en_in check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.spelling import em_im_en_in as chk


class TestCheck(Check):
    """The test class for spelling.em_im_en_in."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for spelling.em_im_en_in."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""We shall imbark on a voyage.""")
