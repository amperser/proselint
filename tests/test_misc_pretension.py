"""Tests for misc.pretension check."""

from proselint.checks.misc.pretension import check

from .conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for misc.pretension."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "We need to reconceptualize the project.")
