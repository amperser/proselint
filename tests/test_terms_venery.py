"""Tests for terms.venery check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.terms import venery as chk


class TestCheck(Check):
    """The test class for terms.venery."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for terms.venery."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""There was a group of alligators.""")
