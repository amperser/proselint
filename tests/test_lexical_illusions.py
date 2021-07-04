"""Tests for lexical_illusions.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.lexical_illusions import misc as chk


class TestCheck(Check):
    """The test class for lexical_illusions.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for lexical_illusions.misc."""
        assert self.passes("Smoke phrase with nothing flagged.")
        assert not self.passes("Paris in the the springtime.")
        assert self.passes("And he's gone, gone with the breeze")
        assert self.passes("You should know that that sentence wasn't wrong.")
        assert self.passes("She had had dessert on the balcony.")
        assert not self.passes("You should know that that that was wrong.")
