"""Tests for needless_variants.misc check."""
from proselint.checks.needless_variants import misc
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def check(text: str) -> list:
    # combined test
    result = []
    result.extend(misc.check_1(text))
    result.extend(misc.check_2(text))
    return result


def test():
    """Basic smoke test for needless_variants.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "It was an extensible telescope.")
