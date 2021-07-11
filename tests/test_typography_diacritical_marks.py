"""Tests for typography.diacritical_marks check."""

from proselint.checks.typography import diacritical_marks as chk

from .check import Check


class TestCheck(Check):
    """The test class for typography.diacritical_marks."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for typography.diacritical_marks."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""He saw the performance by Beyonce.""")
