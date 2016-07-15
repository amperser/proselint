"""Test the consistency_check function from the tools.py module."""
from __future__ import absolute_import

from .check import Check

from proselint.tools import consistency_check as chk


class TestCheck(Check):
    """The test class for tools.consistency_check."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def setUp(self):
        """Create some test fixtures."""
        self.l = [['colour', 'color']]
        self.err = 'error message'
        self.msg = 'inconsistent form of {} vs {}'

    def test_smoke(self):
        """Basic smoke test for consistency_check."""
        assert chk(
            "Painting colour on color", self.l, self.err, self.msg) != []
        assert chk(
            "Painting colour on colour", self.l, self.err, self.msg) == []
        assert chk(
            "Painting color on color", self.l, self.err, self.msg) == []
