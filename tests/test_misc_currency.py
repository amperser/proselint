"""Tests for misc.currency check."""

from proselint.checks.misc import currency as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.currency."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.currency."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""It cost $10 dollars.""")
