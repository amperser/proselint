"""Tests for misc.greylist check."""

from proselint.checks.misc.greylist import check
from tests.conftest import _pass, _fail


def test_smoke():
        """Basic smoke test for misc.greylist."""
        assert _pass(check, "Smoke phrase with nothing flagged.")
        assert _fail(check, "She should utilize her knowledge.")


def test_with_utilized():
    """Don't produce an error when 'use' is used correctly."""
    assert _pass(check, "I use a hammer to drive nails into wood.")


def test_no_utilized():
    """Produce an error when 'utilize' is used in place of 'use'."""
    assert _fail(check, "I utilize a hammer to drive nails into wood.")