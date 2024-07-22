from __future__ import annotations

import importlib
from os import walk
from pathlib import Path
from types import ModuleType

import pytest

import proselint
from proselint.checks import CheckSpec


def is_check(file_path: Path) -> bool:
    """Check whether a file should contain a check."""
    # TODO: there are 3 variations of check
    # refactor when preview is implemented
    return (
        "_template" not in file_path.as_posix()
        and file_path.suffix == ".py"
        and file_path.name != "__init__.py"
    )


def get_check_files() -> list[Path]:
    """
    Traverse through subdirectories and select valid check files.

    These are .py files outside of the template directory that are in an
    explicit module (i.e. they have an associated __init__.py).
    """
    # TODO: duplicated code, test_config_default
    checks_path = (proselint.path / "checks").absolute()
    results = []
    for root, _, files in walk(checks_path):
        root_path = Path(root)
        for file in files:
            file_path = root_path / file
            if not is_check(file_path):
                continue
            if not (file_path.parent / "__init__.py").exists():
                raise FileNotFoundError(
                    "Check directory '%s' is missing an '__init__.py'"
                    % root_path
                )
            results.append(file_path)
    return results


def get_module_names() -> list[str]:
    """Transform file list to importable module names."""
    return [
        file.relative_to(next(iter(proselint.checks.__path__)))
        .with_suffix("")
        .as_posix()
        .replace("/", ".")
        for file in get_check_files()
    ]


# ######### Unittests
def verify_examples(module: ModuleType, name: str, attr: str) -> list[str]:
    """Check that examples are present lists with at least one entry."""
    if not hasattr(module, attr):
        raise AttributeError(f"'{attr}' missing in {name}")

    examples = getattr(module, attr)
    if not isinstance(examples, list) or len(examples) < 1:
        raise ValueError(f"'{attr}' must have 1 or more test entries in {name}")
    return examples


def verify_module(module_name: str) -> ModuleType:
    """Check that a module is importable."""
    try:
        module = importlib.import_module(f".{module_name}", "proselint.checks")
    except ModuleNotFoundError as exc:
        raise ImportError(f"Is {module_name} broken?") from exc
    return module


def extract_checks(module: ModuleType) -> list[CheckSpec]:
    """Extract `CheckSpec`s from a module."""
    return [
        x for d in dir(module) if isinstance(x := getattr(module, d), CheckSpec)
    ]


@pytest.mark.parametrize("module_name", get_module_names())
def test_check(module_name: str) -> None:
    """
    Test for a successful import with present examples and test those examples.

    For successful imports, see `verify_module`.
    For present examples, see `verify_examples`.
    """
    module = verify_module(module_name)
    checks = extract_checks(module)

    examples_pass = verify_examples(module, module_name, "examples_pass")
    for example in examples_pass:
        for check in checks:  # not-any config
            assert (
                check.dispatch_with_flags(example) == []
            ), f"False positive - {check.path}('{example}')"

    examples_fail = verify_examples(module, module_name, "examples_fail")
    for example in examples_fail:
        result = []
        for check in checks:  # any-config
            result.extend(check.dispatch(example))
        assert (
            result != []
        ), f"False negative (did NOT trigger) - {module_name}: '{example}'"


@pytest.mark.parametrize("module_name", get_module_names())
def test_check_paths(module_name: str) -> None:
    """Test that check paths match the module they reside in."""
    checks = extract_checks(verify_module(module_name))
    for check in checks:
        assert check.matches_partial(
            module_name
        ), f"{check.path} does not match {module_name}"
