"""Tests reverse existence for elementary and check."""

from proselint.checks.reverse_existence import elementary as chk

from .check import Check


class TestCheck(Check):
    """The test class for reverse_existence.elementary."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for reverse_existence.elementary."""
        assert self.passes("""A boy and his goat went to a farm.""")
        assert self.passes("""I am tired.""")
        assert self.passes("""Water make up your body.""")
        assert self.passes("""""")

        assert not self.passes(""" Cells make up your body.""")
        assert not self.passes("I love clowns.")
        assert not self.passes(""" I hate cells and clowns.""")
