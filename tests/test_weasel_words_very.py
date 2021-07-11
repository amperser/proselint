"""Tests for weasel_words.very check."""

from proselint.checks.weasel_words import very as chk

from .check import Check


class TestCheck(Check):
    """The test class for weasel_words.very."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for weasel_words.very."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The book was very interesting.""")
