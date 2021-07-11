"""Tests for misc.not_guilty check."""

from proselint.checks.misc import not_guilty as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.not_guilty."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.not_guilty."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes(
            """She is not guilty beyond a reasonable doubt.""")
