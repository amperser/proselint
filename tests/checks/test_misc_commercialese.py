"""Tests for misc.commercialese check."""

from proselint.checks.misc.commercialese import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def tests():
    """Basic smoke test for misc.commercialese."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "We regret to inform you of this.")
