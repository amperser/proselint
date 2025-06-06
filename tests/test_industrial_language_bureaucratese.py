"""Tests for industrial_language.bureaucratese check."""

from proselint.checks.industrial_language import bureaucratese as chk

from .check import Check


class TestCheck(Check):
    """The test class for industrial_language.bureaucratese."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for industrial_language.bureaucratese."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes(
            """I hope the report meets with your approval.""")
