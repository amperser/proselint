"""Tests for terms.venery check."""

from proselint.checks.terms.venery import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for terms.venery."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "There was a group of alligators.")
