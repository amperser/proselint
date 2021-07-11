"""Tests for misc.preferred_forms check."""

from proselint.checks.misc import preferred_forms as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.preferred_forms."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.preferred_forms."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""It was almost haloween.""")
