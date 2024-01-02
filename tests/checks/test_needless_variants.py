"""Tests for needless_variants.misc check."""

from proselint.checks.needless_variants.misc import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for needless_variants.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "It was an extensible telescope.")
