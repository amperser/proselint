"""Tests for annotations.misc check."""

from proselint.checks.annotations.misc import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for annotations.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _pass(check, "Add it to the to do list.")
    assert _fail(check, "Add it to the TODO list.")
