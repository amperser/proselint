"""Tests for terms.denizen_labels check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.terms import denizen_labels as chk


class TestCheck(Check):
    """The test class for terms.denizen_labels."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for terms.denizen_labels."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""He was definitely a Hong Kongite.""")
