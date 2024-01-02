"""Tests for weasel_words.misc check."""

from proselint.checks.weasel_words.misc import check

from .check import Check
from .conftest import _pass


def test_smoke():
    """Basic smoke test for weasel_words.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    # TODO: add test when check is implemented
