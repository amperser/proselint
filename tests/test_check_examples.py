"""Verify that checks pass or fail given examples."""

from itertools import chain, repeat
from operator import itemgetter

from pytest import mark

from proselint.registry.checks import Check

from .common import (
    assert_pass,
    extract_checks,
    get_module_names,
    verify_module,
)
from .examples import data


def _id(value: str | tuple[str, ...]) -> str:
    """Return parameter ID."""
    if isinstance(value, str):
        return value
    return str(len(value))


def test_check_examples_exist() -> None:
    """Verify that all check modules have examples."""
    data_modules = set(map(itemgetter(0), data))
    available_modules = set(get_module_names())
    a_diff = available_modules.difference(data_modules)
    b_diff = data_modules.difference(available_modules)
    assert a_diff == set(), f"Some modules lack examples: {', '.join(a_diff)}"
    assert b_diff == set(), f"Some examples do not exist: {', '.join(b_diff)}"


@mark.parametrize(("module_name", "should_fail", "should_pass"), data, ids=_id)
def test_check_examples(
    module_name: str, should_fail: tuple[str, ...], should_pass: tuple[str, ...]
) -> None:
    """Verify that check modules pass and fail respective examples."""
    module = verify_module(module_name)
    checks = extract_checks(module)
    for example in should_fail:
        result = list(
            chain.from_iterable(
                map(Check.check_with_flags, checks, repeat(example))
            )
        )
        assert result != [], (
            f"False negative against {module_name}: '{example}'"
        )
    for check in checks:
        assert_pass(check, should_pass)
