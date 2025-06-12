"""Tests for needless_variants check."""

from proselint.checks import needless_variants as chk

from .check import Check


class TestCheck(Check):
    """The test class for needless_variants."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for needless_variants."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""It was an extensible telescope.""")
