"""Tests for skunked_terms.misc check."""

from proselint.checks.skunked_terms.misc import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for skunked_terms.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "I gave an impassionate defence of the situation.")
