"""Tests for misc.debased check."""

from proselint.checks.misc.debased import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for misc.debased."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "This leaves much to be desired.")
