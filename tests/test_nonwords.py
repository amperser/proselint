"""Tests for nonwords.misc check."""

from proselint.checks.nonwords.misc import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for nonwords.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "The test was good irregardless.")
