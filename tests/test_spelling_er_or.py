"""Tests for spelling.er_or check."""

from proselint.checks.spelling import er_or as chk

from .check import Check


class TestCheck(Check):
    """The test class for spelling.er_or."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for spelling.er_or."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""She met with the invester.""")
