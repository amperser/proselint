"""Test the tools module."""

from __future__ import annotations

from proselint.tools import lint


def extract_line_col(error):
    """Extract the line and column number from an error tuple."""
    _, _, _, line, column, _, _, _, _, _ = error
    return line, column


def test_errors_sorted():
    """Test that errors are sorted by line and column number."""
    text = """But this is a very bad sentence.
    This is also a no-good sentence.

    """
    lines_and_cols = [extract_line_col(e) for e in lint(text)]
    assert sorted(lines_and_cols) == lines_and_cols


def test_on_no_newlines():
    """Test that lint works on text without a terminal newline."""
    text_with_no_newline = "A very bad sentence."
    assert len(lint(text_with_no_newline)) > 0
