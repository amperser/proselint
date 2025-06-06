"""Tests for annotations check."""

from proselint.checks import annotations as chk

from .check import Check


class TestCheck(Check):
    """The test class for annotations."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for annotations."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""Add it to the to do list.""")
        assert not self.passes("""Add it to the TODO list.""")
