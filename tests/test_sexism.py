"""Tests for sexism.misc check."""

from proselint.checks.sexism import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for sexism.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for sexism.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes(
            """The legal team had two lawyers and a lady lawyer.""")
