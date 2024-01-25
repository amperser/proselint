"""Tests for weasel_words.misc check."""

from proselint.checks.weasel_words.misc import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for weasel_words.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "Some people say this is bad.")
    assert_fail(check, "This is somewhat crazy.")
    assert_fail(check, "It is said this is wrong.")
