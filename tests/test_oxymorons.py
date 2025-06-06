"""Tests for oxymorons check."""

from proselint.checks import oxymorons as chk

from .check import Check


class TestCheck(Check):
    """The test class for oxymorons."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for oxymorons."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""He needed an exact estimate.""")
