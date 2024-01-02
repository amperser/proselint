"""Tests for misc.metadiscourse check."""

from proselint.checks.misc.metadiscourse import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for misc.metadiscourse."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "It's based on the rest of this article.")
