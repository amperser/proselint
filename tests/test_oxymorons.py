"""Tests for oxymorons.misc check."""

from proselint.checks.oxymorons.misc import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for oxymorons.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "He needed an exact estimate.")
