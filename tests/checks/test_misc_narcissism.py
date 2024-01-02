"""Tests for misc.narcissism check."""

from proselint.checks.misc.narcissism import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.narcissism."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(
        check,
        """In recent years, an increasing number of scientists have studied
         the problem in detail.""",
    )
