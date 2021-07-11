"""Tests for misc.bureaucratese check."""

from proselint.checks.misc import bureaucratese as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.bureaucratese."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.bureaucratese."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes(
            """I hope the report meets with your approval.""")
