"""Tests for annotations.misc check."""

from proselint.checks.annotations.misc import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for annotations.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_pass(check, "Add it to the to do list.")
    assert_fail(check, "Add it to the TODO list.")
