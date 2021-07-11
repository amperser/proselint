"""Test the consistency_check function from the tools.py module."""

from proselint.tools import consistency_check as chk

from .check import Check


class TestCheck(Check):
    """The test class for tools.consistency_check."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def setUp(self):
        """Create some test fixtures."""
        self.L = [['colour', 'color']]
        self.err = 'error message'
        self.msg = 'inconsistent form of {} vs {}'

    def test_smoke(self):
        """Basic smoke test for consistency_check."""
        assert chk(
            "Painting colour on color", self.L, self.err, self.msg) != []
        assert chk(
            "Painting colour on colour", self.L, self.err, self.msg) == []
        assert chk(
            "Painting color on color", self.L, self.err, self.msg) == []
