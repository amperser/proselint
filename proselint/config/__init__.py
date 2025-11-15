"""Configuration for proselint."""

import json
from collections.abc import Hashable, Mapping
from importlib.resources import files
from itertools import chain
from pathlib import Path
from typing import TypeAlias, TypedDict, TypeVar, cast
from warnings import showwarning as warn

from proselint import config
from proselint.config import paths


class Config(TypedDict):
    """
    Configuration for proselint.

    Keys:
    - `max_errors`: the maximum allowable number of errors proselint can output
    - `checks`: a dictionary of check modules to enable or disable
    """

    max_errors: int
    checks: dict[str, bool]


DEFAULT = cast(
    "Config", json.loads((files(config) / "default.json").read_text())
)

Checks: TypeAlias = Mapping[str, "bool | Checks"]
KT_co = TypeVar("KT_co", bound=Hashable, covariant=True)
VT_co = TypeVar("VT_co", covariant=True)


def _deepmerge_dicts(
    base: dict[KT_co, VT_co], overrides: dict[KT_co, VT_co]
) -> dict[KT_co, VT_co]:
    # fmt: off
    return base | overrides | {
        key: (
            _deepmerge_dicts(b_value, o_value)  # pyright: ignore[reportUnknownArgumentType]
            if isinstance(b_value := base[key], dict)
            else o_value
        )
        for key in set(base) & set(overrides)
        if isinstance(o_value := overrides[key], dict)
    }


def _flatten_checks(checks: Checks, prefix: str = "") -> dict[str, bool]:
    return dict(
        chain.from_iterable(
            [(full_key, value)]
            if isinstance(value, bool)
            else _flatten_checks(value, full_key).items()
            for key, value in checks.items()
            for full_key in [f"{prefix}.{key}" if prefix else key]
        )
    )


def _sort_by_specificity(checks: dict[str, bool]) -> dict[str, bool]:
    """Sort selected checks by depth (specificity) in descending order."""
    return dict(
        sorted(
            checks.items(),
            key=lambda x: x[0].count("."),
            reverse=True,
        )
    )


def load_from(config_path: Path | None = None) -> Config:
    """
    Read various config paths, allowing user overrides.

    NOTE: This assumes that a `config_path` is valid if one is provided.
    """
    result = DEFAULT
    config_paths = paths.config_paths + ([config_path] if config_path else [])

    for path in config_paths:
        if path.is_file():
            result = _deepmerge_dicts(
                cast("dict[str, object]", result),
                json.loads(path.read_text()),  # pyright: ignore[reportAny]
            )
        if path.suffix == ".json" and (old := path.with_suffix("")).is_file():
            warn(
                f"{old} was found instead of a JSON file. Rename to {path}.",
                DeprecationWarning,
                "",
                0,
            )

    result = cast("Config", result)

    return Config(
        max_errors=result.get("max_errors", 0),
        checks=_sort_by_specificity(_flatten_checks(result.get("checks", {}))),
    )
