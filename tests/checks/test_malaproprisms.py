"""Tests for malaproprisms.misc check."""

from proselint.checks.malapropisms.misc import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for malaproprisms.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "Found in the Infinitesimal Universe.")
