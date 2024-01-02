"""Tests for misc.narcissism check."""

from proselint.checks.misc.narcissism import check

from .conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for misc.narcissism."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(
        check,
        """In recent years, an increasing number of scientists have studied
         the problem in detail.""",
    )
