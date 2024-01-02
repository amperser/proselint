"""Tests for terms.denizen_labels check."""

from proselint.checks.terms.denizen_labels import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for terms.denizen_labels."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "He was definitely a Hong Kongite.")
