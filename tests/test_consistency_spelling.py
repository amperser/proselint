"""Tests for consistency.spelling check."""

from proselint.checks.consistency import spelling as chk

from .check import Check


class TestCheck(Check):
    """The test class for consistency.spelling."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for consistency.spelling."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""The centre for the arts is the art centre.""")
        assert self.passes("""The center for the arts is the art center.""")
        assert not self.passes("""The centre of the arts is the art center.""")
