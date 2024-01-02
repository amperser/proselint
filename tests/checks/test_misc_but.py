"""Tests for misc.but check."""

from proselint.checks.misc.but import check

from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.but."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, """But I never start with the word "but".""")
    assert_pass(
        check,
        """I never start with the word "but", but might use it after a linebreak.""",
    )
