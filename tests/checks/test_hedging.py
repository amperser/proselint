"""Tests for hedging.misc check."""

from proselint.checks.hedging.misc import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for hedging.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "I would argue that this is a good test.")
