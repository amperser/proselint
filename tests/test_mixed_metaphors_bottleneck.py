"""Tests for mixed_metaphors.bottleneck check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.mixed_metaphors import bottleneck as chk


class TestCheck(Check):
    """The test class for mixed_metaphors.bottleneck."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The project produced a huge bottleneck.""")
