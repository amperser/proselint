"""Tests for needless_variants.misc check."""

from proselint.checks.needless_variants import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for needless_variants.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for needless_variants.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""It was an extensible telescope.""")
