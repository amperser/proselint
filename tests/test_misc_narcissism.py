"""Tests for misc.narcissism check."""

from proselint.checks.misc.narcissism import check

from .check import Check
from .conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for misc.narcissism."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check,
        """In recent years, an increasing number of scientists have studied
         the problem in detail.""",
    )
