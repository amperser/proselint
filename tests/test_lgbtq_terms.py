"""Tests for lgbtq.offensive_terms check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.lgbtq import terms as chk


class TestCheck(Check):
    """The test class for lgbtq.terms."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for lgbtq.terms."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""They were a gay couple.""")
        assert not self.passes("""He was a homosexual man.""")

    def test_homosexual_term(self):
        """Check that the term homosexual does not get caught."""
        assert self.passes("""Homosexual.""")

    def test_sexual_prefence(self):
        """Check that sexual preference is flagged."""
        assert not self.passes("""My sexual preference is for women.""")
