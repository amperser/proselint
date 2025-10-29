"""Common utilities for test cases."""

import importlib
from itertools import chain
from os import walk
from pathlib import Path
from types import ModuleType

from proselint.config.paths import proselint_path
from proselint.registry.checks import Check, Padding, engine


def engine_from(
    padding: Padding, opts: engine.RegexOptions | None = None
) -> engine.Engine:
    """Return the correct engine to use for a given `padding`."""
    return [engine.Fast, engine.Fancy][
        int(padding == Padding.STRICT_WORDS_IN_TEXT)
    ](opts)


def assert_pass(check: Check, examples: tuple[str, ...]) -> None:
    """Assert that the `check` does not produce results against `examples`."""
    for example in examples:
        assert list(check.check_with_flags(example)) == [], (
            f"False positive against {check.path}: '{example}'"
        )


def assert_fail(check: Check, examples: tuple[str, ...]) -> None:
    """Assert that the `check` produces results against `examples`."""
    for example in examples:
        assert list(check.check_with_flags(example)) != [], (
            f"False negative against {check.path}: '{example}'"
        )


def is_check(path: Path) -> bool:
    """Check whether a file should contain a check."""
    return path.suffix == ".py" and path.name != "__init__.py"


def get_check_paths() -> list[Path]:
    """Traverse through subdirectories and select check paths."""
    return [
        file
        for root, _, files in walk(proselint_path / "checks")
        for file in map(Path(root).__truediv__, files)
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
    except (ModuleNotFoundError, ImportError) as exc:
        raise ImportError(f"Could not import {name}") from exc


def extract_checks(module: ModuleType) -> list[Check]:
    """Extract `Check`s from a module without relying on the registry."""
    return list(
        chain.from_iterable(
            [value] if isinstance(value, Check) else value  # pyright: ignore[reportUnknownArgumentType]
            for attr in dir(module)
            if (
                attr != "__register__"
                and (
                    isinstance(value := getattr(module, attr), Check)  # pyright: ignore[reportAny]
                    or (
                        isinstance(value, tuple)
                        and all(isinstance(entry, Check) for entry in value)  # pyright: ignore[reportUnknownVariableType]
                    )
                )
            )
        )
    )
