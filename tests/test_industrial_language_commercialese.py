"""Tests for industrial_language.commercialese check."""

from proselint.checks.industrial_language import commercialese as chk

from .check import Check


class TestCheck(Check):
    """The test class for industrial_language.commercialese."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for industrial_language.commercialese."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""We regret to inform you of this.""")
