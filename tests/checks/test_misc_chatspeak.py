"""Tests for misc.chatspeak check."""

from proselint.checks.misc.chatspeak import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.chatspeak."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "BRB getting coffee.")
