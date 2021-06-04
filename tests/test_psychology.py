"""Tests for psychology.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.psychology import lie_detector as chk


class TestCheck(Check):
    """The test class for psychology.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke_lie_detector_test(self):
        """Basic smoke test for psychology.misc.check_lie_detector_test."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The defendant took a lie detector test.""")
