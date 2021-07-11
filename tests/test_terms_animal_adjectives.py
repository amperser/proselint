"""Tests for terms.animal_adjectives check."""

from proselint.checks.terms import animal_adjectives as chk

from .check import Check


class TestCheck(Check):
    """The test class for terms.animal_adjectives."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for terms.animal_adjectives."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""It was some bird-like creature.""")
