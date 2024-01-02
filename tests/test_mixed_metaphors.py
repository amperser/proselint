"""Tests for mixed_metaphors.misc check."""

from proselint.checks.mixed_metaphors import misc

from .conftest import _fail, _pass


def test_smoke_bottleneck():
    """Basic smoke test for check_bottleneck."""
    check = misc.check_bottleneck
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "The project produced a huge bottleneck.")


def test_smoke_misc():
    """Basic smoke test for check_misc."""
    check = misc.check_misc
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "Writing tests is not rocket surgery.")
