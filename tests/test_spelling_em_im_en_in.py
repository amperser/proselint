"""Tests for spelling.em_im_en_in check."""

from proselint.checks.spelling.em_im_en_in import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for spelling.em_im_en_in."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "We shall imbark on a voyage.")
