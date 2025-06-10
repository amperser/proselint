"""Test the tools module."""


from proselint.config import default
from proselint.tools import lint as proselint, load_options

from .check import Check


def lint(text):
    return proselint(text, config=load_options(conf_default=default))


class TestLint(Check):
    """The test class for tools.lint."""

    __test__ = True

    def setUp(self):
        """setUp method creating text fixtures."""
        self.text = """But this is a very bad sentence.
This is also a no-good sentence.

"""
        self.text_with_checks_disabled_forever_tex = """
But this is a bad sentence.
% proselint: disable
There is doubtlessly an error in this one.
This sentence is also very bad.
Proselint should also check this sentence unrelentlessly.

"""
        self.text_with_checks_disabled_and_reenabled_tex = """
But this is a bad sentence.
% proselint: disable
There is doubtlessly an error in this one.
This sentence is also very bad.
% proselint: enable
Proselint should also check this sentence unrelentlessly.

"""
        self.text_with_checks_disabled_and_reenabled_html = """
But this is a bad sentence.
<!-- proselint: disable -->
There is doubtlessly an error in this one.
This sentence is also very bad.
<!-- proselint: enable -->
Proselint should also check this sentence unrelentlessly.

"""
        self.text_with_specific_check_disabled_tex = """
But this is a bad sentence.
% proselint: disable=nonwords.misc
There is doubtlessly an error in this one.
This sentence is also very bad.
% proselint: enable=nonwords.misc
Proselint should also check this sentence unrelentlessly.

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

    def test_checks_disabled_forever_tex(self):
        """Test that disabling all checks works on a (La)TeX document."""
        assert len(lint(self.text_with_checks_disabled_forever_tex)) == 1

    def test_checks_disabled_and_reenabled_tex(self):
        """Test that disabling and reenabling all checks works on a (La)TeX document."""
        assert len(lint(self.text_with_checks_disabled_and_reenabled_tex)) == 2

    def test_checks_disabled_and_reenabled_html(self):
        """Test that disabling and reenabling all checks works on an HTML document."""
        assert len(lint(self.text_with_checks_disabled_and_reenabled_html)) == 2

    def test_specific_check_disabled_tex(self):
        """Test that disabling a specific check works on a (La)TeX document."""
        assert len(lint(self.text_with_specific_check_disabled_tex)) == 3
