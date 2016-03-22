"""Test Butterick's symbols."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.typography import symbols as chk


class TestCheck(Check):
    """The test class for typography.symbols."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_ellipsis(self):
        """Find ... in a string."""
        assert chk.check_ellipsis("""The long and winding road...""")

    def test_copyright(self):
        """Find a (c) or (C) in a string."""
        assert chk.check_copyright_symbol("""Show me the money! (C)""")
        assert chk.check_copyright_symbol("""Show me the money! (c)""")

    def test_trademark(self):
        """Find a (TM) or (tm) in a string."""
        assert chk.check_trademark_symbol("""The Fresh Maker (TM)""")
        assert chk.check_trademark_symbol("""The Fresh Maker (tm)""")

    def test_registered_trademark(self):
        """Find a (r) or (R) in a string."""
        assert chk.check_registered_trademark_symbol("""Just Do It (R)""")
        assert chk.check_registered_trademark_symbol("""Just Do It (r)""")

    def test_sentence_spacing(self):
        """Find a sentence followed by three or more spaces."""
        assert chk.check_sentence_spacing(
            """This is a sentence.   This is another.""")

    def test_multiplication(self):
        """Find an x between two digits."""
        assert chk.check_multiplication_symbol(
            """It is obvious that 2 x 2 = 4.""")

    def test_curly_quotes(self):  # FIXME
        """Find "" quotes in a string."""
        pass
