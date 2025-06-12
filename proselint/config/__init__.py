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
    result = copy.deepcopy(base)

    for key, value in overrides.items():
        if isinstance(value, dict):
            result[key] = _deepmerge_dicts(result.get(key, {}), value)
        else:
            result[key] = value

    return result


def load_from(config_path: Optional[Path] = None) -> Config:
    """Read various config paths, allowing user overrides."""
    result = DEFAULT
    config_paths = copy.deepcopy(paths.config_paths)

    if config_path:
        if not config_path.is_file():
            raise FileNotFoundError(
                f"Config file {config_path} does not exist."
            )
        config_paths.append(config_path)

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
