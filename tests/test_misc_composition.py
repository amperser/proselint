"""Tests for misc.composition check."""

from proselint.checks.misc.composition import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for misc.composition."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "His story is not honest.")
