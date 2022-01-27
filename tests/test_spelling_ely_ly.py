"""Tests for spelling.ely_ly check."""

from proselint.checks.spelling import ely_ly as chk

from .check import Check


class TestCheck(Check):
    """The test class for spelling.ely_ly."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for spelling.ely_ly."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""She was completly unprepared.""")
