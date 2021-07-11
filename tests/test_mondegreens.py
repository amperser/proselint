"""Tests for mondegreens.misc check."""

from proselint.checks.mondegreens import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for mondegreens.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for mondegreens.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""... and laid him on the green.""")
        assert not self.passes("""..and Lady Mondegreen.""")
