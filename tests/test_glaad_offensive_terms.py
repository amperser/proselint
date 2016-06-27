"""Test GLAAD Guidelines."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.glaad import offensive_terms as chk


class TestCheck(Check):
    """The test class for glaad.offensive_terms."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for glaad.offensive_terms."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""I once met a gay man.""")
        assert not self.passes("""I once met a fag.""")
