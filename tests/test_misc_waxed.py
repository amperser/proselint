"""Tests for misc.waxed check."""

from proselint.checks.misc import waxed as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.waxed."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.waxed."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""They really could wax poetically.""")
