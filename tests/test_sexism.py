"""Tests for sexism.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.sexism import misc as chk


class TestCheck(Check):
    """The test class for sexism.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for sexism.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes(
            """The legal team had two lawyers and a lady lawyer.""")
