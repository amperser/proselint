"""Tests for misc.suddenly check."""

from proselint.checks.misc import suddenly as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.suddenly."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.suddenly."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""Suddenly, it all made sense.""")
