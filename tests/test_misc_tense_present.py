"""Tests for misc.tense_present check."""

from proselint.checks.misc.tense_present import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for misc.tense_present."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "I did it on accident honestly.")
