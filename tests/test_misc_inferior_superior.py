"""Tests for misc.inferior_superior check."""

from proselint.checks.misc.inferior_superior import check

from .conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for misc.inferior_superior."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "It was more inferior than the alternative.")
