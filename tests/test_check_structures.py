"""Verify check structures."""

from collections.abc import Collection
from typing import TypeVar

from pytest import mark

from proselint.registry.checks import BATCH_COUNT, types

from .common import extract_checks, get_module_names, verify_module

T = TypeVar("T")


def eq_unordered(a: Collection[T], b: Collection[T]) -> bool:
    """Check whether a and b are equal, irrespective of order."""
    return all(x in b for x in a) and all(x in a for x in b)


@mark.parametrize("module_name", get_module_names())
def test_module_register(module_name: str) -> None:
    """Verify that a check module has a register, and registers its checks."""
    module = verify_module(module_name)
    assert "__register__" in dir(module), f"{module_name} has no register."
    assert eq_unordered(module.__register__, extract_checks(module)), (  # pyright: ignore[reportAny]
        f"{module_name} does not register all viable checks."
    )


@mark.parametrize("module_name", get_module_names())
def test_check_paths(module_name: str) -> None:
    """Verify that check paths match the module they reside in."""
    checks = extract_checks(verify_module(module_name))
    for check in checks:
        assert module_name in check.path, (
            f"{check.path} does not contain {module_name}."
        )
        assert check.matches_partial(module_name), (
            f"{check.path} fails matches_partial against {module_name}."
        )


@mark.parametrize("module_name", get_module_names())
def test_check_batching(module_name: str) -> None:
    """Verify that checks adhere to the global batch count."""
    checks = extract_checks(verify_module(module_name))
    for check in checks:
        if isinstance(
            check.check_type,
            (types.Existence, types.PreferredForms, types.PreferredFormsSimple),
        ):
            items = check.check_type.items
        elif isinstance(check.check_type, types.Consistency):
            items = check.check_type.term_pairs
        else:
            continue
        assert len(items) <= int(BATCH_COUNT * 1.05), (
            f"{check.path} has too many items ({len(items)} vs. {BATCH_COUNT})."
        )
