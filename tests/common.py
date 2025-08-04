"""Common utilities for test cases."""

import importlib
from itertools import chain
from pathlib import Path
from types import ModuleType

from proselint.config.paths import proselint_path
from proselint.registry.checks import Check


def assert_pass(check: Check, examples: tuple[str, ...]) -> None:
    """Assert that the `check` does not produce results against `examples`."""
    for example in examples:
        assert check.check(example) == []


def assert_fail(check: Check, examples: tuple[str, ...]) -> None:
    """Assert that the `check` produces results against `examples`."""
    for example in examples:
        assert check.check(example) != []


def is_check(path: Path) -> bool:
    """Check whether a file should contain a check."""
    return path.suffix == ".py" and path.name != "__init__.py"


def get_check_paths() -> list[Path]:
    """Traverse through subdirectories and select check paths."""
    return [
        file
        for root, _, files in (proselint_path / "checks").walk()
        for file in map(root.__truediv__, files)
        if is_check(file) and (file.parent / "__init__.py").exists()
    ]


def get_module_names() -> list[str]:
    """Transform a list of check paths to importable module names."""
    return [
        file.relative_to(proselint_path / "checks")
        .with_suffix("")
        .as_posix()
        .replace("/", ".")
        for file in get_check_paths()
    ]


def verify_module(name: str) -> ModuleType:
    """Verify that a module is importable."""
    try:
        return importlib.import_module(f".{name}", "proselint.checks")
    except ModuleNotFoundError as exc:
        raise ImportError(f"Is {name} broken?") from exc


def extract_checks(module: ModuleType) -> list[Check]:
    """Extract `Check`s from a module without relying on the registry."""
    return list(
        chain.from_iterable(
            [x] if isinstance(x, Check) else x  # pyright: ignore[reportUnknownArgumentType]
            for d in dir(module)
            if (
                d != "__register__"
                and (
                    isinstance(x := getattr(module, d), Check)  # pyright: ignore[reportAny]
                    or (
                        isinstance(x, tuple)
                        and all(isinstance(entry, Check) for entry in x)  # pyright: ignore[reportUnknownVariableType]
                    )
                )
            )
        )
    )
