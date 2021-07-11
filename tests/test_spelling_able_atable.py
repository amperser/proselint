"""Tests for spelling.able_atable check."""

from proselint.checks.spelling import able_atable as chk

from .check import Check


class TestCheck(Check):
    """The test class for spelling.able_atable."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for spelling.able_atable."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""There was a demonstratable difference.""")
