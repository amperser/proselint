"""Tests for misc.professions check."""

from proselint.checks.misc import professions as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.professions."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.professions."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""I really need a shoe repair guy.""")
