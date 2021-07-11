"""Tests for misc.scare_quotes check."""

from proselint.checks.misc import scare_quotes as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.scare_quotes."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.scare_quotes."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""What was the 'take-home message'?""")
