"""Tests for needless_variants.misc check."""

from proselint.checks.needless_variants import misc
from proselint.checks import ResultCheck
from tests.conftest import assert_fail, assert_pass


def check(text: str) -> list[ResultCheck]:
    # combined test
    result = []
    result.extend(misc.check_1(text))
    result.extend(misc.check_2(text))
    return result


def test():
    """Basic smoke test for needless_variants.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "It was an extensible telescope.")
