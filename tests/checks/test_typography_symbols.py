"""Test Butterick's symbols."""

from proselint.checks.typography.symbols import check
from tests.conftest import assert_fail, assert_pass


def test_ellipsis():
    """Find ... in a string."""
    # check = symbols.check_ellipsis
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The long and winding road...")


def test_copyright():
    """Find a (c) or (C) in a string."""
    # check = symbols.check_copyright_symbol
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "Show me the money! (C)")
    assert_fail(check, "Show me the money! (c)")


def test_trademark():
    """Find a (TM) or (tm) in a string."""
    # check = symbols.check_trademark_symbol
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The Fresh Maker (TM)")
    assert_fail(check, "The Fresh Maker (tm)")


def test_registered_trademark():
    """Find a (r) or (R) in a string."""
    # check = symbols.check_registered_trademark_symbol
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "Just Do It (R)")
    assert_fail(check, "Just Do It (r)")


def test_sentence_spacing():
    """Find a sentence followed by three or more spaces."""
    # check = symbols.check_sentence_spacing
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "This is a sentence.   This is another.")


def test_multiplication():
    """Find an x between two digits."""
    # check = symbols.check_multiplication_symbol
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "It is obvious that 2 x 2 = 4.")


def test_curly_quotes():
    """Find "" quotes in a string."""
    # check = symbols.check_curly_quotes
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_pass(check, """This is “a sentence”. Look at it.""")
    assert_fail(check, """This is "another sentence". How faulty.""")
    assert_fail(check, """"This should produce an error", he said.""")
    assert_pass(check, """“This should produce no error”, he said.""")
    assert_fail(check, """Alas, "it should here too".""")
    assert_pass(check, """A 'singular' should not, though.""")
