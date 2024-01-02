"""Tests for misc.chatspeak check."""

from proselint.checks.misc.chatspeak import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for misc.chatspeak."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "BRB getting coffee.")
