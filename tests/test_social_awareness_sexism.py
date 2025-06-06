"""Tests for social_awareness.sexism check."""

from proselint.checks.social_awareness import sexism as chk

from .check import Check


class TestCheck(Check):
    """The test class for social_awareness.sexism."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for social_awareness.sexism."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes(
            """The legal team had two lawyers and a lady lawyer.""")
