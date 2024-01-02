"""Tests for needless_variants.misc check."""

from proselint.checks.needless_variants.misc import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for needless_variants.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "It was an extensible telescope.")
