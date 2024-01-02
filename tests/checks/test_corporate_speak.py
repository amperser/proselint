"""Tests for corporate_speak.misc check."""

from proselint.checks.corporate_speak.misc import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for corporate_speak.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_pass(check, "We will discuss it later.")
    assert_fail(check, "We will circle back around to it.")
