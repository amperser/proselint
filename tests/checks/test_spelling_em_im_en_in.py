"""Tests for spelling.em_im_en_in check."""

from proselint.checks.spelling.em_im_en_in import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for spelling.em_im_en_in."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "We shall imbark on a voyage.")
