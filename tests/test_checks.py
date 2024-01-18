from __future__ import annotations

import importlib
import os
import re
from pathlib import Path

import pytest

import proselint


def is_check(file_path: Path) -> bool:
    """Check whether a file contains a check."""
    if file_path.suffix != ".py":
        return False
    if file_path.name == "__init__.py":
        return False
    if "inprogress" in file_path.as_posix():
        return False
    return True


def get_check_files() -> list[Path]:
    """traverses through all subdirs and selects
    .py-files that are in a module (have an __init__.py) and are
    not in "inprogress"-dir
    """
    # todo: duplicated code, test_config_default
    checks_path = (proselint.path / "checks").absolute()
    results = []
    for _root, _, _files in os.walk(checks_path):
        root_path = Path(_root)
        for _file in _files:
            file_path = root_path / _file
            if is_check(file_path):
                if not (file_path.parent / "__init__.py").exists():
                    raise FileNotFoundError("Check-Directory is missing '__init__.py'")
                results.append(file_path)
    return results


def get_module_names() -> list[str]:
    """transform file-list to importable module names"""
    result = []
    for _file in get_check_files():
        path_relative = _file.relative_to(proselint.path)
        module_name = path_relative.with_suffix("").as_posix().replace("/", ".")
        print(module_name)
        result.append(module_name)
    return result


@pytest.mark.parametrize("module_name", get_module_names())
def test_check(module_name: str) -> None:
    """ this checks multiple things:
    - successful import of check
    - example_fail and _pass present in file
    - both example-lists with at least one entry
    - successful testing of these examples

    """
    try:
        module = importlib.import_module("." + module_name, "proselint")
    except ModuleNotFoundError as _xpt:
        raise ImportError(f"Is {module_name} broken?") from _xpt

    checks = {d: getattr(module, d) for d in dir(module) if re.match(r"^check", d)}
    try:
        if len(module.examples_pass) < 1:
            # TODO: raise to two as min
            raise ValueError(
                f"there are no passing examples for testing in {module_name}"
            )
        for example in module.examples_pass:
            for _name, _check in checks.items():  # not-any config
                assert (
                    _check(example) == []
                ), f"false positive - {_name}('{example}')"
    except AttributeError as _xpt:
        raise AttributeError(f"'examples_pass' missing in {module_name}") from _xpt

    try:
        if len(module.examples_fail) < 1:
            raise ValueError(
                f"there are no failing examples for testing in {module_name}"
            )
        for example in module.examples_fail:
            result = []
            for check in checks.values():  # any-config
                result.extend(check(example))
            assert (
                result != []
            ), f"false negative (did NOT trigger) - {module_name}: '{example}'"
    except AttributeError as _xpt:
        raise AttributeError(f"'examples_fail' missing in {module_name}") from _xpt
