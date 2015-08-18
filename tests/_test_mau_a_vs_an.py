"""Unit tests for MAU101."""
from __future__ import absolute_import

from .check import Check
from proselint.checks.garner import a_vs_an as chk


class TestCheck(Check):

    """Test garner.a_vs_n."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test(self):
        """Ensure the test works correctly."""
        assert self.check("""An apple a day keeps the doctor away.""")
        assert self.check("""The Epicurean garden.""")
        assert not self.check("""A apple a day keeps the doctor away.""")
        assert not self.check("""An apple an day keeps the doctor away.""")
        assert not self.check("""An apple an\nday keeps the doctor away.""")
