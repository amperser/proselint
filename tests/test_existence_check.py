"""Test the existence_check function from the tools.py module."""
from __future__ import absolute_import

from .check import Check

from proselint.tools import existence_check as chk


class TestCheck(Check):
    """The test class for tools.existence_check."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def setUp(self):
        """setUp method creating some test fixtures."""
        self.l = ['abc']
        self.err = 'error message'
        self.msg = 'it exists'

    def test_smoke(self):
        """Basic smoke test to determine that existence_check is working."""
        assert chk(
            """abc is as easy as 123""", self.l, self.err, self.msg) != []
        assert chk(
            """easy breezy""", self.l, self.err, self.msg) == []
        assert self.err in chk(
            """abc is as easy as 123""", self.l, self.err, self.msg)[0]
        assert self.msg in chk(
            """abc is as easy as 123""", self.l, self.err, self.msg)[0]

    def test_multiple_matches(self):
        """Test that multiple matches are found correctly."""
        assert len(
            chk("""abc and abc are as easy as 123""",
                self.l, self.err, self.msg)) == 2
        assert len(
            chk("""ABC and abc are as easy as 123""",
                self.l, self.err, self.msg, ignore_case=True)) == 2
        assert chk(
            """abcabc are easy as 123""", self.l, self.err, self.msg) == []

    def test_string_types(self):
        """Test that the function works with different string types."""
        assert chk('abc is easy as 123', self.l, self.err, self.msg) != []
        assert chk("abc is easy as 123", self.l, self.err, self.msg) != []
        assert chk(u'abc is easy as 123', self.l, self.err, self.msg) != []
        assert chk(u"abc is easy as 123", self.l, self.err, self.msg) != []
