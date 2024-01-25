"""Tests for mondegreens.misc check."""

from proselint.checks.mondegreens.misc import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for mondegreens.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_pass(check, "... and laid him on the green.")
    assert_fail(check, "..and Lady Mondegreen.")
