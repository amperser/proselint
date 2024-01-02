"""Test Butterick's symbols."""

from proselint.checks.typography import symbols
from tests.conftest import _fail, _pass


def test_ellipsis():
    """Find ... in a string."""
    check = symbols.check_ellipsis
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "The long and winding road...")

def test_copyright():
    """Find a (c) or (C) in a string."""
    check = symbols.check_copyright_symbol
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "Show me the money! (C)")
    assert _fail(check, "Show me the money! (c)")

def test_trademark():
    """Find a (TM) or (tm) in a string."""
    check = symbols.check_trademark_symbol
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "The Fresh Maker (TM)")
    assert _fail(check, "The Fresh Maker (tm)")

def test_registered_trademark():
    """Find a (r) or (R) in a string."""
    check = symbols.check_registered_trademark_symbol
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "Just Do It (R)")
    assert _fail(check, "Just Do It (r)")


def test_sentence_spacing():
    """Find a sentence followed by three or more spaces."""
    check = symbols.check_sentence_spacing
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "This is a sentence.   This is another.")


def test_multiplication():
    """Find an x between two digits."""
    check = symbols.check_multiplication_symbol
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "It is obvious that 2 x 2 = 4.")


def test_curly_quotes():
    """Find "" quotes in a string."""
    check = symbols.check_curly_quotes
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, """This is “a sentence”. Look at it.""")
    assert _fail(check, """“This should produce an error”, he said.""")
    assert _pass(check, "But this should not.")
    assert _fail(check, """Alas, "it should here too".""")
    assert _pass(check, '"A singular should not, though.')
