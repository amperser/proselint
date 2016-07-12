"""Test the tools module."""

from __future__ import absolute_import

from .check import Check

from proselint.tools import lint as lint


class TestLint(Check):
    """The test class for tools.lint."""

    __test__ = True

    def setUp(self):
        """setUp method creating text fixtures."""
        self.text = """But this is a very bad sentence.
This is also a no-good sentence.

"""
        self.text_with_no_newline = """A very bad sentence."""

    def extract_line_col(self, error):
        """Extract the line and column number from an error tuple."""
        _, _, line, column, _, _, _, _, _ = error
        return line, column

    def test_errors_sorted(self):
        """Test that errors are sorted by line and column number."""
        lines_and_cols = [self.extract_line_col(e) for e in lint(self.text)]
        assert sorted(lines_and_cols) == lines_and_cols

    def test_on_no_newlines(self):
        """Test that lint works on text without a terminal newline."""
        assert len(lint(self.text_with_no_newline)) == 1
