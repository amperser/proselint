"""Tests for misc.many_a check."""

from proselint.checks.misc import many_a as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.many_a."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.many_a."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes(
            """There were many a day I thought about it.""")
