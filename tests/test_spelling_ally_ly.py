"""Tests for spelling.ally_ly check."""

from proselint.checks.spelling import ally_ly as chk

from .check import Check


class TestCheck(Check):
    """The test class for spelling.ally_ly."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for spelling.ally_ly."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""She was accidently fired.""")
