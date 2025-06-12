"""Tests for mondegreens check."""

from proselint.checks import mondegreens as chk

from .check import Check


class TestCheck(Check):
    """The test class for mondegreens."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for mondegreens."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""... and laid him on the green.""")
        assert not self.passes("""..and Lady Mondegreen.""")
