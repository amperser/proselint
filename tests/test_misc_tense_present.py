"""Tests for misc.tense_present check."""

from proselint.checks.misc import tense_present as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.tense_present."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.tense_present."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""I did it on accident honestly.""")
