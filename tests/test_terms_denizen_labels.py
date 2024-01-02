"""Tests for terms.denizen_labels check."""

from proselint.checks.terms.denizen_labels import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for terms.denizen_labels."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "He was definitely a Hong Kongite.")
