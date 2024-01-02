"""Tests for misc.metadiscourse check."""

from proselint.checks.misc.metadiscourse import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.metadiscourse."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "It's based on the rest of this article.")
