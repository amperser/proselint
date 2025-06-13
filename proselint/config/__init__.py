"""Configuration for proselint."""

import copy
import json
from importlib.resources import files
from pathlib import Path
from typing import Optional, TypedDict
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


DEFAULT: Config = json.load(files(config).joinpath("default.json").open())


def _deepmerge_dicts(base: dict, overrides: dict) -> dict:
    return base | overrides | {
        key: (
            _deepmerge_dicts(b_value, o_value)
            if isinstance(b_value := base[key], dict)
            else o_value
        )
        for key in set(base) & set(overrides)
        if isinstance(o_value := overrides[key], dict)
    }


def load_from(config_path: Optional[Path] = None) -> Config:
    """
    Read various config paths, allowing user overrides.

    NOTE: This assumes that a `config_path` is valid if one is provided.
    """
    result = DEFAULT
    config_paths = paths.config_paths + ([config_path] if config_path else [])

    for path in config_paths:
        if path.is_file():
            result: Config = _deepmerge_dicts(result, json.load(path.open()))
        if path.suffix == ".json" and (old := path.with_suffix("")).is_file():
            warn(
                f"{old} was found instead of a JSON file. Rename to {path}.",
                DeprecationWarning,
                "",
                0,
            )

    return result
