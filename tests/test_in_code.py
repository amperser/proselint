"""Test that errors in code blocks are ignored."""
from __future__ import absolute_import
from __future__ import print_function

from .check import Check
from proselint.tools import lint

from nose.tools import assert_equals


class TestCheck(Check):
    """Test class for errors in code."""

    __test__ = True

    def test_html_code(self):
        """quotation marks in code blocks should always be ignored."""
        text = '<html>\n<body>\n<p>This is a test.</p>\n<code>mystring = ' \
               '"{hello world}"</code>\n</body>\n</html>\n'
        errors = lint(text)
        assert_equals(len(errors), 0)

    def test_markdown_code(self):
        """quotation marks in code blocks should always be ignored."""
        text = '\nHere is some preformatted code with double quotation ' \
               'marks:\n\n```\n"{hello world}"\n```\n'
        errors = lint(text)
        assert_equals(len(errors), 0)
