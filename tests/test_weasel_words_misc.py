"""Tests for weasel_words.misc check."""

from proselint.checks.weasel_words.misc import check

from .conftest import assert_pass


def test():
    """Basic smoke test for weasel_words.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    # TODO: add test when check is implemented
