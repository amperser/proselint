"""Tests for misc.whence check."""

from proselint.checks.misc.whence import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for misc.whence."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "Go back from whence you came!")
