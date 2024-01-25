"""Tests for misc.composition check."""

from proselint.checks.misc.composition import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for misc.composition."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "His story is not honest.")
