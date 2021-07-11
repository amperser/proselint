"""Tests for archaism.misc check."""

from proselint.checks.archaism import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for archaism.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for archaism.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""I want to sleep, and maybe dream.""")
        assert not self.passes("""I want to sleep, perchance to dream.""")
