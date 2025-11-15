"""Test the tools module."""

from proselint.checks import __register__
from proselint.registry import CheckRegistry
from proselint.tools import LintFile

REGISTRY = CheckRegistry()
if not REGISTRY.checks:
    REGISTRY.register_many(__register__)
TEXT = """But this is a very bad sentence.
This is also a no-good sentence.

"""
TEXT_WITH_NO_NEWLINE = """A very bad sentence."""


def test_errors_sorted() -> None:
    """Test that errors are sorted by line and column number."""
    lines_and_cols = [e.pos for e in LintFile("", TEXT).lint()]
    assert sorted(lines_and_cols) == lines_and_cols


def test_on_no_newlines() -> None:
    """Test that lint works on text without a terminal newline."""
    assert len(LintFile("", TEXT_WITH_NO_NEWLINE).lint()) > 0
