"""Tests for ableism.offensive_terms check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.ableism import terms as chk


class TestCheck(Check):
    """The test class for ableism.terms."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for ableism.terms."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""She's hard of hearing.""")
        assert not self.passes("""It's a madhouse in there.""")
