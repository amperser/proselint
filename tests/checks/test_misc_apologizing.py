"""Tests for misc.apologizing check."""

from proselint.checks.misc.apologizing import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for misc.apologizing."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "More research is needed.")
