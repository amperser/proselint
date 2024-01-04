"""Tests for spelling.ely_ly check."""

from proselint.checks.spelling.ely_ly import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for spelling.ely_ly."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "She was completly unprepared.")
